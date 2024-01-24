# Utils/fee_limit.py
'''
this function checks if the total fee is greater than 15€, then it sets the total fee back to 15€.
if the total fee is not greater than 15€, it returns the total fee.
if the value is greater than or equals 200€, the total fee is 0€.
'''
def calc_fee_limit(total_fee: int, value: int):

    # threshold for the delivery fee
    max_delivery_fee = 15 # 15€

    # checks if the total fee is greater than the threshold. if it is not greater than the threshold, limit_diff = 0.
    limit_diff = max(0, total_fee - max_delivery_fee) 
    print("Max limit difference: " + str(round(float(limit_diff), 2))) # for debugging

    if limit_diff != 0 and value < 200:
        # if the total fee is greater than the threshold, set total fee back to 15€.
        total_fee = 15
        print("Total fee is greater than 15€. Set total fee back to 15€: " + str(round(float(total_fee), 2)))
        return total_fee
    elif value >= 200:
        # if the total fee is not greater than the threshold, return the total fee.
        total_fee = 0
        print("Cart value is over 200. Free delivery: " + str(round(float(total_fee), 2)))
        return total_fee


    print("Total fee is not greater than 15€ amd value < 200€. Return total fee: " + str(round(float(total_fee), 2)))
    return total_fee