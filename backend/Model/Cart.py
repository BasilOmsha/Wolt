from helpers.validations import validate_integer, validate_time
'''
This class represents a cart object.
It has the following attributes:
- cart_value: int
- delivery_distance: int
- number_of_items: int
- time: str

It has the following methods:
- __init__(self, cart_value: int, delivery_distance: int, number_of_items: int, time: str). this is the constructor and it initializes the object.
it can be use as follows:
    cart = Cart(2000, 2235, 4, "2021-01-01T15:00:00Z")
- from_json(cls, json_data) this is a class method that creates an instance of Cart from JSON data. it can be used as follows:
    cart = Cart.from_json(json_data)

Valiation rules:
- Cart_value, delivery_distance, and number_of_items must be valid integers and non-negative.
- If they are number strings, they will be converted to integers. float  is allowed
- Time must be a valid date, a datetime object, or a string.

Imports:
- from helpers.validations import validate_integer, validate_and_convert_time. These are helper functions to validate the data.

Validation is done at this level to ensure that the data is valid before it's passed to the controller and
its underline utilities.
'''
class Cart:
    def __init__(self, cart_value: int, delivery_distance: int, number_of_items: int, time: str):
        # types are specified after the variable name using a colon to better document the code
        # Constructor to initialize the object
        # 'self' refers to the current instance of the class

        # Ensure that 'cart_value', 'delivery_distance', and 'number_of_items' are valid integers and not negative
        self.cart_value = validate_integer(cart_value, "cart_value")
        self.delivery_distance = validate_integer(delivery_distance, "delivery_distance")
        self.number_of_items = validate_integer(number_of_items, "number_of_items")
        self.time = validate_time(time) # Ensure that 'time' is a valid date string
    
    @classmethod 
    def from_json(cls, json_data):
        # Class method to create an instance of Cart from JSON data
        # 'cls' refers to the class itself, used to create a new instance
        # Ensure that cart_value is a valid integer
        
        # Ensure that 'cart_value', 'delivery_distance', and 'number_of_items' are valid integers and not negative
        cart_value = validate_integer(json_data.get('cart_value'), "cart_value")
        delivery_distance = validate_integer(json_data.get('delivery_distance'), "delivery_distance")
        number_of_items = validate_integer(json_data.get('number_of_items'), "number_of_items")
        # Validate and convert "time" to a string if it's a valid date string
        time = validate_time(json_data.get('time', ''))
        # create and return an instance of Cart
        return cls(
            # json_data.get('cart_value', 0), #Expected to be an integer
            cart_value,
            # json_data.get('delivery_distance', 0), 
            delivery_distance,
            # json_data.get('number_of_items', 0),
            number_of_items,
            # json_data.get('time', '') #Expected to be a string
            time
        )