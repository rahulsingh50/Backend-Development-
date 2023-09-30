# Conditional operator

# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

# write a  simple calculator(+,-,*,/)

# num1,operator, num2 = (input("Enter Calculation(num1, operator,num2 ")).split()
# num1 = int (num1)
# num2 = int (num2 )
# if operator == '+':
#     print(" {} + {} = {}".format(num1,num2, num1 + num2))
# elif operator == '-':
#     print(" {} - {} = {}".format(num1, num2, num1 - num2))
# elif operator == '*':
#     print(" {} * {} = {}".format(num1, num2, num1 * num2))
# elif operator == '/':
#     print(" {} / {} = {}".format(num1, num2, num1 / num2))
# else:
#     print("Either use +,-,*,/ or next time")


# logical operator

# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa

'''
I’ll now write a program that will determine whether a birthday is important or not. I’ll use the
following criteria to determine that.

1 - 18 -> Important
21, 50, > 65 -> Important
All others -> Not Important
'''
age = int(input("Enter the age :"))
if (age > 1) and (age <= 18):
    print("birthday is Important")
elif (age == 21) or (age == 65):
    print("Birthday is Important")
elif age < 65:
    print("Birthday is important")
else:
    print("Not birthday is important")



'''
1. If age 5 “Go to Kindergarten”
2. Ages 6 through 17 goes to grades 1 through 12 “Go to Grade 6”
3. If age is greater then 17 then say “Go to College”
Here is sample output :
Enter age : 6
Go to Grade 6

'''
age = int(input("Enter the the age "))
if age < 5:
    print("You are two young to collage")
elif age == 5:
    print("Go tho the Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Goes to {}".format(grade))
else:
    print("Goes to grades Collage")


'''
Ternary Operator
The ternary operator is used to assign one value or another based on a condition. It follows this
format condition_true if condition else condition_false
'''

age = int(input("Enter your age :"))
can_vote = True if age >= 18 else False
print("You can vote :", can_vote)

