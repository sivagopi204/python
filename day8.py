import csv
import json


data = [{'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'}, 
        {'first_name': 'Gopi', 'last_name': 'Chapa', 'phone no': '9012345678', 'address':'Hyderabad', 'email id':'gopi1916@gmail.com'},
        {'first_name': 'Chapa','last_name': 'Gopi', 'phone no': '9801234567', 'address':'Banglore', 'email id':'siva1916@gmail.com'},
        {'first_name': 'srikanth', 'last_name': 'AS', 'phone no': '9870123456', 'address':'Vijayawada', 'email id':'srikanth.as@gmail.com'}, 
        {'first_name': 'ramesh', 'last_name': 'gopi', 'phone no': '9876543210', 'address':'chennai', 'email id':'ramesh@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},
        {'first_name': 'Siva', 'last_name': 'Gopi', 'phone no': '9876543210', 'address':'Vijayawada', 'email id':'sivagopi1916@gmail.com'},]
 
with open('details.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'phone no', 'address','email id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows(data)
with open('details.json', 'w') as f:
    json.dump(data, f,  indent=5)



print("Files created successfully")
