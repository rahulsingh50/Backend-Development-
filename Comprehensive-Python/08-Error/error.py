input = input("Enter the number :")
# print(float(input))


# try:
#     print(float(input))
# except :
#     print("Some thing went Wrong")  # vary genric not allowed in code


try:
    print(float(input))
except Exception as e:
    print(e)