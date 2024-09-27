# Function for table generator
def table(n):
    print()
    print(f"Table of {n}")
    for i in range(1, 11):
        print(n*i)

# Start creating table
while True:
    #  Ask user for input
    print("Which type of table do you want to print?")
    print("1 :    Range of Table")
    print("2 :    Specific Table")
    
    # Error Handling for wrong input
    try:
        result = int(input("Enter your choice: "))
    except  ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    # Generating range of table
    if result == 1:
        start = int(input("Please give me a starting number: "))
        end = int(input("Please give me a ending number: "))
        for i in range(start, end+1):
            table(i)
        print("Do you want to continue?")
        ans = input("Enter yes or no: ")
        if ans.lower() == "no":
            break
        else:
            continue
    
    # Generating specific table
    elif result  == 2:
        n = int(input("Please give me a number: "))
        table(n)
        print("Do you want to continue?")
        ans = input("Enter yes or no: ")
        if ans.lower() == "no":
            print("Thank you for using table generator.")
            break
        else:
            continue
        
    # Error Handling for wrong input
    # else:
    #     break


