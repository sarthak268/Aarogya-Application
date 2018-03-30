from flask import Flask, render_template,request, jsonify
from return_ans import *
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from flask_bootstrap import Bootstrap

app= Flask(__name__)
app.config['SECRET_KEY'] = "Thisissupposedtobesecret"
bootstrap = Bootstrap(app)

class prevention(FlaskForm):
	disease1 = StringField('disease',validators=[InputRequired(),Length(min=2,max=50)])

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/send')
def send():
	L = find_nearest_doctors(28.560280, 77.291332)
	return jsonify(L)


@app.route('/d1')
def prevention_methods(methods=['GET','POST']):
	form = prevention()
	if(form.validate_on_submit()):
		disease = prevention(disease = form.disease1.data)
	links = []
	for url in search('Prevention methods of ' + disease, tld = 'es', lang = 'es', stop = 20):
		links.append(url)
	ind = random.randint(0,len(links) - 1)	
	webbrowser.open_new_tab(links[ind])

if __name__ == '__main__':
	app.run(debug=True)