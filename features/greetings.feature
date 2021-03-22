Feature: Based on the current time the API will greet the invoker

Scenario: When user passes his/her name to the API
    Given the user "Abhishek" wants to be greeted
    When the user invokes the API
    Then the user should be greeted with either "Hi Abhishek, Good Morning." or "Hi Abhishek, Good Afternoon." or "Hi Abhishek, Good Evening." or "Hi Abhishek, Good Night."