Feature: Login functionality of Greatify

  Scenario: Successful login with valid credentials
    Given I launch Chrome browser
    When I open Greatify URL
    Then I enter the username and password
    Then I choose an image file to upload
    Then I click the Syllabus Dropdown
    Then I Click the Medium of School
    Then I enter the contact name
    Then I enter the Phonenumber
    Then I enter the Website Address
    Then I enter the Latitude and Longitude
    Then I enter the Address line 1
    Then I enter the Address line 2
    Then I choose the country
    Then I choose the State
    Then I choose the city
    Then I choose the pincode
    Then I selected for next step 2

  #step 2 onboard subject
    Then I choose Onboard subject file

  #Step 3 Onboard Class
    Then I choose Onboard teacher file

  #Step 4 onboard
    Then I choose Onboard class file

  #Step 5 Student
    Then I choose Onboard Student file

  #step 6 submit
   Then Onboarded Successfully
