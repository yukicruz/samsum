from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to something more secure

login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user for testing
class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username == "trial_user":
        user = User()
        user.id = username
        return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'trial_user' and request.form['password'] == 'test_password':
            user = User()
            user.id = 'trial_user'
            login_user(user)
            return redirect(url_for('chat'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
