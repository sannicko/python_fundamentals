# This code represents a theater ticket center program that allows users to book seats. It provides options to book a single seat, book multiple seats in a row, or book any available seat in the back row. The program displays the current seating arrangement and allows users to make their selections. Overall, this code allows users to interact with a theater ticket center, view the seating arrangement, and book seats based on their preferences using 2D list . 


# initialize 2D list to store seat data
seats = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


def display_seats():
    print("   0  1  2  3  4  5  6  7")
    for i, row in enumerate(seats):
        row_data = [str(seat) if seat == 0 else "X" for seat in row]
        print(f"{i}  {'  '.join(row_data)}")


def book_single_seat(row, col):
    # check if the seat is available
    if seats[row][col] == 0:
        # reserve the seat
        seats[row][col] = 1
        print(f"Great! We reserved seat {col} in row {row} for you [Checkmark]")
    else:
        print(f"Sorry, this seat {col} in row {row} is taken [X] please select another one")


def book_seat_range(row, num_seats):
    ptr1 = 0
    ptr2 = num_seats
    while ptr2 <= len(seats[row]):
        # check if the consecutive seats are available
        if seats[row][ptr1:ptr2] == [0] * num_seats:
            # reserve the seats
            seats[row][ptr1:ptr2] = [1] * num_seats
            print(f"Great! We reserved seats {ptr1} through {ptr2 - 1} in row {row} for you [Checkmark]")
            return
        ptr1 += 1
        ptr2 += 1
    print(f"Sorry, we were unable to book {num_seats} tickets in row {row} [X]")


def book_backrow():
    backrow = seats[4]
    for i in range(len(backrow)):
        if backrow[i] == 0:
            # reserve the backrow seat
            backrow[i] = 1
            print(f"Great! We reserved backrow seat {i} for you [Checkmark]")
            return
    print("Sorry, the backrow is full [X]")


# menu
print("* Theater Ticket Center *")
print(" Please select one of the below choices:")
print("1: Book a single seat")
print("2: Book multiple seats in a row")
print("3: Book a backrow seat")
print("4: Exit")

while True:
    choice = input("\nSelect an option (1-4) or enter 'exit' to exit: ")

    # option 1: book a single seat
    if choice == "1":
        display_seats()
        row = int(input("Enter a row number (0-4): "))
        col = int(input("Enter a column number (0-7): "))
        book_single_seat(row, col)

    # option 2: book multiple seats in a row
    elif choice == "2":
        display_seats()
        row = int(input("Enter a row number (0-4): "))
        num_seats = int(input("Enter number of seats (1-8): "))
        book_seat_range(row, num_seats)

    # option 3: book any backrow seat
    elif choice == "3":
        display_seats()
        book_backrow()

    # option 4: exit
    elif choice == "4":
        break

    elif choice.lower() == "exit" or choice.lower() == chr(27):
        print("Exiting the program...")
        break

    elif choice == "":
        print("Please enter a valid option 1-2-3-4 or enter 'exit' to exit.")

    else:
        print("Invalid input. Please enter a valid option.")

print("Thank you for coming!")
