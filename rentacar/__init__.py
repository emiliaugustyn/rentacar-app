from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '873641a1fe30ec2a559e69afda22fe8b'

engine = create_engine('mysql+mysqlconnector://root:''@localhost:3306/rentacar')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from rentacar import routes
