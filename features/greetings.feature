Feature: Based on the current time the API will greet the invoker

Scenario: When user passes their name to the API
    Given the user "Abhishek" wants to be greeted
    When the user invokes the API
    And Morning time is between "4" and "12"
    And Afternoon time is between "12" and "17"
    And Evening time is between "17" and "20"
    And Night time is between "20" and "4"
    Then the user should be greeted with either "Hi Abhishek, Good Morning." or "Hi Abhishek, Good Afternoon." or "Hi Abhishek, Good Evening." or "Hi Abhishek, Good Night."