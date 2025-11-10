Feature: Login Functionality

  Background:
    Given launch the application
    When navigate to the login page

  Scenario Outline: Verify login with multiple users
    And enter "<username>" and "<password>"
    Then verify login result
    Then close the browser

    Examples:
      | username       | password |
      | abc@gmail.com  | abc1     |
      | xyz@gmail.com  | xyz123   |
