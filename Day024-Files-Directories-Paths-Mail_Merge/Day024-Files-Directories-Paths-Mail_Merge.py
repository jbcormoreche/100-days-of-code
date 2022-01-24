# Files, Directories and Paths

# Open, read and close a file
file = open("my_file.txt")  # same as file = open("./my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open and read a file without having to remember to close a file
with open("./Day024-Files-Directories-Paths-Mail_Merge/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write to a file (deletes the previous content)
with open("./Day024-Files-Directories-Paths-Mail_Merge/my_file.txt", mode="w") as file:
    file.write("New text.")

# Add/append to a file
with open("./Day024-Files-Directories-Paths-Mail_Merge/my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# If the file doesn't exist, it will create it
with open("new_file.txt", mode="w") as file:
    file.write("New text.")

# An absolute path contains the root element (/) and the complete directory list required to locate a file
# ex: /Users/LondonAppBrewery/Desktop/new_file.txt

# A relative path starts from a working directory
#  ex: ../../Desktop/new_file.txt
# ./ to go down the directory tree
# ../ to go up the directory tree

# Day 24 Project - Mail Merge
with open("./Day024-Files-Directories-Paths-Mail_Merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
stripped_names = []
for name in names:
    stripped_names.append(name.strip("\n"))

for name in stripped_names:
    with open("./Day024-Files-Directories-Paths-Mail_Merge/Input/Letters/starting_letter.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[name]", name)
    with open(f"./Day024-Files-Directories-Paths-Mail_Merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_file:
        completed_file.write(contents)
