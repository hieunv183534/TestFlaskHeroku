from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./a.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fsiconnectpynest-default-rtdb.asia-southeast1.firebasedatabase.app'
})

ref = db.reference('changeData/count')

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(ref.get())
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()