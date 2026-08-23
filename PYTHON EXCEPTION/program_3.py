
try:

    # division
    num_1 = int(input("Please enter num 1: "))
    if num_1<=0:
        raise ValueError("value of num 1 should not be zero")

    num_2 = int(input("Please enter num 2: "))
    if num_2<=0:
        raise ValueError("value of num 2 should not be zero")

    div = num_1 / num_2
    print(f"Division of {num_1} and {num_2} is {div}")
  
except Exception as e:
    print("Something went wrong! Please try again")

    error_message = "\n--------------------------------------------------------"
    error_message += "\nError Traceback: "+ str(e.__traceback__.tb_lineno)
    error_message += "\nError Type: "+ type(e).__name__
    error_message += "\nError Message: "+ str(e)
    error_message += "\n--------------------------------------------------------"
    file = open("log.txt","a")
    file.write(error_message)
    