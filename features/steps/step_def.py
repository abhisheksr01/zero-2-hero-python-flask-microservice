import time
import requests
from behave import given, when, then


@given('the user "{name}" wants to be greeted')
def step_impl_given(context, name):
    context.user_name = name


@when("the user invokes the API")
def step_impl_when(context):
    response = requests.get(f"{context.root_url}/greetings/{context.user_name}")
    context.response = response


@when('Morning time is between "{m1}" and "{m2}"')
def step_impl_morning(context, m1, m2):
    context.m1 = m1
    context.m2 = m2


@when('Afternoon time is between "{a1}" and "{a2}"')
def step_impl_afternoon(context, a1, a2):
    context.a1 = a1
    context.a2 = a2


@when('Evening time is between "{e1}" and "{e2}"')
def step_impl_eve(context, e1, e2):
    context.e1 = e1
    context.e2 = e2


@when('Night time is between "{n1}" and "{n2}"')
def step_impl_night(context, n1, n2):
    context.n1 = n1
    context.n2 = n2


@then(
    'the user should be greeted with either "{morning_greeting}" or "{afternoon_greeting}" or "{evening_greeting}" or "{night_greeting}"'
)
def step_impl_then(
    context, morning_greeting, afternoon_greeting, evening_greeting, night_greeting
):
    expected_greeting = ""
    current_hour = int(time.strftime("%H"))
    if (current_hour >= int(context.m1)) and (current_hour < int(context.m2)):
        expected_greeting = morning_greeting
    elif (current_hour >= int(context.a1)) and (current_hour < int(context.a2)):
        expected_greeting = afternoon_greeting
    elif (current_hour >= int(context.e1)) and (current_hour < int(context.e2)):
        expected_greeting = evening_greeting
    else:
        expected_greeting = night_greeting

    assert (
        context.response.status_code == 200
    ), f"Expected status 200 but found {context.response.status_code}"
    assert (
        context.response.json()["greeting"] == expected_greeting
    ), f"Expected {expected_greeting} but found {context.response.get_json()['greeting']}"
