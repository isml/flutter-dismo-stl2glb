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

    path_to_stl = "model1.stl"
    out_path = "model1.glb"
    if len(sys.argv) > 3:
      is_binary = True
    else:
      is_binary = False

    if out_path.lower().endswith(".glb"):
      print("Use binary mode since output file has glb extension")
      is_binary = True
    else:
      if is_binary:
        print("output file should have glb extension but not %s", out_path)

    if not os.path.exists(path_to_stl):
      print("stl file does not exists %s" % path_to_stl)

    if not is_binary:
      if not os.path.isdir(out_path):
        os.mkdir(out_path)

    stl_to_gltf(path_to_stl, out_path, is_binary)
    # firebasedeneme start
    # firebasedeneme start
    
    


    # firebasedeneme finish

    # firebasedeneme finish




    resPuan = str(5)

    return jsonify({"response": "1"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", )
