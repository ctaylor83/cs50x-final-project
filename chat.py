import utime

messages = []  # List to store messages

def escape_html(text):
    """Escape HTML special characters in text."""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#039;"))

def get_formatted_time():
    """Returns the current time formatted as YYYY-MM-DD HH:MM:SS"""
    year, month, mday, hour, minute, second, _, _ = utime.localtime()
    return f"{year:04d}-{month:02d}-{mday:02d} {hour:02d}:{minute:02d}:{second:02d}"

# Usage in add_message function
def add_message(callsign, message):
    """Add a new message to the list with a timestamp."""
    timestamp = get_formatted_time()
    messages.append({"timestamp": timestamp, "callsign": callsign, "message": message})

def get_messages():
    """Return a string representation of all messages."""
    message_elements = []
    for msg in messages:
        timestamp = msg['timestamp']
        callsign = escape_html(msg['callsign'])
        message = escape_html(msg['message'])
        message_html = f"<div><span>{timestamp}</span> <b>{callsign}</b>: {message}<br></div>"
        message_elements.append(message_html)
    return "".join(message_elements)