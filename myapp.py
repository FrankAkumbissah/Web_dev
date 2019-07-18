from flask import *
import json
import os
 
app = Flask(__name__)

items = []

@app.route('/add_todo')
def add_todo():
     item = request.args.get("item")
     print(item)
     items.append(item)
     return redirect("http://localhost:5000/", code = 302)
    
@app.route('/get_todos')
def get_todos():
    resp = Response(json.dumps(items))
    resp.headers['Content-Type'] = 'application/json'
    return resp
 
@app.route('/')
def index():
    return render_template('form.html', items = items)
 
@app.route('/home')
def index1():
     return render_template("home.html")
    
@app.route('/about')
def about():
     return render_template("about.html")
 
@app.route('/services')
def services():
     return render_template("services.html") 
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)
