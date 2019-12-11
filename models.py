from app import db
from datetime import datetime


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.Unicode(20), nullable=False, unique=True)
    password = db.Column(db.Unicode(20), nullable=False, unique=True)
    first_name = db.Column(db.Unicode(25), nullable=True)
    last_name = db.Column(db.Unicode(25), nullable=True)
    pesel = db.Column(db.Unicode(11), nullable=False)
    email = db.Column(db.Unicode(50), nullable=False, unique=True)
    phone_number = db.Column(db.Unicode(9), nullable=True)
    id_number = db.Column(db.Unicode(9), nullable=False)
    reservations = db.relationship('Reservation', backref='client_rsrv')


    def __repr__(self):
        return f"Client('{self.id}','{self.username}')"


class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    make = db.Column(db.Unicode(25), nullable=True)
    model = db.Column(db.Unicode(25), nullable=True)
    registration_number = db.Column(db.Unicode(25), nullable=False)
    horse_power = db.Column(db.Integer, nullable=True)
    passengers = db.Column(db.Integer, nullable=True)
    price_day = db.Column(db.Integer, nullable=True)
    in_stock = db.Column(db.Boolean, nullable=True)
    reservations = db.relationship('Reservation', backref='car_rsrv')
    

    def __repr__(self):
        return f"Car('{self.id}''{self.make}','{self.model}', '{self.registration_number}')"


class Worker(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.Unicode(20), nullable=False, unique=True)
    password = db.Column(db.Unicode(20), nullable=False, unique=True)
    first_name = db.Column(db.Unicode(25), nullable=True)
    last_name = db.Column(db.Unicode(25), nullable=True)
    email = db.Column(db.Unicode(255), nullable=False, unique=True)
    reservations = db.relationship('Reservations', backref='worker_rsrv')

    def __repr__(self):
        return f"Worker('{self.id}','{self.username}', '{self.password}')"


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'),  nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'),  nullable=False)
    worker_id = db.Column(db.Integer, db.ForeignKey('workers.id'),  nullable=False)
    start_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    total_price = db.Column(db.Integer, nullable=True)


