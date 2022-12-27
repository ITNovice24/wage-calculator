

def calculate_hourly_wage():
    #occasional print line statement for user clarity
    print()
    

    #this initial conditional will determine how the paycheck is calculated
    number_of_hours = input('Did you work the same number of hours each week this month? \nYes/No? ')
    noh = number_of_hours.upper()

    if noh == 'YES' or noh == 'Y':
        #asking for user input of how many hours they worked this week
        hour = input('How many hours did you work this week? ')
        print('------------------------------------------------')
        
        #this try-except is determining if the hour argument can be casted as a float or isn't negative
        #if value is negative or not able to be a float, program will end
        try:
            hour_f = float(hour)
            if hour_f < 0:
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

    
        #calculating regular pay
        wages = round(hour_f * rate, 2)
        print(f'Your total weekly wage = ${wages}')
        print(f'Your total monthly wage = ${wages * 4}')
       
        
    
    
    elif noh == 'NO' or noh == 'N': 
        which_week = input('Which week of the month is this for you? \n 1, 2, 3, 4? ')
        wages_list = []
        
        #looping through how many weeks the user has worked thus far
        for i in range(1, int(which_week) + 1):
            print(f'For week {i}: ')
            hour = input('How many hours did you work this week? ')
            
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
            
            
            
            rate = input('What is your hourly rate? ')
            
            
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
            
            print('------------------------------------------------')
            
      
            #calcuating regular pay
            wages = round(hour * rate, 2)
            wages_list.append(wages)
            print(f'Your week {i} wage = ${wages}')
            print()
    
              
        diff_week_wages = sum(wages_list)
        print(f'Your total wages are: ${diff_week_wages}')
    else:
        print('You entered an invalid value. Re-start program.')
        quit()   
            






if __name__ == '__main__':
    calculate_hourly_wage()