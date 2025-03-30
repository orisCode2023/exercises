"""

def calculate_discount():
    purchase_amount = float(input("Enter price "))
    is_member = bool(input("If you are member write True else press enter "))
    holiday_sale = bool(input("If there is sale write True else press enter "))
    coupon_code = input("If you have a coupon enter  the code else press enter ")
    purchase_count = int(input("Enter the number of time you purchased here "))
    #prefer_coupon = bool(input("If you prefer coupon over holiday sale write True else press enter "))
    minimum_price = 10.0
    discount = 0
    price_after_holiday = 0
    prise_after_coupon = 0
    prise_after_count_bigger_then_10 = 0
    prise_after_count_less_then_10 = 0
    final_price = 0

    if is_member:
        discount -= ((purchase_amount * 10) / 100)
        final_price = purchase_amount - discount
    print(f"The original price was {purchase_amount} the final price is {final_price} ")

    if holiday_sale and coupon_code:
        choice = int(input("press 1 to holiday discount or press 2 for coupon discount"))
        if choice == 1:
            print("You choose the holiday discount")
            if purchase_amount >= 100:
                price_after_holiday = purchase_amount - 20
                print(f"The original price was {purchase_amount} after the holiday discount the price is {price_after_holiday }")

            else:
                price_after_holiday = purchase_amount - 10
                print(f"The original price was {purchase_amount} after the holiday discount the price is {price_after_holiday }")

        else:
            print("You choose the coupon discount")
            prise_after_coupon = (purchase_amount * 10) / 100
            print(f"The original price was {purchase_amount} after the coupon discount the price is {prise_after_coupon}")


    if purchase_count >= 10:
        if holiday_sale:
            prise_after_count_bigger_then_10 -= ((price_after_holiday * 5) / 100)

calculate_discount()
"""

purchase_price = float(input("Enter price "))
percent_discount = 0
last_price = 0


def cal_discount_percent(price, discount):
    global last_price
    last_price = purchase_price - ((price * discount) / 100)
    print(f"The final price after discount is {last_price} ")
    return last_price


def is_member():
    member = bool(input("If you are a member in thr club write True else press enter"))
    return member


def discount_member():
    if is_member():
        global percent_discount
        percent_discount = 10
    return cal_discount_percent(purchase_price, percent_discount)


# print(discount_member())


def is_holiday_discount():
    discount = bool(input("If there is discount write True else press enter"))
    return discount


def is_coupon_code():
    code = bool(input("If there is coupon write True else press enter"))
    return code


def prefer_discount():
    if is_holiday_discount() and is_coupon_code():
        choice = int(input("Enter 1 to sale enter 2 for coupon"))
        if choice == 1:
            sale_holiday()
        else:
            discount_coupon()


def sale_holiday():
    if is_holiday_discount():
        if purchase_price > 100:
            global last_price
            last_price = purchase_price - 20
        else:
            last_price = purchase_price - 10
    return last_price


def discount_coupon():
    if is_coupon_code():
        global percent_discount
        percent_discount = 10
        return cal_discount_percent(purchase_price, percent_discount)


#print(discount_coupon())


def purchase_count():
    purchase = int(input("Enter the number of time you purchase in the store"))
    return purchase


def member_and_coupon():
    return cal_discount_percent(purchase_price, 10) - discount_coupon()

print(member_and_coupon())
