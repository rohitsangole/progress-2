from flask import Flask, request, render_template,flash,redirect,session,abort,jsonify
from models import Model


import os

app = Flask(__name__)


@app.route('/')
def root():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'rohit' and request.form['username'] == 'rohit':
        session['logged_in'] = True
        
    elif request.form['password'] == 'gan' and request.form['username'] == 'gan':
        session['logged_in'] = True
        
    else :
        flash('wrong password!')
    return root()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return root()


@app.route("/sentiment")
def sentiment():
    return render_template("sentiment.html")




@app.route('/predict', methods=["POST"])
def predict():
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    
  
    if prediction[0] == 0:
            result = 'Your Stress test result : No Stress'
    if prediction[0] == 1:
            result = 'Your Stress test result : Mild Stress'
    if prediction[0] == 2:
            result = 'Your Stress test result : Moderate Stress (Kindly Take Advanced Stress Test)'
    if prediction[0] == 3:
            result = 'Your Stress test result : Moderately severe Stress (Kindly Take Advanced Stress Test)'
    if prediction[0] == 4:
            result = 'Your Stress test result : Severe Stress (Kindly Take Advanced Stress Test)'
    
    return render_template("result.html", result=result)

@app.route('/normal', methods=["POST"])
def respect():
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    
    
    if prediction[0] == 0:
            result = 'Your Stress test result : No Stress'
    if prediction[0] == 1:
            result = 'Your Stress test result : Mild Stress'
    if prediction[0] == 2:
            result = 'Your Stress test result : Moderate Stress (Kindly Go to the Explore Section)'
    if prediction[0] == 3:
            result = 'Your Stress test result : Moderately severe Stress (Kindly go to the Explore Section)'
    if prediction[0] == 4:
            result = 'Your Stress test result : Severe Stress (Kindly go to the Explore Section)'
    return render_template("esult.html", result=result)





app.secret_key = os.urandom(12)
app.run(port=5987, host='0.0.0.0', debug=True)