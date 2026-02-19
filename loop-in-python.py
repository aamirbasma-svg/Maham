# while loop program
print("While loop program:")
i=1 # initialization
while i<=10: # condition
    print(i) # output
    i+=1 # increment
print()

# for loop program
print("For loop program:")
for i in range(1,5): # initialization, condition, increment
    print(i) # output
print()

# for nested loop program
print("For nested loop program:")
for i in range(1,3): # initialization, condition, increment for outer loop
    for j in range(1,6): # initialization, condition, increment for inner loop
        print(i,j) # output
print()