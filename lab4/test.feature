Feature: BDD file

    Scenario: Test1
        Given I have the coefficients 0, 1 and -4
        When I calculate them
        Then I expect the result to be -2, 2

    Scenario: Test2
        Given I have the coefficients 1, 0 and -81
        When I calculate them
        Then I expect the result to be -3, 3

    Scenario: Test3
        Given I have the coefficients 1, 2 and 0
        When I calculate them   
        Then I expect the result to be 0