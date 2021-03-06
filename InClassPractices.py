# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who rceived votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


# Import the datetime class from the datetime module
import datetime as dt
# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# print present time
print("The time right now is ", now)


# Assign a variable for the file to load and the path.
file_to_load = 'resources/election_results.csv'

# Open the elction results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis

# Close the file
election_data.close()

with open(file_to_load) as election_data:

    # To do: perfom analysis.
    print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
