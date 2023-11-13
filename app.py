from flask import Flask, request, jsonify, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from models import Item, db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = request.form['quantity']
    item_type = request.form['type']  # New field
    dimensions = request.form['dimensions']  # New field

    new_item = Item(name=name, quantity=quantity, type=item_type, dimensions=dimensions)

    db.session.add(new_item)
    db.session.commit()

    return 'Item added successfully!'

@app.route('/items', methods=['GET'])
def view_items():
    items = Item.query.all()
    item_list = [{"id": item.id, "name": item.name, "quantity": item.quantity, "type": item.type, "dimensions": item.dimensions} for item in items]
    return jsonify(item_list)

@app.route('/update_item/<int:item_id>', methods=['POST'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)

    item.name = request.form['name']
    item.quantity = request.form['quantity']
    item.type = request.form['type']  # Update the type
    item.dimensions = request.form['dimensions']  # Update the dimensions

    db.session.commit()

    return 'Item updated successfully!'

@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)

    db.session.delete(item)
    db.session.commit()

    return 'Item deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
