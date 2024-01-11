import time

from flask import Blueprint
from markupsafe import escape

greet = Blueprint("greet", __name__, url_prefix="/greetings/")


@greet.route("/<user_name>", methods=["GET"])
def get_greeting(user_name):
    user_name = escape(user_name)
    current_hour = get_current_hour()
    day_state = "Night"
    if (current_hour >= 4) and (current_hour < 12):
        day_state = "Morning"
    elif (current_hour >= 12) and (current_hour < 17):
        day_state = "Afternoon"
    elif (current_hour >= 17) and (current_hour < 20):
        day_state = "Evening"
    return {"greeting": f"Hi {user_name}, Good {day_state}."}


def get_current_hour():
    return int(time.strftime("%H"))
