#Open the data file.
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.
import csv
import os
# Assign a variable for the file
#  to load and the path.
# file_to_load = os.path.join('../analysis','election_analysis.txt')

# with open(file_to_load,'w') as file:
#     file.write("hello")

# Create a filename variable to a direct or indirect path to the file.
# file_to_save= os.path.join("../analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save,"w") as text_file:

#    # Write some data to the file
#     text_file.write("Counties In the Election\n ---------------------\n Arapahoe\n Denver\n Jefferson")





file_to_load = os.path.join( "/Users/abbyschneider/Desktop/Data Analysis Class/Election_Analysis/","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("../analysis", "Data Analysis Class/election_Analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)

   # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    








