#!/bin/python

import mdtraj as md
import numpy as np
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



# load trajectories
traj_wt = ['../linear_abeta_gb/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(13,21)]
top_wt  = '../linear_abeta_gb/abeta_linear.parm7'
X_wt = genDihed(traj_wt, top_wt)
print('WT.shape:', X_wt.shape)

traj_a2t = ['../A2T/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
top_a2t = '../A2T/abeta_linear.parm7'
X_a2t = genDihed(traj_a2t, top_a2t)
print('A2T.shape:', X_a2t.shape)

traj_a2v = ['../A2V/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(13,21)]
top_a2v = '../A2V/abeta_linear.parm7'
X_a2v = genDihed(traj_a2v, top_a2v)
print('A2V.shape:', X_a2v.shape)

traj_wtd = ['../WT1-6D/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
top_wtd = '../WT1-6D/abeta_linear.parm7'
X_wtd = genDihed(traj_wtd, top_wtd)
print('WTD.shape:', X_wtd.shape)

traj_a2t_beta = ['../A2T_Cbeta_chirality/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
top_a2t_beta  = '../A2T_Cbeta_chirality/abeta_linear.parm7'
X_a2t_beta = genDihed(traj_a2t_beta, top_a2t_beta)
print('A2T_beta.shape:', X_a2t_beta.shape)

X = np.concatenate([X_wt, X_a2t, X_a2v, X_wtd, X_a2t_beta], axis=0)
print('Total.shape:',X.shape)

pca = PCA(n_components=10)
X_pca = pca.fit_transform(X)

joblib.dump(pca, "dihedral_pca_model.pkl")

X_wt_new = pca.transform(X_wt)
np.save('pca_coord_wt.npy',X_wt_new)

X_a2v_new = pca.transform(X_a2v)
np.save('pca_coord_a2v.npy',X_a2v_new)

X_a2t_new = pca.transform(X_a2t)
np.save('pca_coord_a2t.npy',X_a2t_new)

X_wtd_new = pca.transform(X_wtd)
np.save('pca_coord_wtd.npy',X_wtd_new)

X_a2t_beta_new = pca.transform(X_a2t_beta)
np.save('pca_coord_a2t_beta.npy',X_a2t_beta_new)




#np.save("traj_pca_coord.npy",X_pca)
#np.save("pca_loadings.npy",pca.components_)
#np.save("pca_variance.npy",pca.explained_variance_ratio_)

