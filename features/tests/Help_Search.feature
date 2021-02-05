# Created by kusia at 2/2/21
Feature: Amazon Help Search Test

  Scenario: User can search for cancelling an order on Amazon
    Given Open Amazon Help page
    When  Input Cancel Order into Amazon Search Help Library field
    Then Verify that Cancel Items or Orders text is present