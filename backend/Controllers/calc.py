# controller/calc.py
from flask import *
from Model.Cart import Cart 


def calc():

    try:
        # Get the request body data
        req_data = request.get_json()
        print(req_data) # for debugging. it prints the request body data in the terminal

        # instance of the Cart model
        cart_data = Cart.from_json(req_data) # it converts the request body data to a Cart object

        value = cart_data.cart_value # gets the value from the Cart object json_data. cart_value
        print(value) # for debugging. 
        distance = cart_data.delivery_distance # delivery_distance
        print(distance)
        items = cart_data.number_of_items # number_of_items
        print(items)
        time = cart_data.time # time
        print(time)

        # if the cart value is less than 10€, a small order surcharge is added to the delivery price. 
        #The surcharge is the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will be 1.10€.
        if value < 10:
            surcharge = 10 - value

        # A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters 
        # that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
        # Example 1: If the delivery distance is 1499 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
        # Example 2: If the delivery distance is 1500 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
        # Example 3: If the delivery distance is 1501 meters, the delivery fee is: 2€ base fee + 1€ for the first 500 m + 1€ for the second 500 m => 4€
        # if distance <= 1000:
        #     delivery_fee = 2
        # elif distance > 1000:
        #     additional_distance = distance - 1000
        #     print('addOne ' + str(additional_distance))
        #     if additional_distance <= 500:
        #         delivery_fee = 2 + 1
        #     elif additional_distance > 500:
        #         print(additional_distance)
        #         additional_distance2 = additional_distance / 500
        #         print('addTwo ' + str(additional_distance2))
        #         delivery_fee = 2 + 1 + additional_distance2

        # print(int(delivery_fee))
            
        # responseObj = {
        #     "delivery_fee": int(delivery_fee)
        # }

        # return responseObj, 200 # 200 OK
            
         # Initial fee for the first 1 km (1000 meters)
        initial_fee = 2.0  # 2€

        # Additional fee for every 500 meters beyond the first 1 km
        additional_fee_per_500_meters = 1.0  # 1€

        # Calculate the additional distance beyond the first 1 km
        additional_distance = max(0, distance - 1000)  # Ensure it's non-negative

        # Calculate the additional fee based on 500-meter increments
        additional_fee = (additional_distance + 499) // 500 * additional_fee_per_500_meters

        # Calculate the total delivery fee
        total_fee = initial_fee + additional_fee

        # Ensure the minimum fee is 1€
        if total_fee < 1.0:
            total_fee = 1.0

        responseObj = {
            "delivery_fee": int(total_fee)
        }

        return responseObj, 200 # 200 OK
    
    except Exception as e:
        # Return error message if the request body is not a valid JSON
        return jsonify({"error": str(e)}), 400 # 400 Bad Request
    