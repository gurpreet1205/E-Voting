from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////users/gurpr/Desktop/evote/eVoting.sqlite3'


db = SQLAlchemy(app)

class Aadhar(db.Model):
    __tablename__ = 'Aadhar'
    number = db.Column('number', db.Unicode, primary_key=True)
    name = db.Column('name', db.Unicode)


class Epic(db.Model):
    __tablename__ = 'Epic'
    number = db.Column('number', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)

#app.route function tells the url format and in our function index() basic page is called for submitting the aadhar number and the epic number

@app.route('/')
def index():
	return render_template('login.html')

#will redirect to the login page


@app.route('/results/<result>/<name>')
def results(result , name ):
    if result == '1':
        bot = 'Aadhar Invalid'

    if result == '2':
        bot = 'EPIC Invalid'

    if result == '3':
        bot = 'Aadhar and Epic Invalid'
    if result == '4':
        bot = 'Aadhar and Epic Name Not Matching'

    if result == '5':
        bot = 'Aadhar or Epic number not found . Pls register'

    if result == '0':
        return render_template('result.html' ,  name = name)
  #will redirect to the result page which displays message for successful login and provides the logout option
    else:
        return render_template('failure.html', bot = bot)
  #will redirect to the failure page which displays message for unsuccessful login and provides the link for the login page


#when the user clicks on the submit button of login page then this function is called.It takes input the aadhar no. and epic no. and checks the authenticity
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        flag=0
        aadhar_name = ""
        epic_name = ""
        aadhar_no = request.form['aadhar_no']
        epic_no = request.form['epic_no']
        if len(aadhar_no) != 12:
            flag=1
            return redirect(url_for('results',result = flag , name = " "))
        else:
            for i in aadhar_no:
                if i.isdigit()==False:
                    flag=1
                    return redirect(url_for('results',result = flag ,name = " "))
        try:
            ex = Aadhar.query.filter_by(number=aadhar_no).all()
            aadhar_name = ex[0].name
        except:
            flag = 5 
            return redirect(url_for('results',result = flag , name = " "))
        if len(epic_no) != 10:
            flag=2
            return redirect(url_for('results',result = flag , name = " "))
        else:
            for i in epic_no[:3]:
                if i.isalpha()==False:
                    flag=2
                    return redirect(url_for('results',result = flag,name = " "))
                for i in epic_no[3:]:
                    if i.isdigit()==False:
                        flag=2
                        return redirect(url_for('results',result = flag,name = " "))
        try:
            ex = Epic.query.filter_by(number=epic_no).all()
            epic_name = ex[0].name
        except:
            flag = 5
            return redirect(url_for('results',result = flag,name = " "))
        if aadhar_name != epic_name:
            flag = 4

        return redirect(url_for('results', result = flag , name = aadhar_name))


if __name__ == '__main__':
   app.run()
