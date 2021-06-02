from flask import Flask, jsonify,request
from __future__ import with_statement
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
 

    path_to_stl = "soner.stl"
    out_path = "soner.glb"

    is_binary =True

    gltf2 = '''
    {
      "scenes" : [
        {
          "nodes" : [ 0 ]
        }
      ],

      "nodes" : [
        {
          "mesh" : 0
        }
      ],

      "meshes" : [
        {
          "primitives" : [ {
            "attributes" : {
              "POSITION" : 1
            },
            "indices" : 0
          } ]
        }
      ],

      "buffers" : [
        {
          %s
          "byteLength" : %d
        }
      ],
      "bufferViews" : [
        {
          "buffer" : 0,
          "byteOffset" : 0,
          "byteLength" : %d,
          "target" : 34963
        },
        {
          "buffer" : 0,
          "byteOffset" : %d,
          "byteLength" : %d,
          "target" : 34962
        }
      ],
      "accessors" : [
        {
          "bufferView" : 0,
          "byteOffset" : 0,
          "componentType" : 5125,
          "count" : %d,
          "type" : "SCALAR",
          "max" : [ %d ],
          "min" : [ 0 ]
        },
        {
          "bufferView" : 1,
          "byteOffset" : 0,
          "componentType" : 5126,
          "count" : %d,
          "type" : "VEC3",
          "min" : [%f, %f, %f],
          "max" : [%f, %f, %f]
        }
      ],

      "asset" : {
        "version" : "2.0"
      }
    }
    '''

    header_bytes = 80
    unsigned_long_int_bytes = 4
    float_bytes = 4
    vec3_bytes = 4 * 3
    spacer_bytes = 2
    num_vertices_in_face = 3

    vertices = {}
    indices = []

    if not is_binary:
        out_bin = os.path.join(out_path, "out.bin")
        out_gltf = os.path.join(out_path, "out.gltf")
    else:
        out_bin = out_path

    unpack_face = struct.Struct("<12fH").unpack
    face_bytes = float_bytes * 12 + 2
    #sıkıntı burada başlıyor
    f = open("model1.stl") 
        
    
    

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
