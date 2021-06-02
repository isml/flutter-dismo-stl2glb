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
    
     with open(path_to_stl, "rb") as f:
        f.seek(header_bytes)  # skip 80 bytes headers

        num_faces_bytes = f.read(unsigned_long_int_bytes)
        number_faces = struct.unpack("<I", num_faces_bytes)[0]

        # the vec3_bytes is for normal
        stl_assume_bytes = header_bytes + unsigned_long_int_bytes + number_faces * (
                    vec3_bytes * 3 + spacer_bytes + vec3_bytes)

        minx, maxx = [9999999, -9999999]
        miny, maxy = [9999999, -9999999]
        minz, maxz = [9999999, -9999999]

        vertices_length_counter = 0

        data = struct.unpack("<" + "12fH" * number_faces, f.read())
        len_data = len(data)

        
    #breakkkkkk
    gltf2 = gltf2 % (out_bin_uir,
                     # buffer
                     out_bin_bytelength,

                     # bufferViews[0]
                     indices_bytelength,

                     # bufferViews[1]
                     indices_bytelength,
                     vertices_bytelength,

                     # accessors[0]
                     out_number_indices,
                     out_number_vertices - 1,

                     # accessors[1]
                     out_number_vertices,
                     minx, miny, minz,
                     maxx, maxy, maxz
                     )

    glb_out = bytearray()
    if is_binary:
        gltf2 = gltf2.replace(" ", "")
        gltf2 = gltf2.replace("\n", "")

        scene = bytearray(gltf2.encode())

        scene_len = len(scene)
        padded_scene_len = (scene_len + 3) & ~3
        body_offset = padded_scene_len + 12 + 8

        file_len = body_offset + out_bin_bytelength + 8

        # 12-byte header
        glb_out.extend(struct.pack('<I', 0x46546C67))  # magic number for glTF
        glb_out.extend(struct.pack('<I', 2))
        glb_out.extend(struct.pack('<I', file_len))

        # chunk 0
        glb_out.extend(struct.pack('<I', padded_scene_len))
        glb_out.extend(struct.pack('<I', 0x4E4F534A))  # magic number for JSON
        glb_out.extend(scene)

        while len(glb_out) < body_offset:
            glb_out.extend(b' ')

        # chunk 1
        glb_out.extend(struct.pack('<I', out_bin_bytelength))
        glb_out.extend(struct.pack('<I', 0x004E4942))  # magin number for BIN

    # print('<%dI' % len(indices))
    # print(struct.pack('<%dI' % len(indices), *indices))
    glb_out.extend(struct.pack('<%dI' % len(indices), *indices))

    for i in range(indices_bytelength - unpadded_indices_bytelength):
        glb_out.extend(b' ')

    vertices = dict((v, k) for k, v in vertices.items())

    # glb_out.extend(struct.pack('f',
    # print([each_v for vertices[v_counter] for v_counter in range(number_vertices)]) # magin number for BIN
    vertices = [vertices[i] for i in range(number_vertices)]
    flatten = lambda l: [item for sublist in l for item in sublist]

    # for v_counter in :
    # v_3f = vertices[v_counter]
    # all_floats_in_vertices.append(v_3f[0])
    # all_floats_in_vertices.append(v_3f[1])
    # all_floats_in_vertices.append(v_3f[2])

    # for v_counter in range(number_vertices):
    glb_out.extend(struct.pack('%df' % number_vertices * 3, *flatten(vertices)))  # magin number for BIN

    # for v_counter in range(number_vertices):
    # glb_out.extend(struct.pack('3f', *vertices[v_counter])) # magin number for BIN

    # for (v_x, v_y, v_z), _ in sorted(vertices.items(), key=lambda x: x[1]):
    # glb_out.extend(struct.pack('3f', v_x, v_y, v_z)) # magin number for BIN
    # # glb_out.extend(struct.pack('f', v_y)) # magin number for BIN
    # # glb_out.extend(struct.pack('f', v_z)) # magin number for BIN

    with open(out_bin, "wb") as out:
        out.write(glb_out)

    if not is_binary:
        with open(out_gltf, "w") as out:
            out.write(gltf2)

   
    print("Done! Exported to %s" % out_path)

    

    

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
