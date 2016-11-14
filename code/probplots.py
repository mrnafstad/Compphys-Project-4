from matplotlib.pylab import *
from numpy import *

filenames = ["Prob_2.40.txt"]#, "Prob_1.00.txt"]

arr = False
color = iter(cm.rainbow(linspace(0, 1, len(filenames))))
E = []
count = []
for file in filenames:
	f = open(file)
	
	if arr:
		i=0
		for line in f:
			words = line.split()
			E[i] = float(words[0])
			count[i] = float(words[1])
			
			i+=1
	else:
		for line in f:
			words = line.split()
			E.append(float(words[0]))
			count.append(float(words[1]))
			arr = True

	count = array(count); E = array(E)

	plot(E, count, "x", c = next(color))
	hold("On")
	xlabel("E")
	ylabel("P (E) ")
legend(["T=2.40"], loc="upper right")
show()