import ppn
import utils
from matplotlib.pylab import *
symbs=utils.symbol_list('lines2')
x=ppn.xtime('.')
specs=['PROT','HE  4','C  12','N  14','O  16','NE 20','MG 24','SI 28']
abus=[]
for spec in specs:
    abu=x.get(spec)
    abus.append(abu)
time=x.get('time')
close(10);figure(10)
for i in range(len(specs)):
    plot(time,log10(abus[i]),symbs[i],label=specs[i])
ylim(-5,0.2)
legend(loc=2)
xlabel('$t / \mathrm{yrs}$')
ylabel('$\log X \mathrm{[mass fraction]}$')
savefig('abu_evolution.png')
