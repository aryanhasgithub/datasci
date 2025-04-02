import numpy as np
datatype =[("name","S15"),("age",int),("Height",float)]
arr = [("John", 25, 175.5), ("Alice", 30, 160.0), ("Bob", 22, 180)]
info = np.array(arr, dtype=datatype)

print(info)
print("sort by age")
sinfo1 = np.sort(info, order="age")
print(sinfo1)
print(info.dtype)
print(info.shape)
print(info[0][1])
print(info[1:3])
