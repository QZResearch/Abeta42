#!/bin/bash

for i in {1..20}
do

#1 generate trajectories

	mkdir T${i}/allT
cat > T${i}/allT/extract_T_traj.x <<-EOF1

#!/bin/bash

mpirun -np 28 cpptraj.MPI ../../../../../abeta_linear.parm7 <<EOF
ensemblesize 14
ensemble ../../../remd${i}.mdcrd.001
trajout remd.nc
go
EOF

EOF1

#1-1 perform traj gen
(cd T${i}/allT; bash extract_T_traj.x)


done
