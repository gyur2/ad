import pickle
filename = "met.dat"
fh = open(filename,"wb")
pickle.dump({6.0:["weight training","baketball"],6.5:["aerobics"],7.0:["jogging","soccer","tennis","skate","ski"],7.5:["hiking(carry a bag(1~2kg))"],8.0:["running","cycling(20km/h)","freestyle swimming(45m/m)"],10.0:["judo","kickboxing","taekwondo"],11.0:["freestyle swimming(70m/m)","the butterfly"],15.0:["stair-climb"]},fh)
fh.close()


