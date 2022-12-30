
def paycheck_calculator():       
    
    def calculate_pay(hour, rate):
        wages = round(hour * rate, 2)
        return wages


    def check_for_float(input):     
        try:
            value = float(input)
            if value < 0:
                print('You cannot have a negative value')
                quit()
            return value
        except ValueError:
            print('Error, please enter a number.')
            quit()


    hour = input('How many hours did you work this week? ')
    hour = check_for_float(hour)
    print('------------------------------------------------')
    rate = input('What is your hourly rate? ')
    rate = check_for_float(rate)
    print('------------------------------------------------')


    def check_for_hour_consistency():
        print()
        number_of_hours = input('Did you work the same number of hours each week this month? \nYes/No? ')
        print()
        noh = number_of_hours.upper()

        if noh == 'YES' or noh == 'Y':
            return
       
        elif noh == 'NO' or noh == 'N': 
            which_week = input('Which week of the month is this for you? \n 1, 2, 3, 4? ')
            wages_list = []
        
            for i in range(1, int(which_week) + 1):
                print()
                print(f'For week {i}: ')
                diff_hours = float(input('How many hours did you work this week? '))
                print()
                if diff_hours > 40:
                    ot_rate = (diff_hours - 40) * (rate * 1.5) 
                    wage = calculate_pay(40, rate) + ot_rate
                    wages_list.append(wage)
                    diff_week_wages = sum(wages_list)
                else:
                    wage = calculate_pay(diff_hours, rate)
                    wages_list.append(wage)
                    diff_week_wages = sum(wages_list)
            print(f'Your total wages are: ${diff_week_wages}')
            print()
            quit()
        else:
            print('You entered an invalid value. Re-start program.')
            quit()   


    def get_wages():
        wages = calculate_pay(hour, rate)
        return wages

    check_for_hour_consistency()
    print()
    print(f'Your total pay for the week was: ${get_wages()}')
    print(f'Your total monthly pay was ${get_wages() * 4}')
    print()


        
    
    
   
       




if __name__ == '__main__':
    paycheck_calculator()