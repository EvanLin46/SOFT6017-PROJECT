# Evan Linares 


def menu(ticket_type = "", number_of_people = 0, fine_dining_pass = ""):
    
    #initialisation
    choice = 0

    print("MUSIC FARM FESTIVAL")
    print("===================")
    print("1. Make a Booking")
    print("2. Review Bookings")
    print("3. Stats")
    print("4. Income")
    print("5. Exit\n")
    
    while not choice in (1, 2, 3, 4, 5):
        choice = int(input("=>"))

    print("\n")

    if choice == 1:
        ticket_type, number_of_people, fine_dining_pass = choice_1()
        
        menu(ticket_type, number_of_people, fine_dining_pass)
    elif choice == 2:
        choice_2()
        menu(ticket_type, number_of_people, fine_dining_pass)
    
    elif choice == 3:
        choice_3()
        menu(ticket_type, number_of_people, fine_dining_pass)

    elif choice == 4:
        choice_4()
        menu(ticket_type, number_of_people, fine_dining_pass)
    
    elif choice == 5:
        choice_5(ticket_type, number_of_people, fine_dining_pass)


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

    ticket_type_choice = 0
    while not ticket_type_choice in (1, 2, 3):
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

    groups_file_update(name, str(number_of_people))

    return ticket_type, number_of_people, fine_dining_pass



def groups_file_update(new_name, number_of_people):
    file = open("groups.txt", "r")

    new_lines = []

    lines = file.readlines()

    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines.append(data) 
    
    file.close()

    #adding the new datas 
    new_lines.append([new_name, number_of_people])

    #rewriting the file
    file = open("groups.txt", "w")

    for line in new_lines:
        count = 0
        for data in line:
            if count <1:
                file.write(data+",")
            else:
                file.write(data+"\n")
            count+=1

    file.close()

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
def choice_5(ticket_type, number_of_people, fine_dining_pass):
    
    #file updating ----------------------------------
    file_sales_update("Sales_2024.txt",ticket_type, number_of_people)

    if not ticket_type == "Weekend-Camp" and fine_dining_pass.upper() == "Y":

        file_extras_update("Extras.txt", ticket_type, number_of_people)


    print("Your reservation has been saved.")


def choice_3():
    names_list, numbers_list = read_groups_file()

    largest_group = numbers_list.index(max(numbers_list))

    print(f"The largest booking is by {names_list[largest_group]} and is for {numbers_list[largest_group]} people.")

    numbers_sum = sum(numbers_list)
    booking_average = numbers_sum/len(numbers_list)

    print(f"The average size is {booking_average} .\n\n")

    enter_to_continue = str(input("Press Return to continue: "))
    

def read_groups_file():
    file = open("groups.txt", "r")

    new_lines = []

    lines = file.readlines()

    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines.append(data) 
    
    file.close()

    names_list = []
    numbers_list = []

    for line in new_lines:
        names_list.append(line[0])
        numbers_list.append(int(line[1]))

    return names_list, numbers_list


def choice_4():
    sales_datas = read_sales_file()

    extras_datas = read_extras_file()
    
    total_day1 = 0
    total_day2 = 0
    total_weekend = 0
    total_fine_dining = 0

    total_current_income = 0

    count = 0
    for line in sales_datas:
        if count == 0:
            total_day1 += int(line[3])*850
        
        elif count == 1:
            total_day2 += int(line[3])*850

        else : total_weekend += int(line[3])*2000
        count += 1

    
    for line in extras_datas:
        total_fine_dining += int(line[1])*20

    total_current_income = total_day1 + total_day2 + total_weekend + total_fine_dining
    
    print(f"Total income = €{total_current_income}\n")

    breakdown = ""
    while not breakdown.upper() in ("Y", "N"):
        breakdown = str(input("Would you like to see a breakdown Y/N : "))

    if breakdown.upper() == "Y":
        print(f"Day 1 :     €{total_day1}")
        print(f"Day 2 :     €{total_day2}")
        print(f"Weekend Tickets :     €{total_weekend}")
        print(f"Fine Dining :   €{total_fine_dining}")
        print(f"Total : €{total_current_income}\n")

    enter_to_continue = str(input("Press Return to continue: "))

def read_sales_file():
    file = open("Sales_2024.txt", "r")

    new_lines = []

    lines = file.readlines()

    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines.append(data) 
    
    file.close()
    
    return new_lines

def read_extras_file():
    file = open("Extras.txt", "r")

    new_lines = []

    lines = file.readlines()

    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        if data != []:
            new_lines.append(data) 
    
    file.close()
    
    return new_lines

def main():
    menu()
    

if __name__ == "__main__":
    main()


