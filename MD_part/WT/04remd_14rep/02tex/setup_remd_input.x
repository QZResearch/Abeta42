#!/bin/bash -f

if [ -f groupfile ];
then
  rm groupfile
fi

nrep=`wc ../temperatures.dat | awk '{print $1}'`
echo $nrep
count=0
for TEMP in `cat ../temperatures.dat`
do
  let COUNT+=1
  REP=`printf "%03d" $COUNT`
  echo "TEMPERATURE: $TEMP K ==> FILE: remd.mdin.$REP"
  sed "s/XXXXX/$TEMP/g" REMD.RST.mdin > temp
  sed "s/RANDOM_NUMBER/$RANDOM/g" temp > remd.mdin.$REP
  echo "-O -rem 1 -remlog rem6.log -i remd.mdin.$REP -o remd6.mdout.$REP -c remd5.rst.$REP -r remd6.rst.$REP -x remd6.mdcrd.$REP -inf remd6.mdinfo.$REP -p ../../abeta_linear.parm7" >> remd.groupfile
  
  rm -f temp
done
echo "#" >> groupfile

echo "N REPLICAS  = $nrep"
echo " Done."


