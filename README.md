# python-challenge

# python-challenge - Py Me Up, Charlie

## Background

Well... you've made it!

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this assignment, you'll be using the concepts you've learned to complete the **two** Python Challenges, PyBank and PyPoll.

Both of these challenges encompass a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead!

### Before You Begin

* Create a new repository for this project called `python-challenge`. 

* Clone the new repository to your computer.

* Inside your local git repository, create a directory for each Python Challenge. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder that you just created, add the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
  * An "analysis" folder that contains your text file that has the results from your analysis.



## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
==================================================

 Financial Analysis 

==================================================

Total months : 86

Total amount : $38382578.0

Avgrage change : $-2315.12

greatest increase in profit : Feb-12 ($1926159.0)

greatest decrese in losses : Sep-13 ($-2196167.0)

==================================================
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
* The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
* Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
==================================================

 Election Results 

==================================================

Total Votes:  1048575

----------------------------------------------------

Khan: 63.09%  (661583)

Correy: 19.94%  (209046)

Li: 13.96%  (146360)

O'Tooley: 3.01%  (31586)

----------------------------------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down your tasks into discrete mini-objectives. This will be a _much_ better course of action than spending all your time looking for a solution on Stack Overflow.

* As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".

* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.


* Always commit your work and back it up with GitHub/GitLab pushes. You don't want to lose hours of your work because you didn't push it to GitHub/GitLab every half hour or so.

* Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

## Results and Solution

* Solution file can be found under Resources folder 
* Results can be found under analysis folder
