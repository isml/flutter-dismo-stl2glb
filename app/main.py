from flask import Flask
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



  
    

    



    resPuan = str(5)

    return jsonify({"response": "1"})




if __name__ == "__main__":
    app.run(host="0.0.0.0", )
