# controller/calc.py
from flask import *
from Model.Cart import Cart 
from Utils.distance_fee import calc_delivery_distance_fee
from Utils.cart_value_fee import calc_cart_value_surcharge
from Utils.items_count_fee import calc_items_count_fee
from Utils.fee_limit import calc_fee_limit
from Utils.time_fee import calc_time_fee
'''
This function calculates the delivery fee based on:
- The value of the cart
- The distance of the delivery
- The number of items
- The day and time of the delivery
To calculate the delivery fee, it uses the following functions:
- calc_cart_value_surcharge(value: int) 
- calc_delivery_distance_fee(distance: int) 
- calc_items_count_fee(items: int) -> int
- calc_fee_limit(total_fee: int, value: int) 
- calc_time_fee(time: str, total_fee: int)
Distance is in meters. Value is in cents. Time is in the format "YYYY-MM-DDTHH:MM:SSZ".
However, the value is converted to euros for better readability. After the calculations, 
the value is converted back to cents and returned to the client.
Time is converted to UTC. Format: "YYYY-MM-DD HH:MM:SS".
'''
def calc():

    try:
        # Get the request body data
        req_data = request.get_json()
        print(req_data) # for debugging.

        # instance of the Cart model
        cart_data = Cart.from_json(req_data) # it converts the request body data to a Cart object

        value = round(float(cart_data.cart_value / 100),2) # gets the value from the Cart object json_data. cart_value is in cents, so we divide it by 100 to get the value in euros
        print(value) # for debugging. 
        distance = cart_data.delivery_distance # delivery_distance
        print(distance)
        items = cart_data.number_of_items # number_of_items
        print(items)
        time = cart_data.time # time
        print(time)

        cart_value_surcharge = calc_cart_value_surcharge(value) # calculates surcharge if the value is less than 10€

        distance_cart_value = calc_delivery_distance_fee(distance) # calculates the delivery fee based on the distance

        items_cart_value = calc_items_count_fee(items) # calculates the delivery fee based on the number of items

        pre_total_fee = cart_value_surcharge + distance_cart_value + items_cart_value # calculates the total fee
        print("pre_total_fee: " + str(round(float(pre_total_fee), 2))) # for debugging

        time_fee = calc_time_fee(time, pre_total_fee) # checks if a surge is needed for the total, based on the day and time
        print("Total + time_fee: " + str(round(float(time_fee), 2))) # for debugging

        total_fee =  calc_fee_limit(time_fee, value) # checks if the total fee is greater than 15€

        responseObj = {
            # "cart_value_surcharge": round(float(cart_value_surcharge), 2), # for debugging
            # "calculated distance": round(float(distance_cart_value), 2), # for debugging
            # "calculated items": round(float(items_cart_value), 2), # for debugging
            # "time_fee": round(float(time_fee), 2), # for debugging
            "delivery_fee": int(total_fee * 100) # returns the delivery fee in cents,
        }

        return jsonify(responseObj), 200 # 200 OK
    
    except Exception as e:
        # Return error message if the request body is not a valid JSON
        return jsonify({"error": str(e)}), 400 # 400 Bad Request
    