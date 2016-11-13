from matplotlib.pylab import *
from numpy import *

f1 = open("T_1.00.txt")
f2 = open("T_2.40.txt")
f3 = open("Prob_1.00.txt")

mc = []; E1 = []; M1 = []; A1 = []; E2 = []; M2 = []; A2 = []

En = []; Count = []; 

for line in f1:
	words = line.split()
	mc.append(float(words[0]))
	E1.append(float(words[1]))
	M1.append(float(words[2]))
	A1.append(float(words[3]))

for line in f2:
	words = line.split()
	E2.append(float(words[1]))
	M2.append(float(words[2]))
	A2.append(float(words[3]))

for line in f3:
	words = line.split()
	En.append(float(words[0]))
	Count.append(float(words[1]))

mc = array(mc); E1 = array(E1); M1 = array(M1); A1 = array(A1)
E2 = array(E2); M2 = array(M2); A2 = array(A2)

En, Count = zip(*sorted(zip(En, Count)))
En = array(En); Count = array(Count);

plot(mc, E1)
hold('on')
plot(mc, E2)
legend(['T = 1.00', 'T = 2.40'])
xlabel('Cycles')
ylabel(r"$<E>$")
show()

plot(mc, M1)
hold('on')
plot(mc, M2)
legend(['T = 1.00', 'T = 2.40'])
xlabel('Cycles')
ylabel(r'$<|M|>$')
show()

plot(mc, A1)
hold("On")
plot(mc, A2)
legend(["T = 1.0", "T = 2.4"])
xlabel("Cycles")
ylabel("# of accepted states")
show()

plot(En/20., Count/(10**5 - 2500))
xlabel('$E$')
ylabel('$P(E)$')
show()