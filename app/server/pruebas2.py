import face_recognition
from rtree import index
import recognition
import time


def test (person, k, n):
    collection = []

    file = open('encodings.bin', 'r')
    datos = file.read().split('\n')

    total = 0
    for d in datos:
        if len(d) > 0:
            encode = d.split(',')
            name = encode[len(encode) - 1]
            encode.remove(name)
            encode = list(map(float, encode))
            user = {"person": name, "encode": encode}
            collection.append(user)
            total += 1
            if total == n:
                break

    file_name = "tests/" + person + ".jpg"
    picture = face_recognition.load_image_file(file_name)
    faces = face_recognition.face_encodings(picture)

    stime = time.time()
    if (len(faces) > 0):
        encoding = faces[0]
        foto = {"encode" : encoding, "person" : person}
        res1, pres1 = recognition.knn_search_e(foto, collection, k)
        print("Test: ", n, " - Pres: ", pres1)
    else:
        print(" - ", person)

    etime = time.time()
    print("----%s seconds\n" % (etime - stime))
    file.close()

def test2 (person, k, n):
    print("\nTest: ", n)
    p = index.Property()
    p.dimension = 128
    idx = index.Index(properties=p, interleaved = True)

    file = open('encodings.bin', 'r')

    datos = file.read().split('\n')

    total = 0

    stime = time.time()
    for d in datos:
        if len(d) > 0:
            encode = d.split(',')
            name = encode[len(encode) - 1]
            encode.remove(name)
            encode = list(map(float, encode))
            user = {"person": name, "encode": encode}
            idx.insert(total, tuple(encode), obj=name)
            
            total += 1
            if total == n:
                break
    
    etime = time.time()

    print("Time to build R-tree: %s seconds" % (etime - stime))

    file_name = "tests/" + person + ".jpg"
    picture = face_recognition.load_image_file(file_name)
    faces = face_recognition.face_encodings(picture)
    stime = time.time()
    if (len(faces) > 0):
        encoding = faces[0]
        hits = list(idx.nearest(tuple(encoding), k, objects = True))

    etime = time.time()
    
    print("Time to search knn: %s seconds" % (etime - stime))
    file.close()

    new_pres = 0
    for h in hits:
        if h.object == person:
            new_pres+=1
    print("Pres: ", new_pres/k)

person_test = 'Tony_Bennett'

array_n = [100, 200, 400, 800, 1600, 3200, 6400, 9134]

print("Test for Knn-secuential with euclidian distance\n")
for n in array_n:
    test(person_test, 4, n)

print("Test for R-tree\n")
for n in array_n:
    test2(person_test, 4, n)