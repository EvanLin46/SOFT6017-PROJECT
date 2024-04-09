# Evan Linares 


def menu(ticket_type = "", number_of_people = 0, fine_dining_pass = ""):
    
    #initialisation
    choice = 0

    print("MUSIC FARM FESTIVAL")
    print("===================")
    print("1. Make a Booking")
    print("2. Review Bookings")
    print("3. Exit\n")
    
    while not choice in (1, 2, 3):
        choice = int(input("=>"))

    print("\n")

    if choice == 1:
        ticket_type, number_of_people, fine_dining_pass = choice_1()
        
        menu(ticket_type, number_of_people, fine_dining_pass)
    elif choice == 2:
        choice_2()
        menu(ticket_type, number_of_people, fine_dining_pass)
        
    else:
        choice_3(ticket_type, number_of_people, fine_dining_pass)



#choice 1
def choice_1():
    print("MUSIC FARM FESTIVAL (BOOKING)")
    print("=============================\n")

    f_name_control = False
    while f_name_control == False:
        name = str(input("Enter your name (name surname (15 characters max))=> "))
        f_name_control = family_name_control(name)
    
    digit = False

    while not digit:
        phone_number = str(input("Enter your phone number => "))
        digit = phone_number.isdigit()

    
    
    print("Choose a ticket type :")
    print("1. Day 1")
    print("2. Day 2")
    print("3. Weekend-Camp\n")

    ticket_type_choice = int(input("=>"))

    if ticket_type_choice == 1:
        ticket_type = "Day1"

    elif ticket_type_choice == 2:
        ticket_type = "Day2"

    elif ticket_type_choice == 3:
        ticket_type = "Weekend-Camp"

    number_of_people = 0
    while not 0 < number_of_people <= 4:
        number_of_people = int(input("How many people in your group (4 max)? "))
    
    fine_dining_pass = "a"
    
    # total cost calculation
    while not fine_dining_pass.upper() in ("Y", "N") and ticket_type_choice in (1, 2):
        fine_dining_pass = str(input("Do you require a dining pass (Y/N)? "))

    if ticket_type_choice == 1 or ticket_type_choice == 2:
        total_cost = 850*number_of_people
        if fine_dining_pass.upper() == "Y":
            total_cost += 20*number_of_people
    
    else:
        total_cost = 2000*number_of_people
        fine_dining_pass = "Y"


    print("\nBooking Details")
    print("---------------\n")

    print(f"Name:           {name}")
    print(f"Ticket Type:    {ticket_type}")
    print(f"No of People:   {number_of_people}")
    print(f"Fine Dining:    {fine_dining_pass.upper()}")
    print(f"Total Cost:     €{total_cost}")

    enter_to_continue = str(input("Press Return to continue: "))

    #client file creation
    create_client_file(name, phone_number, ticket_type, number_of_people, fine_dining_pass, total_cost)


    return ticket_type, number_of_people, fine_dining_pass


def family_name_control(complet_name):
    
    data = complet_name.split(" ")
    if len(data) != 2 or len(data[1]) > 15:
        return False
    else: return True


def create_client_file(name, phone_number, ticket_type, number_of_people, fine_dining_pass, total_cost):
    
    name = name.replace(" ", "_")

    file = open(name+".txt", "w")

    file.write(f"Type of ticket(s) bought : {ticket_type}\n")
    file.write(f"Phone number : {phone_number}\n")
    file.write(f"Number of people : {number_of_people}\n")
    file.write(f"Total Cost : €{total_cost}\n")
    
    if fine_dining_pass.upper() == "Y":
        file.write(f"Dining Pass : Yes")
    
    else: file.write(f"Dining Pass : No")

    file.close()

def file_sales_update(filename, ticket_type, number_of_people):

    file = open(filename, "r")

    new_lines = []

    lines = file.readlines()

    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines.append(data) 

    #Day 1
    if ticket_type == "Day1":
        int_val = int(new_lines[0][3])
        int_val += number_of_people
        new_lines[0][3] = str(int_val)
        
    
    #Day2
    elif ticket_type == "Day2":
        int_val = int(new_lines[1][3])
        int_val += number_of_people
        new_lines[1][3] = str(int_val)
        

    #Weekend-Camp
    else:
        int_val = int(new_lines[2][3])
        int_val += number_of_people
        new_lines[2][3] = str(int_val)


    file.close()
    #rewriting the file
    file = open(filename, "w")

    count_last_line = 0
    for line in new_lines:
        count = 0
        for data in line:
            if count <3:
                file.write(data+",")
            else:
                file.write(data)
            count+=1
        if not count_last_line == 2:
            file.write("\n")

        count_last_line +=1

    file.close()

def file_extras_update(filename, ticket_type, number_of_people):
    file = open(filename, "r")

    new_lines = []

    lines = file.readlines()

    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines.append(data)

    
    if ticket_type == "Day1":
        int_val = int(new_lines[0][1])
        int_val += number_of_people
        new_lines[0][1] = str(int_val)

    if ticket_type == "Day2":
        int_val = int(new_lines[1][1])
        int_val += number_of_people
        new_lines[1][1] = str(int_val)

    file.close()
    #rewriting the file
    file = open(filename, "w")

    count_last_line = 0
    for line in new_lines:
        count = 0
        for data in line:
            if count <1:
                file.write(data+",")
            else:
                file.write(data)
            count+=1
        if not count_last_line == 1:
            file.write("\n")

        count_last_line +=1

    file.close()
        
#choice 2
def choice_2():
    
    day1_data, day2_data, weekend_data, dining_pass_day1, dining_pass_day2 = file_data_recovery("Sales_2024.txt", "Extras.txt")

    print("MUSIC FARM FESTIVAL - SUMMARY")
    print("==============================")

    print(f"Day 1                {day1_data}")
    print(f"Day 2                {day2_data}")
    print(f"Weekend_Camp         {weekend_data}\n")
    print(f"Fine Dining Day 1    {dining_pass_day1}")
    print(f"Fine Dining Day 2    {dining_pass_day2}\n")

    enter_to_continue = str(input("Press Return to continue: "))


def file_data_recovery(filename1, filename2):
    
    file1 = open(filename1, "r")
    file2 = open(filename2, "r")

    #file 1
    new_lines_1 = []
    lines_1 = file1.readlines()

    for line in lines_1:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines_1.append(data) 


    day1_data = int(new_lines_1[0][3])
    day2_data = int(new_lines_1[1][3])
    weekend_data = int(new_lines_1[2][3])


    #file 2
    new_lines_2 = []
    lines_2 = file2.readlines()

    for line in lines_2:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines_2.append(data) 

    dining_pass_day1 = int(new_lines_2[0][1])
    dining_pass_day2 = int(new_lines_2[1][1])

    return day1_data, day2_data, weekend_data, dining_pass_day1, dining_pass_day2

#choice 3
def choice_3(ticket_type, number_of_people, fine_dining_pass):
    
    #file updating ----------------------------------
    file_sales_update("Sales_2024.txt",ticket_type, number_of_people)

    if not ticket_type == "Weekend-Camp" and fine_dining_pass.upper() == "Y":

        file_extras_update("Extras.txt", ticket_type, number_of_people)


    print("Your reservation has been saved.")



def main():
    menu()


if __name__ == "__main__":
    main()

