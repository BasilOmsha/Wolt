from datetime import datetime, timezone, timedelta
from dateutil import parser
'''
This function calculates the delivery fee based on the time.
If the delivery is on Friday between 15:00 and 19:00 UTC, there is a surcharge of 20%.
'''
def calc_time_fee(deliv_date: str, total: int):

    # print ("total13: " + str(total)) 
    # print("Raw deliv_date: " + deliv_date)  

    start_time = datetime.strptime("15:00", "%H:%M").time() # 15:00. strptime converts string to time
    end_time = datetime.strptime("19:00", "%H:%M").time() # 19:00

    try:
        # Parsing and setting time zone to UTC
        delivery_datetime = parser.isoparse(deliv_date).replace(tzinfo=timezone.utc)
        print("Delivery datetime (UTC): " + str(delivery_datetime)) # for debugging

        delivery_day = delivery_datetime.weekday() # get the day of the week from the date in number format. Monday = 0 and Sunday = 6
        print("Delivery day: " + str(delivery_day))

        delivery_time = delivery_datetime.time() # get the time from the datetime
        print("Delivery time: " + str(delivery_time))

        # check if the day is Friday 
        if delivery_day == 4 :
            print("It is Friday") 
            # check if the time is between 15:00 and 19:00 UTC
            if start_time <= delivery_time <= end_time: #
                print("It is between 15:00 and 19:00 UTC")
                rush_surcharge = total * 1.2 # 20% surcharge
                print("Total fee when day is Friday (UTC) and time between 15 and 19: " + str(round(float(rush_surcharge), 2)))
                return float(rush_surcharge)
        
        return float(total)
    
    except Exception as e:
        # Return error message if there's an exception
        return float(total)
