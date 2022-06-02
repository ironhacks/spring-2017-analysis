# Functional Similarity
This app calculates the funnctional similarity between code for the same problem statement

##Installation
Git clone this repository to your machine

##Configuration
- Edit `code/FunctionalSimilarity.py`. Last few lines should be edited to replace `fall2016-blackironhack` with the required hack names. On the same code lines, edit the last number to reflect the number of phases in the hackathon.

- Edit existing dictionaries in the `dictionary` folder to suit the code usage as per your hackathon

- Create new dictionaries in the `dictionary` folder. Use the following convention:
```
<library-name>-<module-inside-library>.txt
```

##Idea
This app calculates same phase and cross phase functional similarity between codes of participants in an interactive hackathon. Functional similarity can have two levels of granularity:
+ L1 Similarity: Indicates how similar two applications are as per their usage of javascript libraries. Two projects using the libraries will have a L1 similarity of `1`. Can take a value in the range `[0, 1]`
+ L2 Similarity: Indicates how similar two applications are as per the usage of features of the libraries. This is at a more granular level than L2 similarity. The L2 similarity of two projects will always be less than or equal to L1 similarity between them. Can take a vaue in the range `[0, 1]`

##Usage:
You should have python version 3.0 or higher installed on your system. Simply run
```sh
python FunctionalSimilarity.py [hackName] [numPhases] [fetch]
```
If fetch is 1, then repos will be cloned from github, otherwise, similarity will be generated on existing data.
Reports would be generated in reports folder. The report name itself should help you distinguish whether it corresponds to
+ Same phase or cross phase similarity
+ L1 similarity or L2 similarity
+ Similarity with or without templates

##Debugging and Future Work
+ [ ] TODO: Add logging, everything is output to console now
+ [ ] TODO: Check dictionary for the current hackathon
+ [x] TODO: Output results of LibraryExtractor somewhere
+ [ ] TODO: Git Diff fails for Binary files, handling via exception now. No Binary file is created, could possibly be improved.

## Developer Documentation
- Coming Soon