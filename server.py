from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total_items = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['blackberry']) + int(request.form['apple'])
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total_items} fruits")
    return render_template("checkout.html",customer = request.form, total_items=total_items, date_time=dt)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    