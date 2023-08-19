from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

#@app.route('/blog')
#def blog():
#    return render_template ('blog.html')

@app.route('/auth')
def auth_login():
    return render_template('Login.html')

@app.route('/signup')
def sign_up():
    return render_template('sign_up.html')

#@app.route('/project')
#def project():
#    return render_template ('Projects.html')

if __name__ == "__main__" :
  app.run(debug=True,)