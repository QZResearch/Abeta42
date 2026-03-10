#!/bin/bash



for temp in {0..13}
do

if [ -f cpptraj_Rg.in ]; 
then
	rm cpptraj_Rg.in
fi
	
echo "Porcessing Temp ${temp}/13 ..."

cat > cpptraj_Rg.in <<-EOF
parm ../../../../abeta_linear.parm7
EOF

for i in {21..30}
do
	echo "trajin ../T${i}/allT/remd.nc.${temp}" >> cpptraj_Rg.in
done

echo "radgyr :1-42&@CA out rg.${temp}.dat mass" >> cpptraj_Rg.in


cpptraj -i cpptraj_Rg.in

rm cpptraj_Rg.in

done


