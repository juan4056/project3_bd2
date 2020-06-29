import os
import face_recognition

files = [f for f in os.listdir('./lfw') ]
dic_ ={}
one = []
total = 0
fotos = []
fails = []
for f in files:
    images = [f2 for f2 in os.listdir('./lfw/' + f) ]
    for i in images:
        file_name = './lfw/' + f + '/' + i
        picture = face_recognition.load_image_file(file_name)
        faces = face_recognition.face_encodings(picture)
        if (len(faces) > 0):
            encoding = faces[0]
            fotos.append({"encode" : encoding, "person" : f})
            total += 1
        else:
            print(i, " - ", f)
            fails.append(i + "-" + f)
i = 1
file = open('encodings.bin', 'w')
for f in fotos:
    print(i, ": ",f['person'])
    for c in f['encode']:
        file.write(str(c) + ',')
    file.write(f['person'] + '\n')
    i+=1

print(fails)