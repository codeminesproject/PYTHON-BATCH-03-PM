try:

    # division
    num_1 = int(input("Please enter num 1: "))
    num_2 = int(input("Please enter num 2: "))
    div = num_1 / num_2
    print(f"Division of {num_1} and {num_2} is {div}") 

except Exception as e:
    print("Error Traceback:",e.__traceback__.tb_lineno)
    print("Error Type: ",type(e).__name__)
    print("Error Message: ",e)
finally:
    print("Welcome to CodeMines Computer")

