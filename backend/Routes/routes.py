# routes/routes.py
from flask import Blueprint
# from Controllers.hello import hello 
from Controllers.calc import calc

# Create a Blueprint object for your routes
routes = Blueprint('routes', __name__)



# Define the route using the Blueprint
@routes.route('/rest/services/delivery_calc', methods=['POST'])
def calc_route():
    return calc()
# @routes.route('/', methods=['POST'])
# def hello_route():
#     return hello()
