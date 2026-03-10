#!/bin/bash -f

if [ -f groupfile ];
then
  rm groupfile
fi

if [ -f remd.groupfile ];
then
  rm remd.groupfile
fi

nrep=`wc ../temperatures.dat | awk '{print $1}'`
echo $nrep
count=0
for TEMP in `cat ../temperatures.dat`
do
  let COUNT+=1
  REP=`printf "%03d" $COUNT`
  echo "TEMPERATURE: $TEMP K ==> FILE: remd.mdin.$REP"
  sed "s/XXXXX/$TEMP/g" REMD.mdin > temp
  sed "s/RANDOM_NUMBER/$RANDOM/g" temp > remd.mdin.$REP
  echo "-O -rem 1 -remlog rem.log -i remd.mdin.$REP -o remd.mdout.$REP -c ../01equal/equilibrate.rst.$REP -r remd.rst.$REP -x remd.mdcrd.$REP -inf remd.mdinfo.$REP -p ../../abeta_linear.parm7" >> remd.groupfile
  
  rm -f temp
done
echo "#" >> groupfile

echo "N REPLICAS  = $nrep"
echo " Done."


