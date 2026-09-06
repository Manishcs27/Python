# def calculate_total(exp):
#     total = 0
#     for item in exp:
#         total += item
#     return total
#
# x_list = [1,2,3,4,5,6,7,8,9,10]
# y_list = [1,2,3,4,5,6,7,8,9,10]
#
# x_expenses = calculate_total(x_list)
# y_expenses = calculate_total(y_list)
#
# print("x expenses is",x_expenses)
# print("y expenses is",y_expenses)

# total = 0
# for x in x_list:
#     total += x
# print("total of x",total)
# for y in y_list:
#     total += y
# print("total of y",total)

total=0
def sum(a,b=0):
    print("a:",a)
    print("b:",b)
    total = 0
    total = a+b
    return total

n=sum(6)
print("total is",n)
print("total outside function is:",total)