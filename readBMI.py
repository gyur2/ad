import pickle
fileBmi = 'dataBMI.dat'
def readbmi():
    try:
        fo = open(fileBmi,'rb')
    except FileNotFoundError:
        print("There was no filename",fileBmi)
        return []
    resultbmi = []
    try:
        #read result about BMI
        resultbmi = pickle.load(fo)
    except:
        print("Empty result: ",fileBmi)
    else:
        print("Open result: ",fileBmi)
    fo.close()
    return resultbmi






