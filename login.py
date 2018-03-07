from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)


''' app.route function tells the url format and in our function index() basic page is called for submitting the aadhar number and the epic number
'''
@app.route('/')
def index():
   return render_template('login.html')	#will redirect to the login page


@app.route('/results/<result>')
def results(result):
	
	if result == '1':
		bot = 'Aadhar Invalid'
	if result == '2':
		bot = 'EPIC Invalid'
	if result == '3':
		bot = 'Aadhar and Epic Invalid'
	if result == '0':
		return render_template('result.html') 
  #will redirect to the result page which displays message for successful login and provides the logout option
	else:
		return render_template('failure.html', bot=bot) 
  #will redirect to the failure page which displays message for unsuccessful login and provides the link for the login page'''


#when the user clicks on the submit button of login page then this function is called.It takes input the aadhar no. and epic no. and checks the authenticity''' 
@app.route('/login',methods = ['POST','GET'])
def login():
	if request.method == 'POST':
		flag=0
		aadhar_no = request.form['aadhar_no']
		epic_no = request.form['epic_no']
		if len(aadhar_no) != 12:
			flag=1
			return redirect(url_for('results',result = flag))
		else:
			for i in aadhar_no:
				if i.isdigit()==False:
					flag=1
					return redirect(url_for('results',result = flag))
		if len(epic_no) != 10:
			flag=2
			return redirect(url_for('results',result = flag))
		else:
			for i in epic_no[:3]:
				if i.isalpha()==False:
					flag=2
					return redirect(url_for('results',result = flag))
			for i in epic_no[3:]:
				if i.isdigit()==False:
					flag=2
					return redirect(url_for('results',result = flag))
		return redirect(url_for('results',result = flag))
			


if __name__ == '__main__':
   app.run()
