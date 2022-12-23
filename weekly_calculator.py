

def calculate_hourly_wage():
    #occasional print line statement for user clarity
    print()
    
    #asking for user input of how many hours they worked this week
    hour = input('How many hours did you work this week? ')
    print('------------------------------------------------')
    

    #this try-except is determining if the hour argument can be casted as a float or isn't negative
    #if value is negative or not able to be a float, program will end
    try:
        hour = float(hour)
        if hour < 0:
            print('You cannot work negative hours.')
            quit()
    except ValueError:
        print('Error, please enter a positive, rational number.')
        quit()

    #asking for user input of how much they make an hour
    rate = input('What is your hourly rate? ')
    print('------------------------------------------------')
      

    #this try-except is determining if the hour argument can be casted as a float or isn't negative
    #if value is negative or not able to be a float, program will end
    try:
        rate = float(rate)
        if rate < 0:
            print('You cannot make negative wages.')
            quit()
    except ValueError:
        print('Error, please enter a positive, rational number.')
        quit()

    #calculating OT pay based on time & a half
    if hour > 40:
        overtime = hour - 40
        OT_wages = round(40 * rate + overtime * rate * 1.5, 2)
        print(f'Your weekly total wage (including OT) = ${OT_wages}')
        print()
        return OT_wages

    #calcuating regular pay
    else:
        wages = round(40 * rate, 2)
        print(f'Your total weekly wage = ${wages}')
        print()
        return wages


if __name__ == '__main__':
    calculate_hourly_wage()