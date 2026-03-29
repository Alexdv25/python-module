# friends = ['Rolf', 'Bob', 'Jen', 'Anne']

# for friend in friends:
#     print(f"{friend} is my friend") 
    
# #range()
# for number in range(4):
#     print(f"{number} is my friend")
    
    
# #steps()
# for number in range(0, 10,-1):
#     print(f"{number} is my friend")

grades = [80, 75, 90, 100, 85]
amount = len(grades)
total = 0

for grade in grades:
    #total = total + grade
    total += grade
    
print(total/amount)