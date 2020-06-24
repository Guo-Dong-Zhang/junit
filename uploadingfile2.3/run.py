import os
from datetime import timedelta

import readdata
import writedata
from flask import Flask, request, redirect, url_for, render_template ,session
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename


# UPLOAD_FOLDER = '/upload'
JAVAUPLOAD_FOLDER = '/upload/javalist'
JUNITUPLOAD_FOLDER = '/upload/junitlist'
# JAVAUPLOAD_FOLDER = '/Users/guodongzhang/Desktop/毕设/junitserver/filestore/javalist'
# JUNITUPLOAD_FOLDER = '/Users/guodongzhang/Desktop/毕设/junitserver/filestore/junitlist'
ALLOWED_EXTENSIONS = set(['txt', 'java'])

app = Flask(__name__)
app.secret_key = "Author: GuoDong"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)         #Time limit for session
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            stuid = request.form.get('usernameIN')
        except:
            stuid = None

        try:
            pwd = request.form.get('passwordIN')
        except:
            pwd = None

        try:
            stuidUP = request.form.get('usernameUP')
        except:
            stuidUP = None

        try:
            pwdUP = request.form.get('passwordUP')
        except:
            pwdUP = None

        try:
            pwdcheckUP = request.form.get('passwordcheckUP')
        except:
            pwdcheckUP = None

        #sign in check
        if stuid != None:
            dbid = readdata.getinfor(stuid)
            if stuid == dbid[0][0] and pwd == dbid[0][1]:
                session['logstamp'] = stuid
                print(type(stuid),stuid)
                return redirect(url_for('upload_file'))
        #sign up check
        if  pwdcheckUP != None and pwdUP != None and stuidUP !=None:
            if pwdcheckUP == pwdUP:
                writedata.dbwrite(stuidUP,pwdUP)

    return render_template("login.html")

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if session.get("logstamp") !=None:
        if request.method == 'POST':
            try:
                javafile = request.files['javafile']
            except:
                javafile = None
            try:
                junitfile = request.files['junitfile']
            except:
                junitfile = None

            if javafile and allowed_file(javafile.filename):
                filename = secure_filename(javafile.filename)
                # javafile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                javadirid = session.get('logstamp')
                os.system("mkdir -p "+JAVAUPLOAD_FOLDER+'/'+javadirid)
                JAVAUPLOAD_FOLDER_id = JAVAUPLOAD_FOLDER+'/'+javadirid                      #Student id will be added here
                javafile.save(os.path.join(JAVAUPLOAD_FOLDER_id, filename))
                return redirect(url_for('upload_success', filename=filename))

            if junitfile and allowed_file(junitfile.filename):
                filename = secure_filename(junitfile.filename)
                junitdirid = session.get('logstamp')
                os.system("mkdir -p "+JUNITUPLOAD_FOLDER + '/' + junitdirid)
                JUNITUPLOAD_FOLDER_id = JUNITUPLOAD_FOLDER + '/' + junitdirid                  #Student id will be added here
                junitfile.save(os.path.join(JUNITUPLOAD_FOLDER_id, filename))
                return redirect(url_for('upload_success', filename=filename))
        return render_template("uploadpage.html")
    else:
        return redirect(url_for('login'))


@app.route('/upload_success')
def upload_success():
    if session.get("logstamp") !=None:
        return render_template("confirmpage.html")
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)