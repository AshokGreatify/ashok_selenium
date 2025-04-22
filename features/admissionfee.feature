Feature: Admission and fees functionality of Greatify

  Scenario: Successful login with valid credentials
    Given I launch a new Chrome browser for admission
    When I have open Greatify URL
    Then I have enter the username and password
    Then Navigate to Admission and fees module
