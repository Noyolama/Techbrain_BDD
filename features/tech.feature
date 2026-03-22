Feature: Techbrain Functionality

Scenario: Open Techbrain website
Given user open techbrain website
Then user see provided courses by techbrain website


Scenario: Signup user
Given user open techbrain website
When user click login link
And user click signup link
And user enter email "test123@gmail.com" and password "test123" and confirm_password "test123"
Then user click on signup button

Scenario: Signin user
Given user open techbrain website
When user click login link
And user enter email "test123@gmail.com" and password "test123" 
Then Techbrain user click on login button

Scenario: List display
Given user open techbrain website
When user click list link
Then lists of lesson of courses are displayed 

Scenario: Quiz display
Given user open techbrain website
When user click start button of first course
And user click next button until they encounter go to quiz button
And user click go to quiz button
And user choose any one option from each question
Then user click on submit button

Scenario: Lessonlist display
Given user open techbrain website
When user click start button of first course
And click lessonlist button
Then user see list of lessonlist

Scenario: nodenv link open
Given user open techbrain website
When user click start button of second course
And scroll upto they found nodenv link and click
Then nodenv opens

Scenario: finish button functionality
Given user open techbrain website
When user click start button of first course
And click lessonlist button
And user scroll all the lesson until last lesson and click on it
And user click on finish button
Then user land to dashboard
