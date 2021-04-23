import json
from flask import Flask
from flask import render_template

from flask import Flask, request,redirect,url_for,jsonify

app= Flask(__name__)

@app.route('/')
def index():
    users=['rose','jasmine','lily']
    return render_template('index.html',title='welcome',usernames=users)

@app.route('/hello')
def hello_world():
    return jsonify({'name':'rose','email':'rose@rose.com'})

@app.route('/login',methods =['POST','GET'])
def login():
    if request.method=='POST':
        user= request.form['name']
        return redirect(url_for('dashboard',name=user))
    else:
        user1=request.args.get('name')
        return render_template('login.html')

@app.route('/dashboard/<name>')
def dashboard(name):
    return "Welcome" + name

@app.route('/sale/<transaction_id>')
def displaytid(transaction_id=0):
    return "The Transaction id is :" +str(transaction_id)

@app.route('/json')
def readjsonvariable():
    person='{"name":"mudassar","languages":["english","hindi"]}'
    person_dict=json.loads(person)
    if "english" in person_dict['languages']:
        return person_dict['name'] + " knows english"
    else :
        return person_dict['name'] + " does not know english"

@app.route('/jsonfile',methods=['GET'])
def readfromjsonfile():
    with open('data/person.json') as f:
        persondict=json.load(f)
        if "english" in persondict['languages']:
            response=json.dumps(persondict)
            return response
        else:
            return "does not have english"

@app.route('/testjsonfile')
def testjsonfile():
    with open('data/person.json') as f:
        datadict=json.load(f)
        return json.dumps(datadict['languages'])

app.run(host='0.0.0.0', port=3000)