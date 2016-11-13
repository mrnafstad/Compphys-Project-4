from matplotlib.pylab import *
from numpy import *

filenames = ["meanvalues_40.00.txt", "meanvalues_60.00.txt", "meanvalues_100.00.txt", "meanvalues_140.00.txt"]

arr = False
color = iter(cm.rainbow(linspace(0, 1, len(filenames))))
temp = []
E = []
for file in filenames:
	f = open(file)
	
	if arr:
		i=0
		for line in f:
			words = line.split()

			E[i] = float(words[1])
			
			i+=1
	else:
		for line in f:
			words = line.split()
			temp.append(float(words[0]))
			E.append(float(words[1]))
			arr = True

	temp = array(temp); E = array(E); print len(E)

	plot(temp, E, c = next(color))
	hold("On")
	xlabel("T")
	ylabel(r"$<E>$")
legend(["40x40", "60x60", "100x100", "140x140"], loc="upper left")
show()

color = iter(cm.rainbow(linspace(0, 1, len(filenames))))
M = []
arr=False
for file in filenames:
	f = open(file)
	
	if arr:
		i=0
		for line in f:
			words = line.split()

			M[i] = float(words[2])
			
			i+=1
	else:
		for line in f:
			words = line.split()
			M.append(float(words[2]))
			arr = True

	M = array(M)

	plot(temp, M, c = next(color))
	hold("On")
	xlabel("T")
	ylabel(r"$<|M|>$")
legend(["40x40", "60x60", "100x100", "140x140"], loc="upper left")
show()


color = iter(cm.rainbow(linspace(0, 1, len(filenames))))
Cv = []
arr=False
for file in filenames:
	f = open(file)
	
	if arr:
		i=0
		for line in f:
			words = line.split()

			Cv[i] = float(words[3])
			
			i+=1
	else:
		for line in f:
			words = line.split()
			Cv.append(float(words[3]))
			arr = True

	Cv = array(Cv)

	plot(temp, Cv, c = next(color))
	hold("On")
	xlabel("T")
	ylabel(r"$C_V$")
legend(["40x40", "60x60", "100x100", "140x140"], loc="upper left")
show()


color = iter(cm.rainbow(linspace(0, 1, len(filenames))))
chi = []
arr=False
for file in filenames:
	f = open(file)
	
	if arr:
		i=0
		for line in f:
			words = line.split()

			chi[i] = float(words[4])
			
			i+=1
	else:
		for line in f:
			words = line.split()

			chi.append(float(words[4]))
			arr = True

	chi = array(chi)

	plot(temp, chi, c = next(color))
	hold("On")
	xlabel("T")
	ylabel(r"$\chi$")
legend(["40x40", "60x60", "100x100", "140x140"], loc="upper left")
show()