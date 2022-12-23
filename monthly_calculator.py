from weekly_calculator import calculate_hourly_wage

def calculate_monthly_wage():
    monthly_wages = calculate_hourly_wage() * 4
    print('------------------------------------------------')
    print(f'Your total monthly wage = ${monthly_wages}')
    print()
    return monthly_wages



if __name__ == '__main__':
    calculate_monthly_wage()