import pickle
fileCALORIE = 'dataCALORIE.dat'
def readcalorie():
    try:
        fo = open(fileCALORIE,'rb')
    except FileNotFoundError:
        print("There was no filename",fileCALORIE)
        return []
    resultcalorie = []
    try:
        #read result about CALORIE
        resultcalorie = pickle.load(fo)
    except:
        print("Empty result: ",fileCALORIE)
    else:
        print("Open result: ",fileCALORIE)
    fo.close()
    return resultcalorie
