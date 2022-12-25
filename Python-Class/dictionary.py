# Dictionary in Python

dict1 = {}
print("Type of dict1 = ",type(dict1))

# How to insert values in a dictionary
dict2 = {}
# 'name' is the key and 'Raghavan' is the value mapped against it
dict2['name'] = 'Raghavan'
# 'age' is the key and 38 is the value mapped against it
dict2['age'] = 38
# 'skills' is the key and value is a list here containing "Java" and "Python"
dict2['skills'] = ['Python','Java']
dict2['states_visited'] = ('UP','Maharashtra','Madhya Pradesh')
dict2[45] = 'Random Key'
# Another dictionary
# dict3 = {'color':'Black','nationality':'Indian'}
# Nested dictionary example
# dict2['other_details'] = dict3
dict2['other_details'] = {'color':'Black','nationality':'Indian'}

print("Contents of dict2 = ",dict2)

# Check the length of a dictionary. Returns number of keys we have created in our dictionary
print("Length of the dictionary dict2 = ", len(dict2))

# How to access value of a particular key?
print(dict2['age'])
print(dict2['skills'][1]) # Will print Java
# Accessing dictionary within a dictionary i.e. nested dictionary
print(dict2['other_details']['color'])
print(dict2['other_details']['nationality'])

# How to update value on a particular key?
# updating the age
dict2['age'] = 36
print(dict2['age'])
print("Contents of dict2 = ",dict2)
