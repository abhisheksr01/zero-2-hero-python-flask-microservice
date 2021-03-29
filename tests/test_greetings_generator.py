from greetings.greetings_generator import get_greeting
from unittest.mock import patch


def test_get_greetings_function_should_accept_a_string_input_and_returns_string_response():
    type(get_greeting("Abhishek")) is str


@patch("greetings.greetings_generator.get_current_hour")
def test_get_greetings_should_return_morning_greeting_when_current_time_is_between_4_and_12(
    get_current_hour,
):
    get_current_hour.return_value = 5

    expected_greeting = {"greeting": "Hi Abhishek, Good Morning."}
    actual_greeting_dict = get_greeting("Abhishek")
    assert (
        expected_greeting == actual_greeting_dict
    ), f"Expected {expected_greeting} but found {actual_greeting_dict}"


@patch("greetings.greetings_generator.get_current_hour")
def test_get_greetings_should_return_afternoon_greeting_when_current_time_is_greater_equals_12_and_less_than_17(
    get_current_hour,
):
    get_current_hour.return_value = 12

    expected_greeting = {"greeting": "Hi Abhishek, Good Afternoon."}
    actual_greeting_dict = get_greeting("Abhishek")
    assert (
        expected_greeting == actual_greeting_dict
    ), f"Expected {expected_greeting} but found {actual_greeting_dict}"


@patch("greetings.greetings_generator.get_current_hour")
def test_get_greetings_should_return_evening_greeting_when_current_time_is_between_17_and_20(
    get_current_hour,
):
    get_current_hour.return_value = 18

    expected_greeting = {"greeting": "Hi Abhishek, Good Evening."}
    actual_greeting_dict = get_greeting("Abhishek")
    assert (
        expected_greeting == actual_greeting_dict
    ), f"Expected {expected_greeting} but found {actual_greeting_dict}"


@patch("greetings.greetings_generator.get_current_hour")
def test_get_greetings_should_return_night_greeting_when_current_time_is_between_20_and_4(
    get_current_hour,
):
    get_current_hour.return_value = 22

    expected_greeting = {"greeting": "Hi Abhishek, Good Night."}
    actual_greeting_dict = get_greeting("Abhishek")
    assert (
        expected_greeting == actual_greeting_dict
    ), f"Expected {expected_greeting} but found {actual_greeting_dict}"
