from flask import Flask 
app = Flask(__name__)
print("Hello")
from app import routes