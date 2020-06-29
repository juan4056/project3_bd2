from rtree import index

p = index.Property()
p.dimension = 128
p.dat_extension = 'data'
p.idx_extension = 'index'
idx = index.Index('encode_index',properties=p, interleaved = True)

file = open('encodings.bin', 'r')

datos = file.read().split('\n')

i = 0

encode_temp = []

for d in datos:
    if len(d) > 0:
        encode = d.split(',')
        name = encode[len(encode) - 1]
        encode.remove(name)
        encode = list(map(float, encode))
        user = {"person": name, "encode": encode}
        idx.insert(i, tuple(encode), obj=name)
        i+= 1
        if i == 15:
            encode_temp = encode

hits = list(idx.nearest(tuple(encode_temp), 25, objects = True))
for h in hits:
    print(h.id)
    print(h.object)



    
