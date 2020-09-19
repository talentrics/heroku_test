from flask import Flask,render_template,request,redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
   return render_template('/index.html')

@app.route('/about')
def main():
   return render_template('/about.html')

@app.route('/talentrics')
def main():
   return render_template('/talentrics.html')