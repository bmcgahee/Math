import pickle
algebraPickleList = ['variables', 'constants', 'equations', 'lines', 'polynomials', 'quadratics', 'inequalities']
pickleMathFile = open('algebra.txt', 'w')
pickle.dump(algebraPickleList, pickleMathFile)
pickleMathFile.close()
