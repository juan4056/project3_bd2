from rtree import index

from flask import Flask
from flask import render_template 
from flask import request
from flask import jsonify
import json
from flask_cors import CORS
import face_recognition
import os

p = index.Property()
p.dimension = 128
p.dat_extension = 'data'
p.idx_extension = 'index'
idx = index.Index('rtree', properties=p, interleaved = True)

# instantiate the app
app = Flask(__name__)
#app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})





@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/build", methods=['GET'])
def build():
    global idx

    file = open('encodings2.bin', 'r')

    datos = file.read().split('\n')
    total = 0
    for d in datos:
        if len(d) > 0:
            encode = d.split(',')
            name = encode[len(encode) - 1]
            encode.remove(name)
            encode = list(map(float, encode))
            idx.insert(total, tuple(encode), obj=name)
            total += 1

    file.close()
    return jsonify({'status': 1})



@app.route("/upload", methods=['POST'])
def upload():

    global idx
    
    data = dict(request.files)['image']

    picture = face_recognition.load_image_file(data)
    faces = face_recognition.face_encodings(picture)
    results = []
    if (len(faces) > 0):
        encoding = faces[0]
        hits = list(idx.nearest(tuple(encoding), 5, objects = True))

        for h in hits:
            results.append(h.object)

    return jsonify({'status': 200, 'result': results})

if __name__=="__main__":
    app.run(debug=True)