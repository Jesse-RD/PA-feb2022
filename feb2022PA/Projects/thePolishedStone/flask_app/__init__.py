from flask import Flask

app = Flask(__name__)



app.secret_key = "arbitrary_secret_key_here"
