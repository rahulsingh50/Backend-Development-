# # For loop
#
# for i in [1, 2, 3, 4, 5]:
#     print("i =", i)
#
# for i in range(10):
#     print("value is :", i)
#
# # Truncate the decimal values from float values
# value = 12.6789
# print("Truncate 2 digit decimal is {:.2f}".format(value))

money = input(" How much money you investment: ")
interest = input("Enter the interest  rate :")
year = int(input("How many years you invest it:"))
money = float(money)
interest = float(interest) * 0.01
for i in range(1, (year+1)):
    money = money + (money * interest)

print("Investment after {} years is {:.2f}".format(year, money))


# calculation for the computer
#  1- exponent and root extraction
#  2 - multiplication and division
#  3 - addition and subtraction
