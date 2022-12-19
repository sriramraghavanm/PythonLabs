# Syntax for while loop
# while expression:
#    statements

# Write a program to print the table of 9
num = 9
counter = 1
while counter <= num + 1:
    ans = num * counter
    print(num," * ",counter," = ",ans)
    counter = counter + 1
    
# What will happen if counter is not incremented ??
# while counter < num + 1:
#     ans = num * counter
#     print(num," * ",counter," = ",ans)

# What will happen if this is executed ??   
# while True:
#     print("Raghavan")
