# python program that reads the data from the text file and prints it out in two different sections

# putting names in a form of a list
name = []

# putting birthdays in a form of list
birthday = []

# reading the content of the text
# and store in a string variable
# named dob using read() function
f = open("DOB.txt", "r")
dob = f.readlines()

# for list in range,
for list in dob:
    # file is initialize to list.split()
    file = list.split()

    # name.append file in position 2 in the list of dob
    name.append(file[:2])

    # birthdays.append file in position 2 in the list of dob
    birthday.append(file[2:])

# close file
f.close()

# displaying the content of name
print("Name")

# for i, name in enumerate name starting from position one(1) in the file
for i, name in enumerate(name, start=1):
    # displaying all the names in the file
    print("{}. {}".format(i, " ".join(name)))

    # print new line
print("\n")

# displaying the content all the birthday from yhe file
print("Birthdays: ")

# for i, birthday in enumerate from position one(1) in the file
for i, birthday in enumerate(birthday, start=1):

    # displaying all the birthday in the file
    print("{}. {}".format(i, " ".join(birthday)))

