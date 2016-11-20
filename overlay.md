http://stackoverflow.com/questions/21878868/extracting-patches-of-a-certain-size-from-the-image-in-python-efficiently


backup plan: 

randomly select a pixel from mask, use as center of candidate patch; if candidate patch is >T% within mask, then accept as a usable patch -> rotate all directions, and mirror all directions. 


just use benign tumor masses

for normal:
invert masks

merge masks: [example](http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_04/case1045/A_1045_1.LEFT_CC.LJPEG.1_highpass.gif)



For each abnormality, there is a diagnosis (usually one, but sometimes 2 lesion types for the same abnormality):
```
# cancer_09/case3077/B-3077-1.html
ABNORMALITY 1
LESION_TYPE CALCIFICATION TYPE FINE_LINEAR_BRANCHING DISTRIBUTION LINEAR
LESION_TYPE MASS SHAPE ARCHITECTURAL_DISTORTION MARGINS N/A
ASSESSMENT 4
SUBTLETY 5
PATHOLOGY MALIGNANT
TOTAL_OUTLINES 4
BOUNDARY
	CORE
	CORE
	CORE
```

It seems that Calcification type lesions tend to have further outlines ("CORE") pointint to the calcification within the lesion


### TOTAL_ABNORMALITIES (there is sometimes more than one per overlay file)
```bash
for f in `ls -1 ./done/*/case*/*.OVERLAY`; do 
  grep -e 'TOTAL_ABNORMALITIES' $f | awk '{print $2}' >> TOTAL_ABNORMALITIES.txt
done
sort TOTAL_ABNORMALITIES.txt | uniq -c
#   3641 1
#    252 2
#     86 3
#     24 4
#     13 5
#     11 6
#      2 7
#4029 TOTAL
#4644 = 1*3641 + 2*252 + 3*86 + 4*24 + 5*13 + 6*11 + 7*2
```

### TOTAL_OUTLINES (there is sometimes more than one per overlay file)
```bash
for f in `ls -1 ./done/*/case*/*.OVERLAY`; do 
  grep -e 'TOTAL_OUTLINES' $f | awk '{print $2}' >> TOTAL_OUTLINES.txt
done
sort TOTAL_OUTLINES.txt | uniq -c
#   4455 1
#    203 2
#      1 3
#      5 4
#4664 TOTAL

#CORRECTIONS
#./done/benign_13/case3469/B_3469_1.RIGHT_CC.OVERLAY should have only 1 total outline, not 3
#./done/benign_04/case3356/B_3356_1.RIGHT_CC.OVERLAY should hav eonly 1 total outline, not 2
#there are probably others in the 2... but not enough time to manually correct each. 

#example ./done/benign_04/case0334/C_0334_1.RIGHT_CC.OVERLAY:TOTAL_OUTLINES 2

grep 'TOTAL_OUTLINES 2' excess_outlines.txt | cut -f1 -d':' | tee verify_paths.txt | 
#unfinished code
 | awk -F'_' '{print "http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/" $1 "s/" $1 "_" $2 "-" $3 "-" $4 ".html"}' > verify2.txt


```

http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_01/case3030/B-3030-1.html
./done/benign_02/case1282/A_1282_1



cancer_01 Case: B-3030-1
http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_01/case3030/B_3030_1.LEFT_MLO.LJPEG.1_highpass.gif
In this case, there is one boundary, and 3 additional cores. 

Does this mean there is always one boundary per overlay file?


### PATHOLOGIES (there is sometimes more than one per overlay file)
```bash
for f in `ls -1 ./done/*/case*/*.OVERLAY`; do 
  grep -e 'PATHOLOGY' $f | awk '{print $2}' >> PATHOLOGY.txt
done
sort PATHOLOGY.txt | uniq -c
#   1963 BENIGN
#    729 BENIGN_WITHOUT_CALLBACK
#   1935 MALIGNANT
#     37 UNPROVEN
#4664 TOTAL
```

### Anomalous files
```bash
#superfluous overlay file in wrong folder
rm cancer_11/case1826/A_1585_1.RIGHT_MLO.OVERLAY

#extra overlay file in wrong folder (and not expected in original folder metadata)
rm cancer_03/case1059/A_1045_1.RIGHT_MLO.OVERLAY

#Some patients don't have an age
grep -H -e '^PATIENT_AGE' ./done/*/*/*.ics | awk '{if (NF < 2)  print $0 }'
./done/benign_08/case1735/A-1735-1.ics
./done/cancer_10/case1621/A-1621-1.ics
./done/cancer_10/case1654/A-1654-1.ics


#eleven chain codes out of bounds: 
  #e.g. http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/benigns/benign_09/case4070/D-4070-1.html
IndexError: index 2612 is out of bounds for axis 1 with size 2596
IndexError: index 3406 is out of bounds for axis 1 with size 3406
IndexError: index 1846 is out of bounds for axis 1 with size 1846
IndexError: index 2461 is out of bounds for axis 1 with size 2461
IndexError: index 2287 is out of bounds for axis 1 with size 2281
IndexError: index 2139 is out of bounds for axis 1 with size 2131
IndexError: index 2521 is out of bounds for axis 1 with size 2521
IndexError: index 2705 is out of bounds for axis 1 with size 2701
IndexError: index 2102 is out of bounds for axis 1 with size 2086
IndexError: index 1997 is out of bounds for axis 1 with size 1981
IndexError: index 2057 is out of bounds for axis 1 with size 2041
```

### Download thumbnails
Unfinished code:
```bash

target:  http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_01/case3013/B_3013_1.RIGHT_MLO.LJPEG.1_highpass.gif

./done/benign_04/case0334/C_0334_1.RIGHT_CC.OVERLAY:TOTAL_OUTLINES 2

grep 'TOTAL_OUTLINES 2' excess_outlines.txt | cut -f1 -d':' | awk -F'.' 

 | awk -F'_' '{print "http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/" $1 "s/" $1 "_" $2 "-" $3 "-" $4 ".html"}' > verify2.txt

```
