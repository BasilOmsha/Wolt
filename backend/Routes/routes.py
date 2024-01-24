# routes/routes.py
from flask import Blueprint
# from Controllers.hello import hello 
from Controllers.calc import calc

# Create a Blueprint object for your routes
router = Blueprint('routes', __name__)

# route using the Blueprint
@router.route('/rest/services/delivery_calc', methods=['POST'])
def calc_route():
    return calc()

