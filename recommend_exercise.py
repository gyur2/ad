import pickle

fo = "test.dat"
data = []
fh = open(fo,"wb")
data = pickle.dump({3.0 : ['Bicycle ergometer : 50 Watt', 'Weight traning', 'Bowling', 'Volley vall', ' Frisbee'], 3.5 : ['Gymnastics', 'Golf(using carter)'], 3.8 : ['Walking(94m/m)'], 4.0 : ['Trot(95 ~ 100m/m)', 'Ping-Pong', 'Teakwondo', 'Aqua exercise'], 4.5 : ['badminton', 'Golf(Don\'t use carter)'], 4.8: ['ballet', 'Twistrun', 'Jazz dance', 'Tap dance'], 5.0 : ['Softball', 'Baseball', 'Trot(107m/m)'], 5.5 : ['Bicycle ergometer : 100 Watt']},fh)
fh.close()
