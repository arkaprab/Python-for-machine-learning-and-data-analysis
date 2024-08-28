my_dictionary={"Country" : 'Capital',
              "India" : 'New Delhi',
              "Russia" : 'Moscow',
              "Iraq" : "Baghdad",
              "Iran" : "Tehran",
              "United States":"Wahington DC"}
print(my_dictionary)
print(type(my_dictionary))

print(my_dictionary["Iran"])
print(my_dictionary["India"])
print(my_dictionary["United States"])

#Dictionary doesnt allows duplicate values.
dictionaries={"Key":"Number",
              "1":"200",
              "1":"200"}
print(dictionaries)