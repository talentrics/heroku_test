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