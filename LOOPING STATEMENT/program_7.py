

is_continue = "y"

while is_continue=="y":
    num = int(input("Please enter num: "))

    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

    is_continue = input("Press y to continue, otherwise press anything to stop: ")