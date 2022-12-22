# Output as HWeolrllod

str1 = "Hello"
str2 = "World"

# Get length of both the strings
str1len = len(str1)
str2len = len(str2)

i = 0 # counter for str1

# using while loop
while i < str1len and i < str2len:
    print(str1[i] + str2[i], end = '', flush = True)
    i += 1 # this is equal to i = i + 1
    
# using for loop
for i in range(len(str1)):
    for j in range(len(str2)):
        if i == j:
            print(str1[i] + str2[j], end = '', flush = True)
