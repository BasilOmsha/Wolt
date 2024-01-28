import unittest
from datetime import datetime
from server import app
'''
test only preformed on cart_value and time. 
Beacause delivery_distance and number_of_items are integers and the validation is the same as for the cart_value.
'''
class TestCalcFunction(unittest.TestCase):
    
    def setUp(self):
        # Create a Flask test client
        self.app = app.test_client()

    def make_request(self, json_data):
        return self.app.post('http://127.0.0.1:5000/rest/services/delivery_calc', json=json_data)
    

    def test_request_with_data_types_as_descriped_in_task(self):
        # Arrange:
        valid_json = {
            "cart_value": 2000,  
            "delivery_distance": 2235,  
            "number_of_items": 4,  
            "time": "2024-01-26T19:00:00Z"  
        }

        # Act
        response = self.make_request(valid_json)
        response_data = response.get_json()
        
        # Assert
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response_data, {"delivery_fee": 600})  

    
    def test_request_with_numbers_as_strings(self):
        # Arrange:
        json_with_string_numbers = {
            "cart_value": "2000",  
            "delivery_distance": "2235",  
            "number_of_items": "4",  
            "time": "2024-01-26T19:00:00Z"  
        }

        # Act
        response = self.make_request(json_with_string_numbers)
        response_data = response.get_json()
        
        # Assert
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response_data, {"delivery_fee": 600})

    def test_cart_value_as_a_not_valid_string(self):
        # Arrange:
        json_with_string_cart_value = {
            "cart_value": "asdasd",
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_string_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "cart_value must be a valid non-negative integer or a float."}) #Expected to pass
    
    def test_cart_value_as_a_negative_number(self):
        # Arrange:
        json_with_negative_cart_value = {
            "cart_value": -2000,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_negative_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "cart_value must be a valid non-negative integer or a float."})

    def test_cart_value_as_a_float(self):
        # Arrange:
        json_with_float_cart_value = {
            "cart_value": 2000.0,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_float_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response_data, {"delivery_fee": 600})

    def test_cart_value_as_a_flaot_string(self):
        # Arrange:
        json_with_float_string_cart_value = {
            "cart_value": "2000.0",
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_float_string_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response_data, {"delivery_fee": 600})

    def test_cart_value_as_none(self):
        # Arrange:
        json_with_none_cart_value = {
            "cart_value": None,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_none_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "cart_value cannot be None."})

    def test_cart_value_as_empty_string(self):
        # Arrange:
        json_with_empty_string_cart_value = {
            "cart_value": "",
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_empty_string_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "cart_value must be a valid non-negative integer or a float."})

    def test_object_without_cart_value(self):
        # Arrange:
        json_with_empty_object_cart_value = {
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-26T19:00:00Z"
        }

        # Act
        response = self.make_request(json_with_empty_object_cart_value)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "cart_value cannot be None."})

    def test_time_as_a_not_valid_string(self):
        # Arrange:
        json_with_string_time = {
            "cart_value": 2000,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "asdasd"
        }

        # Act
        response = self.make_request(json_with_string_time)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "Invalid 'time' format. It should be a valid date, a datetime object, or a string."})

    def test_time_as_a_empty_string(self):
        # Arrange:
        json_with_empty_string_time = {
            "cart_value": 2000,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": ""
        }

        # Act
        response = self.make_request(json_with_empty_string_time)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "'time' cannot be an empty string."})

    def test_time_as_none(self):
        # Arrange:
        json_with_none_time = {
            "cart_value": 2000,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": None
        }

        # Act
        response = self.make_request(json_with_none_time)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "'time' cannot be None."})

    def test_time_as_a_float(self):
        # Arrange:
        json_with_float_time = {
            "cart_value": 2000,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": 2000.0
        }

        # Act
        response = self.make_request(json_with_float_time)
        response_data = response.get_json()
        
        # Assert:
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response_data, {"error": "Invalid 'time' format. It should be a valid date, a datetime object, or a string."})

if __name__ == '__main__':
    unittest.main()
