#!/bin/bash

for i in {1..30}
do

####bypass the process of generating trajectory at specified Temp
####1 generate trajectories
###
###	mkdir T${i}
###cat > T${i}/extract_T_traj.x <<-EOF1
###
####!/bin/bash
###
###cpptraj ../../../../abeta_linear.parm7 <<EOF
###trajin ../../remd${i}.mdcrd.001 remdtraj remdtrajtemp 287.00
###trajout remd.287K.mdcrd nobox
###
###go
###EOF
###
###EOF1

#2 generate script for analysis
mkdir T${i}/dssp
mkdir T${i}/Rg

cat > T${i}/dssp/cpptraj_dssp.in <<-EOF2
parm ../../../../../abeta_linear.parm7
trajin ../allT/remd.nc.1

secstruct :1-42 out dssp.gnu sumout dssp_summary.dat
EOF2

cat > T${i}/Rg/cpptraj_rg.in <<-EOF3
parm ../../../../../abeta_linear.parm7
trajin ../allT/remd.nc.1

radgyr :1-42&@CA out rg.dat mass
EOF3

##1-1 perform traj gen
##(cd T${i}; bash extract_T_traj.x)
#2-1 analysis dssp
(cd T${i}/dssp; cpptraj -i cpptraj_dssp.in)
#2-2 analysis rg
(cd T${i}/Rg; cpptraj -i cpptraj_rg.in)

done
