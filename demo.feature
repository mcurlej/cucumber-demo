Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      when we implement a test
      then behave will test it for us!

  Scenario: Login with different users
    Given we login with user Bob 
    then the step should be successfull
    when the user will logout
    then the step should be successfull
    Given we login with user Martin 
    then the step should be successfull
    when the user will logout
    then the step should be successfull
    Given we login with user Eric
    then the step should be unsuccessfull
