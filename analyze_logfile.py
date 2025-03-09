# Log File Analyzer Script
# This script extracts ERROR and WARNING messages from a given log file and saves them to an output file.

# Uncomment the following line to allow the user to provide the log file path manually:
# input_file = input("Enter the path of the Log File: ")

# Uncomment the following lines to enable file upload in Google Colab:
'''
from google.colab import files
input_file = files.upload()
'''

# Define the input and output file paths (Update this path according to your system)
input_file = r"F:\Engineering\Internships\Internship_2k25_Infoblox\Assignments\logfile.log"  # Use raw string (r"") to avoid escape character issues
output_file = "outputfile.txt"  # Output file where filtered logs will be stored

# Open the input file and read all lines
with open(input_file, "r") as infile:
    lines = infile.readlines()  # Read all lines from the log file

# Initialize an empty list to store filtered messages
filtered_lines = []

# Define the keywords to filter (ERROR and WARNING)
extract_condition_words = ["error", "warning"]

# Iterate through each line in the log file
for line in lines:
    lower_line = line.lower()  # Convert line to lowercase for case-insensitive matching
    if any(word in lower_line for word in extract_condition_words):  # Check if any keyword exists in the line
        filtered_lines.append(line)  # Append the original line (preserving case) to the filtered list

# Write the extracted messages to the output file
with open(output_file, "w") as outfile:
    outfile.writelines(filtered_lines)  # Write filtered messages to the file

# Print confirmation message
print("Log analysis complete.\nExtracted messages saved to outputfile.txt.")

# Display the contents of the output file
with open(output_file, "r") as output:
    print(output.read())  # Read and print the extracted log messages
    
