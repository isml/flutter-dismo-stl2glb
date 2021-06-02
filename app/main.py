from flask import Flask, jsonify,request
import requests
import struct
import os
import pyrebase
import sys

app = Flask(__name__);


@app.route("/bot", methods=["POST"])

def response():


    query = dict(request.form)['query']
    modelUrls = query.split("+linkdivider+")
    modelUrl = "https://firebasestorage.googleapis.com/v0/b/dismo-45c00.appspot.com/o/soner.stl?alt=media&token=e97408ce-0253-46c3-b755-72024bb4a1d2"
    r1 = requests.get(modelUrl, allow_redirects=True)
    open('model1.stl', 'wb').write(r1.content)
    modelPath = "deneme/model1.glb"
 

    binary_stl_path = "soner.stl"
    out_path = "model1.glb"
   
    print("Done! Exported to %s" % out_path)
    config = {
        "apiKey": "AIzaSyB1nw436MIG5oq53Bd7_xYanYwA1U7GnH0",
        "authDomain": "dismo-45c00.firebaseapp.com",
        "databaseURL": "https://dismo-45c00-default-rtdb.firebaseio.com/",
        "projectId": "dismo-45c00",
        "storageBucket": "dismo-45c00.appspot.com",
        "messagingSenderId": "400086979067",
        "appId": "1:400086979067:web:17d86fc6f7451d1bf63b5e",
        "measurementId": "G-9DVNRGDQFJ"
    }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    storage.child("model1.glb").put("model1.stl")
   
    




    resPuan = "5"

    return jsonify({"response": "1"})




if __name__ == "__main__":
    app.run(host="0.0.0.0", )
