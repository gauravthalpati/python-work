# This is a PoC for Flask API
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
# https://codeloop.org/how-to-build-rest-api-with-sqlalchemy-marshmallow/

# https://www.youtube.com/watch?v=s_ht4AKnWZg&t=241s
# https://www.youtube.com/watch?v=EAokwpPMVdc&t=2018s
# https://www.youtube.com/watch?v=y_Wc2qwVKbg&t=765s
# https://www.youtube.com/watch?v=lllB-78pkDQ


# Output to be displayed at
# http://127.0.0.1:5000/
# OR
# curl -X GET http://127.0.0.1:5000/
# OR
# Use Postman - easiest of all


import requests
import json
import flask
import flask_restx
import flask_sqlalchemy
import flask_marshmallow
import marshmallow_sqlalchemy
import os
import jsonify

from flask import Flask,request,jsonify
from flask_restx import Resource,Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
api = Api(app)

# Set base dir for SQL Lite database
basedir = os.path.abspath(os.path.dirname(__file__))
#C:\Users\gaura\PycharmProjects\pythonProject

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'demo1.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize DB
db = SQLAlchemy(app)

#Initialiaze marshmallow
ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Constructor
    def __init__(self,username,email):
        self.username = username
        self.email = email

# Create database
#db.create_all()

# Insert Records in SQL Lite Database
# admin = User(username='admin2', email='admin2@example.com')
# guest = User(username='guest2', email='guest2@example.com')

# # Insert Sample Records
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

# To see the data - not working :(
#User.query.all()

# User Schema
class UserSchema (ma.Schema):
    class Meta:
        fields = ('id','username','email')

# Initialise Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Get all data from table - WORKING

# @app.route('/User')
# def get_users():
#     all_users = User.query.all()
#     result = users_schema.dump(all_users)
#     return jsonify(result)

# # Get single data from table -- WORKING
# @app.route('/User/<int:id>', methods=['GET'])
# def get_user(id):
#     single_user = User.query.get(id)
#     return user_schema.jsonify(single_user)


# # # Check if flask is working
# @app.route('/')
# def index():
#     return 'Flask is working'


# # Check if flask is working
# @app.route('/',methods=['GET'])
# def get():
#      return jsonify({'msg' : 'Flask is working' })

# #For Swagger API - WORKING
# @api.route("/data")
# class My_Data(Resource):
#     def get(self):
#         with open('D:\Work\Training Stuff\python-proj\data-files\m1.json') as json_file:
#             data = json.load(json_file)
#             return data

# api.add_resource(My_Data, "/MakeName")

#Swagger API with all data - WORKING
@api.route('/data')
class My_Data(Resource):
     def get(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)


# Swagger API with single data - WORKING
@api.route('/User/<int:id>', methods=['GET'])
class My_Data(Resource):
    def get(self,id):
        single_user = User.query.get(id)
        return user_schema.jsonify(single_user)

# Swagger API with display from json file - WORKING
# @api.route("/data")
# class My_Data(Resource):
#     def get(self):
#         with open('D:\Work\Training Stuff\python-proj\data-files\m1.json') as json_file:
#             data = json.load(json_file)
#             return data




# Run server
if __name__ == "__main__":
  app.run(debug=True)
