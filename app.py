
from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def get_Health():
    return {"msg" : "Success"}, 200



