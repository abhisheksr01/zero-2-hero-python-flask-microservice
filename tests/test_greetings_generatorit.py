from unittest.mock import patch


@patch("greetings.greetings_generator.get_current_hour")
def test_get_greetings_should_return_morning_msg_when_current_time_is_between_4_and_12(
    get_current_hour, web_client
):
    get_current_hour.return_value = 5

    response = web_client.get("/greetings/Abhishek")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"greeting": "Hi Abhishek, Good Morning."}
