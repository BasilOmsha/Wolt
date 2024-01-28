<!---
To switch between views in VScode, press Ctrl+Shift+V in the editor.
-->
# Wolt
The pre-assignment for 2024 backend internship at Wolt Helsinki/Finland

# Flask Delivery Fee Calculator

This Flask application calculates the delivery fee based on various factors, including the cart value, delivery distance, number of items, and the day and time of the delivery.

## Endpoints

### Calculate Delivery Fee

- **Endpoint**: `/rest/services/delivery_calc`
- **HTTP Method**: POST
- **Description**: Calculates the delivery fee based on the provided JSON data, which includes the cart details.
- **Request Body**: JSON data containing the following parameters:
  - `cart_value`: The total value of the cart in cents.
  - `delivery_distance`: The distance of the delivery in meters.
  - `number_of_items`: The number of items in the cart.
  - `time`: The day and time of the delivery in the format "YYYY-MM-DDTHH:MM:SSZ".

### Error Handling
If the provided JSON data is invalid or if there are any errors during the calculation, the server will respond with a JSON 
error message and an HTTP status code of 400 (Bad Request).

## Test Controller
The test controller, represented by the `TestCalcFunction` class, is responsible for conducting unit tests on the Flask application's `/rest/services/delivery_calc` endpoint. These unit tests serve the following technical purposes:

- **Data Validation**: Verify the endpoint's ability to validate and convert different data types correctly, such as integers, strings, floats, and datetime objects. With the help of the test, the app accepts string integer and floats. Example: 123, "123", 123.4 and "123.4"

- **Error Handling**: Validate the error-handling mechanisms of the endpoint, particularly its responses to invalid or missing data such as "asd!#ad", None, ""

These unit tests focus on technical validation and verification of the values sent to the `calc` endpoint, contributing to the overall quality assurance of the Flask application.


### Running the Server

To set up and run the Flask server, follow these steps:

1. Install Python (if not already installed).
2. Install Flask using `pip` if it's not already installed: `pip install Flask`.
3. Clone or download this repository to your local machine.
4. Navigate to the project directory.
5. Run the Flask server by executing the following command: `python server.py`
6. The server should start, and you should see output indicating that the server is running in debug mode.
7. You can now send POST requests to the `/rest/services/delivery_calc` endpoint to calculate the delivery fee.

## Usage Example

Here's an example of how to calculate the delivery fee using the `/rest/services/delivery_calc` endpoint:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
 "cart_value": 2000,
 "delivery_distance": 2235,
 "number_of_items": 4,
 "time": "2024-01-26T19:00:00Z"
}' http://localhost:5000/rest/services/delivery_calc'
```
Result output:
```bash
{
  "delivery_fee": 600
}
```
Or by using postman.
