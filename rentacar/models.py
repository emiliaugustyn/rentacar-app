from datetime import datetime
from sqlalchemy.orm import relationship
from rentacar import *


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
