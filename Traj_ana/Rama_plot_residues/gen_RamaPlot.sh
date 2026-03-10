#!/bin/bash

if [ -f cpptraj_rama.in ];
then
	rm cpptraj_rama.in
fi

cat > cpptraj_rama.in <<-EOF

parm ../../../../abeta_linear.parm7
trajin ../T1[3-9]/allT/remd.nc.1
trajin ../T20/allT/remd.nc.1

EOF


for i in {2..41}
do

let pre=`expr $i - 1`
let nxt=`expr $i + 1`

echo "dihedral phi${i} :${pre}@C :${i}@N :${i}@CA :${i}@C out phi${i}.dat" >>cpptraj_rama.in
echo "dihedral psi${i} :${i}@N :${i}@CA :${i}@C :${nxt}@N out psi${i}.dat" >>cpptraj_rama.in
echo " " >> cpptraj_rama.in

done

echo "run" >> cpptraj_rama.in

cpptraj -i cpptraj_rama.in
