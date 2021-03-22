import time
import requests

@given(u'the user "{name}" wants to be greeted')
def step_impl(context,name):
    context.user_name = name

@when(u'the user invokes the API')
def step_impl(context):
    response = requests.get(f"http://localhost:5000/greetings/{context.user_name}")
    context.response = response


@then(u'the user should be greeted with either "{morning_greeting}" or "{afternoon_greeting}" or "{evening_greeting}" or "{night_greeting}"')
def step_impl(context, morning_greeting, afternoon_greeting, evening_greeting, night_greeting):
    current_hour = int(time.strftime('%H'))
    if (current_hour >= 4) and (current_hour < 12):
        expected_message = morning_greeting
    elif (current_hour >= 12) and (current_hour < 17):
        expected_message = afternoon_greeting
    elif (current_hour >= 17) and (current_hour < 20) :
        expected_message = evening_greeting
    elif (current_hour >= 20) and (current_hour < 5):
        expected_message = night_greeting

    assert context.response.msg == expected_message