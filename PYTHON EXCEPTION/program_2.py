
try:

    # division
    num_1 = int(input("Please enter num 1: "))
    num_2 = int(input("Please enter num 2: "))
    div = num_1 / num_2
    print(f"Division of {num_1} and {num_2} is {div}")

    # list program
    list_var = [56,43,55,11,87]
    print(f"value at 0 position is {list_var[0]}")
    print(f"value at 1 position is {list_var[1]}")
    print(f"value at 2 position is {list_var[2]}")
    print(f"value at 3 position is {list_var[3]}")
    print(f"value at 4 position is {list_var[4]}")
    print(f"value at 5 position is {list_var[5]}")    

except ZeroDivisionError as e:
    print("value of num 2 should not ve zero")
except IndexError as e:
    print(f"Size of list is {len(list_var)} and you are trying to access index which is not present")
except Exception as e:
    print("Error Traceback:",e.__traceback__.tb_lineno)
    print("Error Type: ",type(e).__name__)
    print("Error Message: ",e)