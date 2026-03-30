from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open("items.json", "r") as f:
            data = json.load(f)
            items_list = data.get("items", [])
    
    except Exception:
        items_list = []
    
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
  src = request.args.get("source")
  id = request.args.get("id")

  if src not in ["json", "csv"]:
    return render_template('product_display.html', error="Wrong source")

  data = []
  file = f"products.{src}"

  try:
    with open(file, "r") as f:
      
      if src == "json":
        data = json.load(f)
      
      else:
        reader = csv.DictReader(f)
        for row in reader:
          row["id"] = int(row["id"])
          row["price"] = float(row["price"])
          data.append(row)
        
  except Exception:
    data = []

  if id:
    try:
      id = int(id)
      data = [p for p in data if p.get('id') == id]
    except ValueError:
      data = []
    
    if not data:
        return render_template('product_display.html', error="Product not found")

  return render_template('product_display.html', products=data)
  
if __name__ == '__main__':
   app.run(debug=True, port=5000)
