#dictonaries methods in python
ep={234:45,123:45,456:78,853:98}
ep2={257:67,543:87,325:56}

ep.update(ep2)
print(ep)

# ep.pop(123)  remove given key pair
# print(ep)

# ep.popitem()  remove last key value

del ep
print(ep)