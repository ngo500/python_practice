import pandas as pd

#save url
url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
#read csv file to df
df = pd.read_csv(url,header=None)

print("csv files")
print("")

#no column names, just numbers
#print(df)

#add columns names
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

#print("whole data frame:")
#print(df)

#print just specified column
print("Just First Name column:")
print(df["First Name"])

#select multiple columns
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print("whole data frame:")
print(df)

#select the first row
print("first row only:")
print(df.loc[0])

#select thee first, second, and third row of "First Name" column
print("just the 1st, 2nd, 3rd row of First Name column using loc:")
print(df.loc[[0, 1, 2], "First Name"])

#select the first, second, and third row of the "First Name" column
print("just the 1st, 2nd, 3rd row of First Name column using iloc:")
print(df.iloc[[0, 1, 2], 0])


import numpy as np

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

print("whole data frame:")
print(df)

#transform the df- add 10 to every element
df = df.transform(func = lambda x : x + 10)

print("whole data frame, transformed by adding 10 to every element:")
print(df)

#transform the df- find the sqrt of every element, but save it in a different df
result = df.transform(func = ['sqrt'])
print("whole data frame, transformed by taking the square root of every element:")
print(result)


import json

print("json files")
print("")

#create a dictionary object
person = {
    'first_name' : 'Mark',
    'last_name' : 'Smith',
    'age' : '27',
    'address' : {
        "streetAddress" : "21 2nd St",
        "city" : "New York",
        "state" : "NY",
        "postalCode" : "10021-3100"
    }
}
print("dictionary object:")
print(person)

#use json.dump to write to a json file
#open(json file to create, mode)
#   .dump(dictionary to create json from, file pointer opened in write/append
with open('person.json', 'w') as f:
    json.dump(person, f)

#serialize json (indent is number of units for indents)
json_object = json.dumps(person, indent = 4)

#write to json file
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print("serialized json that was sent to file:")
print(json_object)

#open the json file
with open("sample.json", "r") as openfile:
    json_object2 = json.load(openfile)

print("deserialized json that was retrieved from file:")
print(json_object2)
print(type(json_object2))


import urllib.request

print("xlsx files")
print("")

#get file and savee as sample.xlsx
urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
#store file as df
df = pd.read_excel("sample.xlsx")

print("entire data frame:")
print(df)


print("xml files")
print("")

import xml.etree.ElementTree as etree

#create file structure
employee = etree.Element('employee')
details = etree.SubElement(employee, 'details')
first = etree.SubElement(details, 'firstname')
second = etree.SubElement(details, 'lastname')
third = etree.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

#create a new XML file with data
data1 = etree.ElementTree(employee)

#write to xml file with given xml
with open("sample.xml", "wb") as files:
    data1.write(files)




url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml'
#get file and save as samp1.xml
urllib.request.urlretrieve(url, "samp1.xml")
#store file as tree
tree = etree.parse("samp1.xml")

#save the root
root = tree.getroot()
#make names for columns
columns = ["firstname", "lastname", "title", "division", "building", "room"]

#create df
df = pd.DataFrame(columns = columns)

#loop to get data into df
for node in root:
    firstname = node.find("firstname").text

    lastname = node.find("lastname").text 

    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    df = df._append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)


print("entire data frame:")
print(df)

#save the df to a .csv file
df.to_csv("employee.csv", index = False)



print("binary files")
print("")


from PIL import Image

#get jpg
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

#read image
img = Image.open('dog.jpg')

#image read
print(img)


#data analysis

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

#show the first 5 rows
print("first 5 rows: ")
print(df.head(5))

print("dimensions:")
print(df.shape)

print("stat overview:")
print(df.info)

print("more info like index dtype col, nonnull values, memory usage:")
print(df.describe())

#get null values
missing_data = df.isnull()
print("bool that shows if null ie missing data for first 5 rows:")
print(missing_data.head(5))

#count any null/missing values
for column in missing_data.columns.values.tolist():
    #print(column)
    print(missing_data[column].value_counts())
    print("")

#data format
print("check the data type")
print(df.dtypes)



import matplotlib.pyplot as plt

#show amount of women that are diabetic vs not diabetic on a pie chart

#labels for chart percentages
labels = 'Not Diabetic', 'Diabetic'
#using outcome, display both as percentage
plt.pie(df['Outcome'].value_counts(), labels = labels, autopct = '%0.02f%%')
#show diabetic/not diabetic legend with color on side
plt.legend()
#display chart
plt.show()
