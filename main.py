"""
USAGE - The code reads a list of names from a text file, and for each name, it opens another 
        text file that serves as a letter template. The code replaces a placeholder string 
        in the template with the current name and writes a new version of the letter to a 
        separate output file, which is named according to the recipient's name.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
