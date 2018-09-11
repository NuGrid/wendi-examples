### Running a new ppn problem - follow these steps

(This is a quickstart guide. For more details see the [wiki](https://github.com/NuGrid/NuPPN/wiki))

1. Set up the `Make.local` file in the `frames/ppn/CODE` directory. The
   templates in the `CODE/MAKE_LOCAL` directory are a good starting point. Consult the `README.md` in `frames/ppn/CODE`.
2. Make a copy of the RUN_TEMPLATE: `cp -rf frames/ppn/RUN_TEMPLATE /scratch/my_id/my_runs/RUN1` where you replace `my_id`  and `my_runs` with the appropriate values.
3. Go to your new run directory and compile the code: 
	* set the `PCD` variable in `Makefile`, do not use `~` that bash understands but make will not
	* `make distclean`
	* `make`
4. Prepare your input files. The frame, physics package and solver each have their own input file that together define the problem: 
	* `ppn_frame.input` - everything related to the I/O, data handling etc
	* `ppn_physics.input` - determine nuclear physics input
	* `ppn_solver.input` - specify input parameters related to the numerical solver
5. Execute the code: `./ppn.exe`

### Plotting

* Use the ppn module from the [NuGridPy](https://github.com/NuGrid/NuGridPy) repo. See documenation there for how to install and use. 
* You will find some examples in the `*.py` files as well as an example notebook in the `notebook` folder.
