import face_recognition
import recognition

collection = []
total1 = 0.0
total2 = 0.0

def test (data, k):
    global total1
    global total2
    global collection
    for person in data:
        file_name = "tests/" + person + ".jpg"
        picture = face_recognition.load_image_file(file_name)
        faces = face_recognition.face_encodings(picture)
        if (len(faces) > 0):
            encoding = faces[0]
            foto = {"encode" : encoding, "person" : person}
            res1, pres1 = recognition.knn_search_e(foto, collection, k)
            res2, pres2 = recognition.knn_search_m(foto, collection, k)
            print("Pres1: ", pres1, " - Pres2: ", pres2)
            total1 += pres1
            total2 += pres2
        else:
            print(" - ", person)

data2 = {'Valdas_Adamkus', 
'Scott_McNealy', 
'Adrian_Nastase'
}
data4 = {'Tony_Bennett', 
'Naoto_Kan', 
'David_Hyde_Pierce'
}
data8 = {'Antonio_Palocci', 
'Juan_Pablo_Montoya', 
'Justin_Timberlake'
}
data16 = {'Tommy_Franks', 
'Halle_Berry', 
'Trent_Lott'
}


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
        total+=1


print("K = 2")
test(data2, 2)
print("K = 4")
test(data4, 4)
print("K = 8")
test(data8, 8)
print("K = 16")
test(data16, 16)
print("Average pres1: ", total1/12)
print("Average pres2: ", total2/12)
print(total)