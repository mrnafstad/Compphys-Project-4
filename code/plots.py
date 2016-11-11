from matplotlib.pylab import *
from numpy import *

f1 = open("T_1.00.txt")
f2 = open("T_2.40.txt")

mc = []; E1 = []; M1 = [] ; E2 = []; M2 = [];

for line in f1:
	words = line.split()
	mc.append(float(words[0]))
	E1.append(float(words[1]))
	M1.append(float(words[2]))

for line in f2:
	words = line.split()
	E2.append(float(words[1]))
	M2.append(float(words[2]))

mc = array(mc); E1 = array(E1); M1 = array(M1);
E2 = array(E2); M2 = array(M2);

plot(mc, E1)
hold('on')
plot(mc, E2)
legend(['T = 1.00', 'T = 2.40'])
xlabel(['Cycles'])
ylabel(['<E>'])
show()

plot(mc, M1)
hold('on')
plot(mc, M2)
legend(['T = 1.00', 'T = 2.40'])
xlabel(['Cycles'])
ylabel(['<|M|>'])
show()