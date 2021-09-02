# Spring 2017 IronHacks ReadMe :wink:
## Spring 2017 Purdue and Bogota IronHacks :neckbeard: 


## Link to Analysis Plan - https://docs.google.com/document/d/1VVUgQH9RfCzhaBqLwxk4KuRjpURCHKJN3kYDWh8GTSY/edit

## Link to Data Dictionary - https://github.com/ironhacks/participants-code-2015-2019/blob/main/analysis/Spring-2017-Data-Dictionary.ipynb

### During the first part of this document, you will read about the general process of the Gold Ironhacks. On the subsequent part, you will get a deeper understanding on the raw data collected. Finally, you will be guided through the process of how we transform the data collected.

## 00 Pre-Analysis of Participant :purple_heart: 

Total number of Participants in each category for ALL Phase for Purdue Hack

:grinning: Purdue Hack = 42 people 

Total number of Participants in each category for ALL Phases for Bogota Hacks

:grinning: Bogota 0 = 39 people
:grinning: Bogota 1 = 41 people
:grinning: Bogota 2 = 41 people
:grinning: Bogota 3 = 41 people

## 01 Raw Click Data :blue_heart: 

For Purdue 

Click data for scores is located at 02 Data -> 2 - 1 Raw -> 01 Raw click data -> 01 Purdue -> 2017-08-12-12-36-scores.csv

For Bogota 

Click data for topics is located at 02 Data -> 2 - 1 Raw -> 01 Raw Click data -> 02 Bogota -> 2017-04-28-01-16-topics.csv

Click data for scores is located at 02 Data -> 2 - 1 Raw -> 01 Raw Click data -> 02 Bogota -> 2017-08-12-12-36-scores.csv


## 02 Detailed Analysis :green_heart: 

### Number of Participants who didn't submit :alien: 

### Number of People who didn't submit in each phase for Bogota 0 :cop: 

### Phase 1 :hibiscus:
Bogota 0 = 11 people

### Phase 2 :hibiscus:
Bogota 0 = 0 people
 
### Phase 3 :hibiscus:
Bogota 0 = 10 people

### Phase 4 :hibiscus:
Bogota 0 = 8 people 
 
### Phase 5 :hibiscus:
Bogota 0 = 8 people 


### Number of People who didn't submit in each phase for Bogota 1 :cop: 

### Phase 1 :palm_tree:
Bogota 1 = 8 people

### Phase 2 :palm_tree:
Bogota 1 = 1 person 

### Phase 3 :palm_tree:
Bogota 1 = 5 people

### Phase 4 :palm_tree:
Bogota 1 = 4 people 

### Phase 5 :palm_tree:
Bogota 1 = 5 people

### Number of People who didn't submit in each phase for Bogota 2 :cop: 

### Phase 1 :sunflower:
Bogota 2 = 10 people

### Phase 2 :sunflower:
Bogota 2 = 0 people

### Phase 3 :sunflower:
Bogota 2 = 3 people

### Phase 4 :sunflower:
Bogota 2 = 3 people

### Phase 5 :sunflower:
Bogota 2 = 3 people

### Number of People who didn't submit in each phase for Bogota 3 :cop: 

### Phase 1 :herb:
Bogota 3 = 6 people

### Phase 2 :herb:
Bogota 3 = 0 people 

### Phase 3 :herb:
Bogota 3 = 4 people

### Phase 4 :herb:
Bogota 3 = 4 people 

### Phase 5 :herb:
Bogota 3 = 3 people


## 03 Steps to Process the Data :blue_heart:

### The big excel sheet for spring 2017 is located at [Dropbox Link Here](https://www.dropbox.com/home/09%20NSF%20open%20data/05%20Experiments%202017/01%20Hack%20Spring%202017?preview=Data_Cleaning_By_Jay.xlsx)
### This excel sheet will tell you who submit and who did not in each phase. 
### It will also tell you who do not have infovis score in a particular phase. The definition of "who do not have infovis score" is defined by the fact that they DID submit but their apps DO NOT compile. 


Topics covered in this file:

### Background info
1.1 Task-Timeline-Prices-Intervention Design <br />
1.2 Technical platform used. <br />
1.3 Training. <br />
1.4 Individual feedback. <br />
1.5 Judging and Evaluation criteria. <br />
1.6 Survey structure.<br />

### Data
2.1 Raw data. <br /> 
2.2 Cleaned Data. <br /> 
2.3 Processed data. <br />
2.4 Scripts. <br /> 

## 1. Background Info
## 1.1. Task-Timeline-Prizes-Intervention design
Basics: This hack was focused on "Finding fresh and cheap vegetables in Lafayette".

Type of Hack: Class Hack Students from Purdue University.

Time frame: 09/07/2016 to 10/05/2017.

The actual task description and rules and prizes and further details on the hack can be found in this 'manual'. This manual was created by the team running this hack in Fall 2016.

The hack was run in two classes at Purdue University (CNIT531, CGT 531). Prof. Sabine Brunswicker worked with Prof. John Springer, and Prof. Chen.

In this IronHacks, we implemented a single treatment: Performance transparency in a quasi-experimental design setting (no randomization).

Performance transparency: All hackers had information about other's scores. Transparency is designed into the platform and it is not under control of the participants (they couldn't decide wether to make it transparent or not).

See a screenshot of how we structured this here

This information was accessible via a website on the portal (only accessible for registered users). For further detail on the architecture of the platform and its conceptual foundation also see the paper

Brunswicker et al. (2018). Transparency as a design choice of open data contests. Journal of Information Technology and Sciencs, Forthcoming

Performance transparency: All users were expose to their individual score and others participants performance.

For the perfomance transparency, we displayed the participants' score for each dimension (Technology, User Experience, Info visualization, Novelty).

Here is the dropbox link to the summary of treatments.

## 1.2. Technical platform used
The contest was ran on four separate phases as described in the task and handout referred above (see 1.1).

The actual platform we used. It is no longer hosted yet there is the structure of the database information. For further information please go to section 2.1.

The GoldIronhacks platform was hosted on Heroku and powered by Meteor js. The presentation of the platform is similar to the one used on the green IronHacks Spring 2016 without the project visualization of the project and code (view here to look the green feedback view).

## 1.3 Training
We trained the students prior and during the hack. Information on the presentation shown are here.

Description and links for the material used to train the participants on the minimum technical knowledge needed to complete the task. Link here.

## 1.5. Judging and Evaluation criteria
After each phase, the tech judging and user experience judging will be carried out in the form of excel evaluation sheets.

In the GoldIronHacks, we had two tech judges and four user experience judges. After the tech judges were done with the tech judging, the judging sheets handed over to the user experience judges.

You can find a more detail description of the criterias of these dimensions in the documents with the evaluation forms used by the two types of judgers:

InFoVis and Tech:

After all judgings are done, individual emails will be sent out to all participants to inform them about their performance on each phase. The participants will be directed to the platform to check out other participants' performances.

## 1.2. Individual feedback
In addition to transparency feature on the platform (acccesssible for all participants), each participant received an email of the percentile rank scores. An example can be seen here and the log file when the emails were sent.

Here is the link of the raw data to the percentiles shown in the individual email.

The % of participants whose InfoViz score below your score
The % of participants whose Nolvelty score below your score
The % of participants whose Tech score below your score
The % of participants whose User Requirement score below your score
1.7 Survey structure
We sent two surveys to be filled in. THese survey's were administered via qualtrics. THey were mandatory in order to qualify for the award (see 1.1).

## 2. Data
## 2.1. Raw Data
Click Data: We used Google Analytics to track the clicks when the user click on the button beside the total score to see the detailed scores, links to projects and codes.

Absolute and percentile score data

In the GreenIronhacks, we had the absolute and percentile score. The absolute score is the raw score that each participant got on the four dimensions evaluated (Technology User Experience, Infovis, Novelty). The percentile score is the score that the participants get in relative to others. In the Greenironhacks platform, we displayed the percentile score data.

Raw evaluations
Raw evaluations were performed by the tech judges and UX judges. A total percentile score sheet will then be created after the judgings are done.

Survey data
In the survey folder, you will be able to locate for the survey data performed on qualtrics. The post survey was done after the experiments ended. The survey data was collected in qualtrics.

Participants code
The participants code are stored in GitHub under the folders Goldironhacks. During the GoldIronhacks competitions, the apps are hosted on the Amazon Web Services to be displayed on the platform. The apps would have to be re-hosted from GitHub if needed.

Community data (likes, number of comments)
The community data are stored in the click data folder. The community data consists of clicks and comments made by the participants on the forums during the contests.

Further, you will also be able to locate the click data recorded when participants clicks on the others' posts and comments. The number of times the participants posted and commented on the forums are also recorded in the click data folder.

Interview data
After the competition ended, the winnners of the competition mainly the best solution winner, the improvement award winner and the community spirit winner were interviewed. The videos for these interviews can be found on RCODI twitter account, facebook and youtube channel.

Database
The database was under an object-oriented structure. Here are the export JSON files of the database. These structures could be used to restructure the database if needed. Each file represents a collection (an object) that stores the respective information of the hack. For more detail refer to this readme.

Commits
Here is the link for the commits generated by the participates when submtting to save their code.

## 2.2 Cleaned data
From the raw data, the files had a data handling to were a better representation of the data.

click data
abs_percentile scores This file contains all the phases of each participant
disaggregated evaluations
For the additional information: the -1 values are missing values when the complexity code was performed.
## 2.3 Processed Data
We processed the data to collect the code similarities and functional similarities. The code similarity was collected based on the MOSS algorithm. The functional similarity scores were collected based on the similarities of the functions that the participants used.

## 2.4 Scripts
This section has the "libraries sniffer" code and the complexity input and here is the link for the similarity scores

