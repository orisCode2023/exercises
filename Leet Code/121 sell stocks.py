from operator import index


def profit_day_for_stocks():
    stocks = [7,1,2,3,4,5,6]
    minimum_number = None
    maximum_number = 0
    for i in stocks:
        if minimum_number is None or minimum_number > i:
            minimum_number = i
        potential_buy = index(minimum_number)

        while potential_buy <= len(stocks):
            if maximum_number < i:
                maximum_number = i
            potential_buy += 1

    return maximum_number - minimum_number



print(profit_day_for_stocks())



