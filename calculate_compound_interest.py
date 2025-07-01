INTEREST = 1 / 3

def get_next_month(fund, deposit):
    return (1 + INTEREST / 100) * fund + deposit

def get_year(fund, deposit):
    for i in range(1, 13):
        fund = get_next_month(fund, deposit)
    return fund

def get_5_years(fund, deposit):
    for i in range(5):
        fund = get_year(fund, deposit)

    return fund

print(get_5_years(5000, 1000))

# month2 = get_next_month(5000, 50)
# month3 = get_next_month(month2, 50)
# print("month 1 " , 5000)
# print("month 2 " , month2)
# print("month 3 " , month3)
