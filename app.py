from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy imcmport SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Unicode, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
# jp emilke
app = Flask(__name__)
app.config['SECRET_KEY'] = '873641a1fe30ec2a559e69afda22fe8b'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/rentacar'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

engine = create_engine('mysql+mysqlconnector://root:''@localhost:3306/rentacar')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    worker_id = Column(Integer, ForeignKey('workers.id'), nullable=False)
    start_date = Column(DateTime, nullable=True, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True, default=datetime.utcnow)
    total_price = Column(Integer, nullable=True)


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    username = Column(Unicode(20), nullable=False, unique=True)
    password = Column(Unicode(20), nullable=False, unique=True)
    first_name = Column(Unicode(25), nullable=True)
    last_name = Column(Unicode(25), nullable=True)
    pesel = Column(Unicode(11), nullable=False)
    email = Column(Unicode(50), nullable=False, unique=True)
    phone_number = Column(Unicode(9), nullable=True)
    id_number = Column(Unicode(9), nullable=False)
    reservations = relationship('Reservation', backref='client_rsrv', primaryjoin="Client.id==Reservation.client_id")

    def __repr__(self):
        return f"Client('{self.id}','{self.username}')"


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    make = Column(Unicode(25), nullable=True)
    model = Column(Unicode(25), nullable=True)
    registration_number = Column(Unicode(25), nullable=False)
    horse_power = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    price_day = Column(Integer, nullable=True)
    in_stock = Column(Boolean, nullable=True)
    reservations = relationship('Reservation', backref='car_rsrv', primaryjoin="Car.id==Reservation.car_id")

    def __repr__(self):
        return f"Car('{self.id}''{self.make}','{self.model}', '{self.registration_number}')"


class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    username = Column(Unicode(20), nullable=False, unique=True)
    password = Column(Unicode(20), nullable=False, unique=True)
    first_name = Column(Unicode(25), nullable=True)
    last_name = Column(Unicode(25), nullable=True)
    email = Column(Unicode(255), nullable=False, unique=True)
    reservations = relationship('Reservation', backref='worker_rsrv', primaryjoin="Worker.id==Reservation.worker_id")

    def __repr__(self):
        return f"Worker('{self.id}','{self.username}', '{self.password}')"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
