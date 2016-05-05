import pickle
mathUnpickleFile = open('algebra.txt', 'r')
algebraUnPickleList = pickle.load(mathUnpickleFile)
mathUnpickleFile.close()
for topic in algebraUnPickleList:
    print topic
