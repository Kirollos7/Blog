from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
main = Flask(__name__)

main.config['SECRET_KEY'] = '49781caeb0488ca837fac39f5213ec4b'

posts = [
    {
        'author': 'Kirollos Noshy',
        'title' : 'C++',
        'content' : 'Linkedlist , Stack , Queue',
        'date_posted': 'April 05, 2021', 
    }
    ,
    {
        'author': 'Mina Hany',
        'title' : 'Python',
        'content' : 'ERP System',
        'date_posted': 'Jan 05, 2021', 
    }
]

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', posts = posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login' , form= form)

@main.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    else:
        pass
    return render_template('register.html', title='Register', form= form)

if __name__ == '__main__':
    main.run(debug=True)
    
    
    
    


'''
this command for run flask server inside v-env
$export FLASK_APP=main.py --> in Linux and Mac
$set FLASK_APP=main.py    --> in Windows
    ----------------------------------------
turn on Debug mode = export FLASK_DEBUG=1
'''
# -- flask run --> flask run --host=0.0.0.0 --port=80
# Forms in lask using WTF
# pip3 install flask-wtf