from phew import logging, server, access_point, dns
from phew.template import render_template
from phew.server import redirect
import morse
import chat


DOMAIN = "pico.survival"

@server.route("/", methods=['GET'])
def index(request):
    """ Render the Index page"""
    if request.method == 'GET':
        logging.debug("Get request")
        return render_template("index.html")

# microsoft windows redirects
@server.route("/ncsi.txt", methods=["GET"])
def hotspot(request):
    print(request)
    print("ncsi.txt")
    return "", 200


@server.route("/connecttest.txt", methods=["GET"])
def hotspot(request):
    print(request)
    print("connecttest.txt")
    return "", 200


@server.route("/redirect", methods=["GET"])
def hotspot(request):
    print(request)
    print("****************ms redir*********************")
    return redirect(f"http://{DOMAIN}/", 302)

# android redirects
@server.route("/generate_204", methods=["GET"])
def hotspot(request):
    print(request)
    print("******generate_204********")
    return redirect(f"http://{DOMAIN}/", 302)

# apple redir
@server.route("/hotspot-detect.html", methods=["GET"])
def hotspot(request):
    print(request)
    """ Redirect to the Index Page """
    return render_template("index.html")


@server.catchall()
def catch_all(request):
    print("***************CATCHALL***********************\n" + str(request))
    return redirect("http://" + DOMAIN + "/")

@server.route("/morse", methods=['GET'])
def morse_page(request):
    if request.method == 'GET':
        return render_template("morse.html")

@server.route("/morse", methods=['POST'])
def morse_input(request):
    if request.method == 'POST':
        morse_code_input = request.form['morseInput']
        for character in morse_code_input:
            morse.send_morse(character)
        return render_template("morse.html")

@server.route("/chat", methods=['GET'])
def chat_page(request):
    if request.method == 'GET':
        messages_html = chat.get_messages()
        full_page_html = generate_full_chat_page(messages_html)
        return full_page_html

def generate_full_chat_page(messages_html):
    # Construct the full HTML for the chat page
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Message Board</title>
    </head>
    <body>
        <h1>Pi Pico Message Board</h1>
        <form action="/send_message" method="post">
            <label for="callsign">Callsign:</label>
            <input type="text" id="callsign" name="callsign" required><br>
            <label for="message">Message:</label>
            <input type="text" id="message" name="message" required><br>
            <input type="submit" value="Send">
        </form>
        <br>
        <div id="messages">
            {messages_html}
        </div>
        <br>
        <a href="/">Return to Index</a>
    </body>
    </html>
    """
    return html_content
 
@server.route("/send_message", methods=['POST'])
def send_message(request):
    if request.method == 'POST':
        callsign = request.form['callsign']
        message = request.form['message']
        chat.add_message(callsign, message)

    # Redirect to the chat page after adding a message
    return redirect(f"http://{DOMAIN}/chat") 

def parse_post_data(body):
    # Parse the body to extract callsign and message
    # This is a simplified parser and might need adjustment based on the actual format of POST data
    parts = body.split('&')
    callsign = parts[0].split('=')[1]
    message = parts[1].split('=')[1]
    return callsign, message

def generate_chat_page_with_messages():
    with open('chat.html', 'r') as file:
        page = file.read()
    messages_html = chat.get_messages()
    page_with_messages = page.replace('</body>', f'{messages_html}</body>')  # Insert messages before the body tag ends
    return page_with_messages

# Set to Accesspoint mode
# Change this to whatever Wifi SSID you wish
ap = access_point("Pico EmgSrv")
ip = ap.ifconfig()[0]
# Grab the IP address and store it
logging.info(f"starting DNS server on {ip}")
# # Catch all requests and reroute them
dns.run_catchall(ip)
server.run() # Run the server
logging.info("Webserver Started")
