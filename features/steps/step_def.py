import time
import requests
from behave import given, when, then


@given('the user "{name}" wants to be greeted')
def step_impl(context, name):
    context.user_name = name


@when("the user invokes the API")
def step_impl_when(context):
    response = requests.get(f"{context.root_url}/greetings/{context.user_name}")
    context.response = response


@then(
    'the user should be greeted with either "{morning_greeting}" or "{afternoon_greeting}" or "{evening_greeting}" or "{night_greeting}"'
)
def step_impl_then(
    context, morning_greeting, afternoon_greeting, evening_greeting, night_greeting
):
    expected_greeting = ""
    current_hour = int(time.strftime("%H"))
    if (current_hour >= 4) and (current_hour < 12):
        expected_greeting = morning_greeting
    elif (current_hour >= 12) and (current_hour < 17):
        expected_greeting = afternoon_greeting
    elif (current_hour >= 17) and (current_hour < 20):
        expected_greeting = evening_greeting
    else:
        expected_greeting = night_greeting

    assert (
        context.response.status_code == 200
    ), f"Expected status 200 but found {context.response.status_code}"
    assert (
        context.response.json()["greeting"] == expected_greeting
    ), f"Expected {expected_greeting} but found {context.response.get_json()['greeting']}"
