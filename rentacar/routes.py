from flask import render_template, url_for, flash, redirect, request
from rentacar.forms import RegistrationForm, LoginForm
from rentacar.models import *
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        client = Client(username=form.username.data.encode('utf-8'),
                        first_name=form.first_name.data.encode('utf-8'),
                        last_name=form.last_name.data.encode('utf-8'),
                        pesel=form.pesel.data.encode('utf-8'),
                        email=form.email.data.encode('utf-8'),
                        phone_number=form.phone_number.data.encode('utf-8'),
                        id_number=form.id_number.data.encode('utf-8'),
                        password=form.password.data.encode('utf-8')
                        )
        session.add(client)
        session.commit()
        flash('Submitted! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        client = session.query(Client).filter_by(email=form.email.data).first()
        if client and client.password == form.password.data:
            login_user(client, remember=true)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
