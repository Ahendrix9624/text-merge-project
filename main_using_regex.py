"""
USAGE -  uses regular expressions to find any file path in the Input/Names and Input/Letters directories. 
         It then reads the contents of invited_names.txt and starting_letter.txt, and for each name 
         in invited_names.txt, it replaces the [name] placeholder in starting_letter.txt with 
         the name and saves the new letter to a file in the Output/ReadyToSend directory with 
         the format letter_for_{name}.txt

AUTHOR - https://github.com/Ahendrix9624/
"""
import re
import glob

PLACEHOLDER = "[name]"
name_files = glob.glob("Input/Names/*")

for name_file in name_files:
    with open(name_file) as names_file:
        names = names_file.readlines()

    with open("Input/Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
        for name in names:
            stripped_name = name.strip()
            new_letter = re.sub(PLACEHOLDER, stripped_name, letter_contents)
            with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)
