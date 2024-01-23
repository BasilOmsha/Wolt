class Cart:
    def __init__(self, cart_value: int, delivery_distance: int, number_of_items: int, time: str):
        # types are specified after the variable name using a colon to better document the code
        # Constructor to initialize the object
        # 'self' refers to the current instance of the class
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time

    @classmethod 
    def from_json(cls, json_data):
        # Class method to create an instance of OrderData from JSON data
        # 'cls' refers to the class itself, used to create a new instance
        return cls(
            json_data.get('cart_value', 0), #Expected to be an integer
            json_data.get('delivery_distance', 0), 
            json_data.get('number_of_items', 0),
            json_data.get('time', '') #Expected to be a string
        )

    def to_dict(self):
        # Method to convert the OrderData object to a dictionary helpful for JSON conversion because JSON can only contain string keys. Also, it is good for validation for example, if you want to check if a key exists in the JSON data, you can check if the key exists in the dictionary.
        # 'self' is used to access the attributes of the current instance
        return {
            "cart_value": self.cart_value,
            "delivery_distance": self.delivery_distance,
            "number_of_items": self.number_of_items,
            "time": self.time
        }
