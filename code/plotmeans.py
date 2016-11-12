from matplotlib.pylab import *
from numpy import *

f = open("meanvalues_40.00.txt")

temp = []; E = []; M = []; Cv = []; Suscept = []

for line in f:
	words = line.split()
	temp.append(float(words[0]))
	E.append(float(words[1]))
	M.append(float(words[2]))
	Cv.append(float(words[3]))
	Suscept.append(float(words[4]))

temp = array(temp); E = array(E); M = array(M); Cv = array(Cv); Suscept = array(Suscept)

plot(temp, E)
xlabel("T")
ylabel(r"$<E>$")
show()

plot(temp, M)
xlabel("T")
ylabel(r"$<|M|>$")
show()

plot(temp, Cv)
xlabel("T")
ylabel(r"$C_V$")
show()

plot(temp, Suscept)
xlabel("T")
ylabel(r"$\chi$")
show()