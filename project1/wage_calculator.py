def wage_calculator():
    """This function takes no arguments"""
    hour = input('How many hours?')

    try:
        hour = float(hour)
        if hour < 0:
            print('You cannot work negative hours.')
            quit()
    except ValueError:
        print('Error, please enter a positive, rational number.')
        quit()

    rate = input('What is your hourly rate?')

    try:
        rate = float(rate)
        if rate < 0:
            print('You cannot make negative wages.')
            quit()
    except ValueError:
        print('Error, please enter a positive, rational number.')
        quit()

    if hour > 40:
        overtime = hour - 40
        wages = 40 * rate + overtime * rate * 1.5
        print(f'Your total wages + OT = ${wages}')

    else:
        wages = 40 * rate
        print(f'Your total wages = ${wages}')

if __name__ == '__main__':
    wage_calculator()
