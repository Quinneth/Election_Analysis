# Election_Analysis

## Project Overview
Colorad Board of Election employee has given the following tasks to complete the election audit a recent local congressional election.

1. Calulate te total number of votes cast.
2. Get a complete list of candidates who received votes 
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidates won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source : [election_results.csv](/Resources/election_results.csv)
- Software : Python 3.7 (64 bit) .Visual Studio Code.
- PyPoll_Challenge_starter_code.py


## Summary 
The analysis of the election show that :
There were 369 711 votes cast in the election. 
- **The candidates were :**
    - Candidate 1 : *Charles Casper Stockham
    - Candidate 2 : *Diana DeGette
    - Candidate 3 : *Raymon Anthony Doane   
- **The candidates results were :**
    - Candidate 1 received 3.0% of the vote and 85,213 number of votes.
    - Candidate 2 received 73.8% of the vote and 272,892 number of votes.
    - Candidate 3 received 3.1% of the vote and 11,606 number of votes.  
    
- **The winner of the election was :**
    - Candidate 2, *Diane DeGette,* who received 73.8 % of the vote and 272,892 number of votes.**
 
## Challenge overview
Revisit Pypoll election audit. Revise script for additional analysis relating to voter turnout based on county. 

1. Extract a complete list of the counties.
2. Calculate the total number of votes for each county.
3. Calculate the percentage of votes for each county.
4. Determine the county with the highest turnout.

## Challenge Results

The analysis of the election show that :

**There were 369 711 votes cast in the election.**

- **Counties included in precint :**
  - County 1:  Arapahoe
  - County 2:  Jefferson
  - County 3:  Denver

- **Total votes and the percentage of total votes per county ranked lowest to highest :**
  - 1. Arapahoe:  24,801 *(6.7%)*
  - 2. Jefferson:  38,855 *(10.5%)*
  - 3. Denver:  306,055 *(82.8%)*
  
- **County with largest number of votes :**
  - ***Denver***, county 2,cast the most votes in the precinct with a total of 306,055 *(82.8%)*
  
- **Denver county breakdown by number and percentage of votes per candidate**
  - 1. Diana DeGette:  272,892 *(73.8%)
  - 2. Charles Casper Stockham:  85,231 *(23.0%)
  - 3. Raymon Anthony Doane:  11,606 *(3.1%)*  
- **Election Winner:**
    - Candidate : ***Diana DeGette***
    - Vote Count:  **272,892**
    - Percentage:  **73.8%**

   
## Election-Audit Summary
   
The goal of this Python script provides potentially actionable insights. The script used to generate the outputs could be adapted for future elections or expanded to include larger precincts and varied candidates. Depending on the dataset, the election commission could extract more specific voter attributes or tracked these results over time to detect trends. 
The results provided could be used to target "Get out the Vote" campaigns in poorly performing precincts. 
   
