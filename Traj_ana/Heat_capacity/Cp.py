#!/bin/python

import numpy as np
import pandas as pd
CAL2J = 4.184


def loadlog(Ts,fs,fe):
	temps = np.loadtxt(Ts)
	output = {}
	for t in temps:
		output['{:.2f}'.format(t)] = []

	for x in range(fs,fe+1):
		tmp_file = '../../rem{}.log'.format(x)
		with open(tmp_file,'r') as f:
			while True:
				line = f.readline()
				if not line:
					break
				else:
					if len(line.split()) == 8:
						temp0 = float(line.split()[4])
						eptot = float(line.split()[3])
						output['{:.2f}'.format(temp0)].append(eptot)
	return output			  


def readmdouts(Ts, fs, fe):
	temps = np.loadtxt(Ts)
	output = {}
	for t in temps:
		output['{:.2f}'.format(t)] = []

	for x in range(fs,fe+1):
		for rep in range(1,15):
			tmp_file = '../../remd{}.mdout.{:03d}'.format(x,rep)
			with open(tmp_file,'r') as f:
				while True:
					line = f.readline()
					if not line:
						break
					else:
						if 'NSTEP' in line:
							temp_curr = float(line.split()[8])
							line = f.readline()
							etot = float(line.split()[2])
							for _ in range(10):
								line = f.readline()
								if 'TEMP0' in line:
									#print(line)
									temp0 = float(line.split()[2])
									break
							output['{:.2f}'.format(temp0)].append([etot,temp_curr])
	return output



def heatcap(data):
	kb = 1.380649*10**-23 # J/K-1
	NA = 6.02*10**23	  # Avogadro unit mol-1
	output = []
	for k,v in data.items():
		T = float(k)
		v = np.array(v)
		PTOT = v[:,0]*CAL2J*1000
		TEMP = v[:,1]
		#print(T,PTOT)
		#print(T,np.array(v))
		v_mean = np.mean(PTOT)
		v_mean_2 = v_mean ** 2
		v_2	= np.array(PTOT)**2
		v_2_mean = np.mean(v_2)
		T_mean   = np.mean(TEMP)		

		cp = (v_2_mean - v_mean_2)/NA/kb/T_mean**2
		#cp1 = np.var(PTOT)/NA/kb/T**2

		output.append([T,T_mean,cp])
	return np.array(output)



if __name__ == '__main__':
	#outene = loadlog('../../../temperatures.dat',21,30)
	outene = readmdouts('../../../temperatures.dat',13,20)
	cp = heatcap(outene)
	# The heat capacity in the unit of J/mol/K
	#print(cp)
	np.savetxt('heat_capacity.txt',cp)
	
