while True:
    print("\n----- MENU -----")
    print("1. Square of a number")
    print("2. Cube of a number")
    print("3. Exit")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        num = int(input("Enter a number: "))
        square = num * num
        print("Square of", num, "is:", square)

    elif choice == 2:
        num = int(input("Enter a number: "))
        cube = num * num * num
        print("Cube of", num, "is:", cube)

    elif choice == 3:
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice! Please enter 1,2,3")