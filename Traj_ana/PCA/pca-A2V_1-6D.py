#!/bin/python

import numpy as np
import mdtraj as md
from sklearn.decomposition import PCA
import joblib

def genDihed(trajs,top):
	traj_list = [md.load_netcdf(f, top=top) for f in trajs]
	traj = md.join(traj_list)
	atom_indices = traj.topology.select("protein and name CA")
	traj.superpose(traj, frame=0, atom_indices=atom_indices)
	phi_idx, phi = md.compute_phi(traj)
	psi_idx, psi = md.compute_psi(traj)
	# concatenate all the angles computed
	angles = np.concatenate(
		[phi, psi],
		axis=1
	)
	# convert the degree into rad
	X = np.concatenate(
		[np.sin(angles), np.cos(angles)],
		axis=1)
	return X

# load A2V 1-6D trajectories
traj_a2vd = ['../A2V_1-6D/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
top_a2vd  = '../A2V_1-6D/abeta_linear.parm7'
X_a2vd    = genDihed(traj_a2vd, top_a2vd)


pca = joblib.load('dihedral_pca_model.pkl')

X_a2vd_new = pca.transform(X_a2vd)
np.save('pca_coord_a2vd.npy', X_a2vd_new)
