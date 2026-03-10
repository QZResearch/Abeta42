#!/bin/bash



for temp in {0..13}
do

if [ -f cpptraj_dssp.in ]; 
then
	rm cpptraj_dssp.in
fi
	
echo "Porcessing Temp ${temp}/13 ..."

cat > cpptraj_dssp.in <<-EOF
parm ../../../../abeta_linear.parm7
EOF

for i in {13..20}
do
	echo "trajin ../T${i}/allT/remd.nc.${temp}" >> cpptraj_dssp.in
done

echo "secstruct :1-42 out dssp.${temp}.dat sumout dssp_summary.${temp}.dat" >> cpptraj_dssp.in


cpptraj -i cpptraj_dssp.in

rm cpptraj_dssp.in

done


