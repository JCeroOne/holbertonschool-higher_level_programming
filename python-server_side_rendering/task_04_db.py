import sqlite3
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

  if src not in ["json", "csv", "sql"]:
    return render_template('product_display.html', error="Wrong source")

  data = []

  if src in ["json", "csv"]:
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
  else:
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, category, price FROM products"
        )

        rows = cursor.fetchall()

        for row in rows:
            data.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()

    except Exception as e:
        return render_template(
            "product_display.html",
            error="Database error"
        )
