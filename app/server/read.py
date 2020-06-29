
file = open('encodings.bin', 'r')

datos = file.read().split('\n')
for d in datos:
    if len(d) > 0:
        encode = d.split(',')
        name = encode[len(encode) - 1]
        encode.remove(name)
        encode = list(map(float, encode))
        print(name, ": ", encode)