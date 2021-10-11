file=name-list.csv
while IFS= read -r line
do
    diff spring2017-unal-goldironhack-phase2/2017-Purdue-UNAL-IronHack-$line spring2017-unal-goldironhack-phase1/2017-Purdue-UNAL-IronHack-$line  | diffstat
done < "$file"
