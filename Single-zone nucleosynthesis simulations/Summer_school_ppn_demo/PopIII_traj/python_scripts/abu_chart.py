import ppn as pn
q=pn.abu_vector('.')
mq=q.get('mod')
sparse=10
#q.abu_chart(mq[start:enmd:sparse],plotaxis=[4,10,5,10],lbound=6,show=False)
q.abu_chart(mq[::sparse],plotaxis=[4,10,5,10],lbound=(-6,0),show=False)

