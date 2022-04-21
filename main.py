from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login-page.html')

@app.route('/sign-up')
def sign_up():
    return render_template('signup-page.html')

if __name__ == '__main__':
    app.run(debug=True)
