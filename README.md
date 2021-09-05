# Election_Analysis

## Overview of Election Audit

Our clients, Seth and Tom, liked the analysis we did on the election audit, but they wanted some additional data to complete the audit. They wanted the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout. We needed to add code to find the new requested data.

### Purpose

The purpose of this election audit is to find the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout.

## Election-Audit Results

* There were 369,711 total votes cast in this congressional election. We figured this out by analyzing the data row by row to extract the total votes cast.

```# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data) 
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
```

* Jefferson County had a total of 38,855 votes, which accounted for 10.5% of the total votes. Denver County had a total of 306,055 votes, which made up for 82.8% of the total votes. Arapahoe County had 24,801 votes, and 6.7% of the total votes. 

```
        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:  

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1      
```

* Denver County had the largest turnout with 82.8%. 

``` 
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes_county > largest_county_count) and (vote_percentage_county > winning_percentage_county):    
```

* Charles Casper Stockham received 85,213 votes, which was 23.0% of the total votes. Diana DeGette received 272,892 votes, which was 73.8% of the total votes. Raymon Anthony Doane received 11,606 votes, which was 3.1% of the total votes.

```
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage        

```

* Diana DeGette won the election with 73.8% of the total votes. She received a total of 272,892 votes. 

```
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

```

## Election-Audit Summary

Our code works well for this election audit. With a few changes, we can update the code to work for other elections. A few possible modifications are adding a year column, to get data from multiple years, and comparing the data between the years. Adding these changes will allow us to see election patterns.