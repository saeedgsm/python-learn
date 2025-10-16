# read file
# with open("faq.txt","r",encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# create file
# f = open("faq.txt","x")
# print(f)


# write file = append
# with open("faq.txt","a") as f:
#     f.write("now the file has more content!")

# with open("faq.txt") as f:
#     print(f.read())


# Overwrite Existing Content
# with open("faq.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("faq.txt") as f:
#   print(f.read())

# with open("faq2.txt", "w") as f:
#   f.write("new file if not Exist")

# with open("faq2.txt") as f:
#   print(f.read())


# Python Delete File
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")



# Delete Folder
# import os

# # os.mkdir("myfolder")

# if os.path.exists("myfolder"):
#     os.rmdir("myfolder")
# else:
#     print("the folder does not exist ")
import csv

# with open('products.csv','w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar="|",quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# with open("products.csv",newline='', encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(f"product name: {row['name']} | price: {row['price']}")

# Define header and data rows
# fields = ['Name', 'Branch', 'Year', 'CGPA']
# rows = [
#     ['Nikhil', 'COE', '2', '9.0'],
#     ['Sanchit', 'COE', '2', '9.1'],
#     ['Aditya', 'IT', '2', '9.3'],
#     ['Sagar', 'SE', '1', '9.5'],
#     ['Prateek', 'MCE', '3', '7.8'],
#     ['Sahil', 'EP', '2', '9.1']
# ]

# filename = "university_records.csv"
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)        # Create writer object
#     csvwriter.writerow(fields)             # Write header
#     csvwriter.writerows(rows)  


# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)