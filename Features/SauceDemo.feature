Feature: SauceDemo is checking for valid and invalid users authentication and let them to shopping
  Scenario: Successful Login
    Given I launch Chrome browser
    When I am on the Demo Login Page
    When I fill the account information to account StandardUser to the Username "standard_user" to the Password "secret_sauce"
    When I click the Login Button
    Then I am redirected to the Demo Main Page "Products"
    And I verify the App Logo exists

  Scenario: Failed Login
    Given Launching Chrome browser
    When I am on Demo Login Page
    When I fill account information to account LockedOutUser to the Username "locked_out_user" to the Password "secret_sauce"
    When I click Login Button
    Then I verify the Error Message contains the text "Sorry, this user has been banned. "

  Scenario: Successful Login
    Given I am launching Chrome browser
    When I am in the Demo Login Page
    When I fill account information on account StandardUser to the Username "standard_user" to the Password "secret_sauce"
    When I clicked the Login Button
    Then I am redirected to Demo Main Page "Products"
    When User sorts products from low price to high price "p"
    When user adds lowest priced product
    When user clicks on cart
    When user clicks on checkout
    Then user enters firstname "John" lastname "Doe" zipcode "123"
    Then user clicks Continue button
    Then I verify in Checkout overview page if the total amount for the added item is "Total: $8.63"
    When user clicks Finish button
    Then Thank You header is shown in Checkout Complete page
