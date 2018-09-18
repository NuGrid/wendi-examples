#!/bin/bash
# this is a runscript for running ppn
# of machines; do not change anything in this file, instead before you 
# execute this script check the configuration parameters and comments 
# in config.sh
# PD, 141212

function check_okay {
        if [ $error -ne 0 ]
        then
             echo $fail_warning
	     exit 1
        fi
}

function check_info {
        if [ $error -ne 0 ]
        then
             echo $fail_warning
        fi
}

[ -f config.sh ] && source config.sh
error=$?
fail_warning="ERROR: no file config.sh. Run compile.sh script."
check_okay

# check if CODE is compiled with same parameter.inc as specified 
# in this RUN directory
CODE_DIR=$PPN_DIR/$FRAME/CODE
diff parameter.inc $CODE_DIR/parameter.inc
error=$?
fail_warning="WARNING: parameter.inc is not the same as in CODE directory. Need to recompile! Use compile.sh script."
check_okay

# check if PPN_DIR in Make.local is same as in this RUN directory
set -- `grep "PPN\s*=" $PPN_DIR/$FRAME/CODE/Make.local | grep -v "^\s*#"`
[[ `readlink -e $PPN_DIR` ==  *`echo $3`* ]]
error=$?
fail_warning="ERROR: PPN_DIR in this RUN dir and in CODE dir are not the same."
check_okay

# check if NPDATA is setup correctly
rm -f ../NPDATA
error=$?
fail_warning="INFO: can not remove link ../NPDATA - it may not exist."
check_info
PPN_DIR=`readlink -e $PPN_DIR`
ln -s $PPN_DIR/$PHYSICS/NPDATA ..
error=$?; fail_warning="WARNING: can not link NPDATA"; check_okay

NPDATA_DIR=`readlink ../NPDATA`
echo "Using NPDATA in $NPDATA_DIR"

# launching run
echo "Starting run with ppn executable "$EXE 
nice -n $NVAL ./$EXE |tee fort.6

python plot_abu_evolution.py
python abu_chart.py
python plot_isoabund.py

echo Finished making *.png plots. Compare with master_results/*png.

