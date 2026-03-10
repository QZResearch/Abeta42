#!/bin/python

import numpy as np
import pandas as pd
import mdtraj as md
from collections import Counter
from scipy.spatial.distance import pdist, squareform


def get_rep_str(pca_data,labels,trajs,desc):
    #labels_count = Counter(labels)
    for k,v in labels.items():
        #label_index = np.where(labels==k)[0]
        label_index = v
        print(label_index)
        pca_data_label = pca_data[label_index]
        distance = squareform(pdist(pca_data_label, metric='euclidean'))
        beta = 1
        index = np.exp(-beta*distance / distance.std()).sum(axis=1).argmax()
        print('label {} | distance.shape: {} | index of center: {}'.format(k,distance.shape[0], index))
        #distance = np.empty((v,v))
        trajs[index].save('{}_cluster_{}_{}.pdb'.format(desc,k,index))
        

# section of A2T
X_pca_a2t = np.load("../PCA_model_dihed/pca_coord_a2t.npy")
labels_a2t = np.load("../clustering2traj/dbscan_labels/a2t.npy",allow_pickle=True).item() 

traj_files = ['../A2T/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
traj_list = [md.load_netcdf(f, top='../A2T/abeta_linear.parm7') for f in traj_files]
traj_a2t = md.join(traj_list)
#print(labels)

get_rep_str(X_pca_a2t, labels_a2t, traj_a2t, 'a2t')

# section of A2V
X_pca_a2v = np.load("../PCA_model_dihed/pca_coord_a2v.npy")
labels_a2v = np.load("../clustering2traj/dbscan_labels/a2v.npy",allow_pickle=True).item() 

traj_files = ['../A2V/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(13,21)]
traj_list = [md.load_netcdf(f, top='../A2V/abeta_linear.parm7') for f in traj_files]
traj_a2v = md.join(traj_list)
#print(labels)

get_rep_str(X_pca_a2v, labels_a2v, traj_a2v, 'a2v')

# section of WT
X_pca_wt = np.load("../PCA_model_dihed/pca_coord_wt.npy")
labels_wt = np.load("../clustering2traj/dbscan_labels/wt.npy",allow_pickle=True).item() 

traj_files = ['../linear_abeta_gb/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(13,21)]
traj_list = [md.load_netcdf(f, top='../linear_abeta_gb/abeta_linear.parm7') for f in traj_files]
traj_wt = md.join(traj_list)
#print(labels)

get_rep_str(X_pca_wt, labels_wt, traj_wt, 'wt')

# section of WTD
X_pca_wtd = np.load("../PCA_model_dihed/pca_coord_wtd.npy")
labels_wtd = np.load("../clustering2traj/dbscan_labels/wtd.npy",allow_pickle=True).item() 

traj_files = ['../WT1-6D/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
traj_list = [md.load_netcdf(f, top='../WT1-6D/abeta_linear.parm7') for f in traj_files]
traj_wtd = md.join(traj_list)
#print(labels)

get_rep_str(X_pca_wtd, labels_wtd, traj_wtd, 'wtd')

# section of A2T
X_pca_a2t_beta = np.load("../PCA_model_dihed/pca_coord_a2t_beta.npy")
labels_a2t_beta = np.load("../clustering2traj/dbscan_labels/a2t_beta.npy",allow_pickle=True).item() 

traj_files = ['../A2T_Cbeta_chirality/04remd_14rep/02tex/extract_T/T{}/allT/remd.nc.1'.format(i) for i in range(21,31)]
traj_list = [md.load_netcdf(f, top='../A2T_Cbeta_chirality/abeta_linear.parm7') for f in traj_files]
traj_a2t_beta = md.join(traj_list)
#print(labels)

get_rep_str(X_pca_a2t_beta, labels_a2t_beta, traj_a2t_beta, 'a2t_beta')
