# Utils/items_count_fee.py
'''
This function calculates the delivery fee based on the number of items.
If the number of items is less than 5, there is no surcharge.
If the number of items is equal or greater than 5, there is a surcharge of 0.5€ per item.
If the number of items is equal or greater than 13, there is one 'bulk surcharge of 1.2€ 
to all the items in addtion to the 0.5€ if each item.
'''
def calc_items_count_fee(items: int):

    # minumum number of items to add a surcharge of 0.5€ per item needs to surpass the threshold
    threshold = 4 # 5 items 

    # minimum number of items to add a bulk surcharge of 1.2€ needs to surpass the threshold2
    threshold2 = 12 # 13 items

    # 50 cents surcharge for every item equal or beyond the threshold
    additional_fee_per_item = 0.5 # 0.5€

    # 1.2€ surcharge for all the items beyond the threshold2
    bulk_surcharge = 1.2 # 1.2€

    # Calculate the additional items beyond the threshold
    # if it is negative, additional_items = 0, which means the number of items is less than the threshold
    # max function returns the largest of the given items. If result is negative, we set it to 0 then return it.   
    additional_items = max(0, items - threshold)
    print("Additional items: " + str(additional_items)) # for debugging

    bulk_items = max(0, items - threshold2)
    print("Bulk items: " + str(bulk_items)) # for debugging
    
    # checking if there are additional items
    if additional_items !=0:
        # adding the surcharge for every item beyond the threshold
        additional_fee_per_item = additional_items * additional_fee_per_item
        print("Total sum of additional fee per item: " + str(additional_fee_per_item)) # for debugging

        # checking if there are bulk items (13 items or more)
        if bulk_items !=0:
            # adding one bulk surcharge for all the items beyond the threshold2
            bulk_surcharge = additional_fee_per_item + bulk_surcharge
            print("Bulk surcharge + total: " + str(bulk_surcharge)) # for debugging
            return bulk_surcharge
        else:
            # returning the surcharge for every item beyond the threshold when there aren't bulk items
            return additional_fee_per_item

    # no surcharge
    return 0

