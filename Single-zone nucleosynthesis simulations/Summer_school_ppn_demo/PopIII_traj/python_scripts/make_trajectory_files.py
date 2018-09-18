# a little script to make trajectory and staring initial abundance files
# from mppnp to be used in ppn, use nsource=1 (link trajectory filename
# to trajectory.input) and iabuini=12 (put massf file into variable
# ini_filename)


import ascii_table
import mppnp as mp

s=mp.se('/rpod2/fherwig/M/Set_1.2_simple_atm/M2.00Z0.020/M2.00Z0.020')

r,rho,T,age=s.trajectory(1436,1450,1,0.01,age_in_sec=True)
T8=array(T)/1.e8
data=[age,T8,rho]
ascii_table.writeTraj(filename='trajectory_M2.0Z0.02_1436-1450_m0.01.input',data=data)

# sp=mp.se('/rpod2/fherwig/PPN/RUNS/M2.00Z1.0e-02_neut-test/H5_out')
# sp.abund_at_masscoorinate(1435,0.01)

