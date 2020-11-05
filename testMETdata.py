name = "MET.dat"
import pickle
data = []
fh = open(name,"rb")
data = pickle.load(fh)
fh.close()
for i in data:
    print(i,data[i])

