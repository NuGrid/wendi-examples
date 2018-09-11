title_string='Title of this plot'
#title_string='T=200MK, X(H)=0.2, X(He4)=0.1, X(C12)=0.5, X(O16)=0.2'

import utils
import ppn
import matplotlib.pyplot as pl

symbs=utils.symbol_list('lines1')
symbs2=utils.symbol_list('list2')
symbs3=['o','d','>']
#plot_species=['PROT','C  12','C  13','N  13','O  14','N  14','O  18','F  18','NE 22']
plot_species=['PROT','C  12','C  13','N  13','O  14','O  15','N  14','N  15']
x=ppn.xtime('.')

i=0
for thing in plot_species:
    x.plot('t_y',thing,logy=True,logx=True,shape=symbs[i],legend=plot_species[i],show=False)
    i += 1

pl.legend(loc=3)
pl.ylim(-9,0)
pl.title(title_string)
pl.show()
pl.savefig('t-abu.pdf')


