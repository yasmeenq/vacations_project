# if type(lst) is not list:
#     raise ValueError("Parameter must be list type.")
# if len(lst) == 0:
#     raise IndexError("List cannot be empty.")

# try:
#     print(f"digits count = {count_digits(-47)}")  #2
#     print(f"digits count = {count_digits(0)}")  #0
#     print(f"digits count = {count_digits(7865)}")  #4
#     #other examples:
#     print(count_digits("Banana"))  #Value Error: Parameter must be integer.
#     print(count_digits(2.5)) # Value Error: Parameter must be integer.(because it's float not int)

# except ValueError as e:
#     print("Value Error:", e)
# except Exception as e:
#     print("General Error:", e)

# print("==========================================")

# #d-e
# from handle_same_digits import same_digits

# try:
#     print(same_digits(999))  #True
#     print(same_digits(1))  #True
#     #other examples:
#     print(count_digits("Banana"))  #Value Error: Parameter must be integer.
#     print(count_digits(2.5)) # Value Error: Parameter must be integer.(because it's float not int)

# except ValueError as e:
#     print("Value Error:", e)
# except Exception as e:
#     print("General Error:", e)

# print("==========================================")

# #f-g
# from handle_list import average_and_sum

# try:
#     print(average_and_sum([2,3,4]))
#     #other examples:
#     print(average_and_sum("cat")) #Value Error: parameter must be a list type(because it's string not list)
#     print(average_and_sum((1,2,3))) #Value Error: Parameter must be list type(because it's tuple not list)
#     print(average_and_sum([])) #Index Error: List cannot be empty.

# except ValueError as e:
#     print("Value Error:", e)
# except IndexError as e:
#     print("Index Error:", e)
# except Exception as e:
#     print("General Error:", e)

