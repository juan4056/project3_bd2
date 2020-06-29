import face_recognition
import heapq

def euclidian_distance (encode1, encode2):
    power = pow(encode1 - encode2, 2)
    res = 0
    for p in power:
        res += p
    return pow(res, 1/2)

def manhattan_distance (encode1, encode2):
    power = abs(encode1 - encode2)
    res = 0
    for p in power:
        res += p
    return res

def knn_search_e (foto, collection, k):
    result = []
    i = 1
    for item in collection:
        dis = euclidian_distance (foto["encode"], item["encode"])
        heapq.heappush (result, (dis, item["person"]))
        i+=1
    
    result = [heapq.heappop(result) for i in range(k)]

    cont = 0
    for item in result:
        if item[1] == foto["person"]:
            cont += 1

    return result, cont/len(result)

def knn_search_m (foto, collection, k):
    result = []
    i = 1
    for item in collection:
        dis = manhattan_distance (foto["encode"], item["encode"])
        heapq.heappush (result, (dis, item["person"]))
        i+=1
    
    result = [heapq.heappop(result) for i in range(k)]

    cont = 0
    for item in result:
        if item[1] == foto["person"]:
            cont += 1

    return result, cont/len(result)

