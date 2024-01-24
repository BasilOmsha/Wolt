# Utils/cart_value_fee.py
'''
This function calculates the surcharge if the value is less than 10€
which the difference between the threshold and the value.
'''
def calc_cart_value_surcharge(value: int):

    # threshold.
    threshold = 10 #10€

    # if value is greater than or equals the threshold, surcharge = 0. 
    # Also it ensures that surcharge is non-negative. Example: 10 - 5 = 5. if it is less than 10, surcharge is the difference. 
    # if it is negative, surcharge = 0 which means the value is greater than the threshold.
    surcharge = max(0, threshold - value) 
    print("Value Surcharge: " + str(round(float(surcharge), 2))) # for debugging


    return surcharge 