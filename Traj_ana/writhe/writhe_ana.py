#!/bin/python

import mdtraj as md
import matplotlib.pyplot as plt
import numpy as np

from writhe_tools.utils import reindex_list
from writhe_tools.md_tools import get_residues # convenience function for getting residue names from mdtraj.Trajectory

from writhe_tools.utils import Timer


traj_files = ['../T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]

traj_list = [md.load_netcdf(f, top='../../../../abeta_linear.parm7') for f in traj_files]

traj = md.join(traj_list)
xyz = traj.atom_slice(traj.top.select('name CA')).xyz
print('Total frames: {}'.format(len(xyz)))
residues = get_residues(traj)

from writhe_tools.writhe import Writhe

writhe = Writhe(xyz=xyz)

with Timer():
    for length in range(2,6):
        writhe.compute_writhe(length=length, multi_proc=True, cpu_method='ray',speed_test=False, store_results=True)
        writhe.save(path="./results",dscr="wt_chirality_298K")




