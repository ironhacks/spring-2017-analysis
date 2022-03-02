## Track Change Extractions for Each Phase

Run the file with the command 

```
./ifs.sh

```

We get the changes for the relevant phase from running the script above

Then we do, 

```
grep '^ [0-9]' diff.txt > phase-1-2-prelim.csv

```
to get the line with only the track change 

Output the file with the desired file name



