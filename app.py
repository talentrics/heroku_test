from flask import Flask,render_template,request,redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
   return render_template('/index.html')

@app.route('/about')
def about():
   return render_template('/about.html')

@app.route('/talentrics')
def talentrics():
   return render_template('/talentrics.html')

@app.route('/danielbmacdonald')
def danielbmacdonald():
   return render_template('/danielbmacdonald.html')

@app.route('/github')
def github():
   return render_template('/github.html')

@app.route('/guide')
def guide():
   return render_template('/guide.html')

@app.route('/tutorial')
def tutorial():
   return render_template('/tutorial.html')