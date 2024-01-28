# Utils/distance_fee.py
'''
This function calculates the delivery fee based on the distance.
The initial fee for the first 1 km of delivery is 2€.
There is an additional fee of 1€ for every 500 meters beyond the first 1 km.
It ensures that the minimum fee is 1€.
'''
def calc_delivery_distance_fee(distance: int):

    # Initial fee for the first 1000 meters of delivery
    initial_fee = 2.0  # 2€

    # Additional fee for every 500 meters beyond the first 1 km
    additional_fee_500 = 1.0  # 1€

    # Calculate the additional distance beyond the first 1 km
    # Ensure it's non-negative. Example 2690 - 1000 = 1690. if it is less than 1000, additional_distance = 0. 
    # if it is negative, additional_distance = 0
    additional_distance = max(0, distance - 1000)  
    print("Additional distance in meters: " + str(additional_distance)) # for debugging

    # Calculate the additional fee based on 500-meter increments
    # Example (1690 + 499) // 500 * 1.0 = 4.0. so it means there is 4 times 500 meters beyond the first 1 km
    additional_fee = (additional_distance + 499) // 500 * additional_fee_500 
    print("Additional distance fee: " + str(round(float(additional_fee), 2))) # for debugging

    # Calculate the total delivery fee
    total_fee = initial_fee + additional_fee # Example 2.0 + 4.0 = 6.0
    print("Total distance fee: " + str(round(float(total_fee), 2))) # for debugging

    # Ensure the minimum fee is 1€
    if total_fee < 1.0:
        total_fee = 1.0

    return total_fee 