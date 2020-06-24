import os
import readdata
from flask import Flask, request, redirect, url_for, render_template
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import sys

# UPLOAD_FOLDER = '/upload'
JAVAUPLOAD_FOLDER = '/upload/javalist'
JUNITUPLOAD_FOLDER = '/upload/junitlist'
# JAVAUPLOAD_FOLDER = '/Users/guodongzhang/Desktop/毕设/junitserver/filestore/javalist'
# JUNITUPLOAD_FOLDER = '/Users/guodongzhang/Desktop/毕设/junitserver/filestore/junitlist'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])

@app.route('/', methods=['GET', 'POST'])

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            stuid = request.form.get('userameIN')
        except:
            stuid = None
        try:
            pwd = request.form.get('passwordIN')
        except:
            stuid = None

        dbid = readdata.getinfor(stuid)
        if stuid == dbid[0][1] and pwd == dbid[0][2]:
            return redirect(url_for('upload_file'))
    return render_template("login.html")

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
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
            JAVAUPLOAD_FOLDER_id = JAVAUPLOAD_FOLDER+'/s1'                      #Student id will be added here
            javafile.save(os.path.join(JAVAUPLOAD_FOLDER_id, filename))
            return redirect(url_for('upload_success', filename=filename))

        if junitfile and allowed_file(junitfile.filename):
            filename = secure_filename(junitfile.filename)
            JUNITUPLOAD_FOLDER_id = JUNITUPLOAD_FOLDER + '/s1'                  #Student id will be added here
            junitfile.save(os.path.join(JUNITUPLOAD_FOLDER_id, filename))
            return redirect(url_for('upload_success', filename=filename))
    return render_template("uploadpage.html")


@app.route('/upload_success')
def upload_success():
    return render_template("confirmpage.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)