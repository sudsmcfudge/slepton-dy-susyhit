#!/bin/bash

inputparamfile="input.dat"
rundir="../../susyhit-1.3"
template="../suspect2_lha.template"
suspectfile=$rundir/suspect2_lha.in
susyhitfile=$rundir/susyhit_slha.out

outfile="msl500_tb3_ma_2000.pkl"

rm $outfile

N=`head -n 1 $inputparamfile`

M1_list=(`gawk 'NR>1 {print $1}' $inputparamfile`)
M2_list=(`gawk 'NR>1 {print $2}' $inputparamfile`)
At_list=(`gawk 'NR>1 {print $3}' $inputparamfile`)
mu_list=(`gawk 'NR>1 {print $4}' $inputparamfile`)
ma_list=(`gawk 'NR>1 {print $5}' $inputparamfile`)
tb_list=(`gawk 'NR>1 {print $6}' $inputparamfile`)
mL_list=(`gawk 'NR>1 {print $7}' $inputparamfile`)
mR_list=(`gawk 'NR>1 {print $8}' $inputparamfile`)

len=${#mL_list[@]}
len=`expr $len - 1`

echo $N > $outfile

for i in `seq 0 $len`; do
    mL=${mL_list[i]}
    mR=${mR_list[i]}
    M1=${M1_list[i]}
    M2=${M2_list[i]}
    mu=${mu_list[i]}
    tanb=${tb_list[i]}
    ma=${ma_list[i]}

    echo $mL $mR $M1 $M2 $mu

    sed -e "s/__M_L__/$mL/" -e "s/__M_R__/$mR/" -e "s/__M_1__/$M1/" -e "s/__M_2__/$M2/" -e "s/__tb__/$tanb/" -e "s/__mu__/$mu/" -e "s/__ma__/$ma/" $template > $suspectfile
    
    pushd $rundir
    ./run_noqcd
    #./run_noloop
    popd

    ../stripslep.py $rundir $outfile

done
