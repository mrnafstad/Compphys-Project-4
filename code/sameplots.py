from matplotlib.pylab import *
from numpy import *

filenames = ["T_1.00.txt", "T_2.40.txt", "T_random_1.00.txt", "T_random_2.40.txt"]

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
	xlabel("Monte Carlo cycles")
	ylabel(r"$<E>$ $[spin^{-1}]$")
legend(["T=1.00", "T=2.40", "T=1.00 random", "T=2.40 random"], loc="upper right")
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
	xlabel("Monte Carlo cycles")
	ylabel(r"$<|M|>$ $[spin^{-1}]$")
legend(["T=1.00", "T=2.40", "T=1.00 random", "T=2.40 random"], loc="lower right")
show()


color = iter(cm.rainbow(linspace(0, 1, len(filenames))))
A = []
arr=False
for file in filenames:
	f = open(file)
	
	if arr:
		i=0
		for line in f:
			words = line.split()

			A[i] = float(words[3])
			
			i+=1
	else:
		for line in f:
			words = line.split()
			A.append(float(words[3]))
			arr = True

	A = array(A)

	plot(temp, A, c = next(color))
	hold("On")
	xlabel("Monte Carlo cycles")
	ylabel("Accepted configurations")
legend(["T=1.00", "T=2.40", "T=1.00 random", "T=2.40 random"], loc="upper left")
show()
