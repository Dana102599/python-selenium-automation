# Created by kusia at 2/3/21
Feature: Test Scenario for Shopping Cart Functionality
  # Enter feature description here

  Scenario: User can check the Shopping Cart
    Given Open Amazon page
    When Click on the cart icon
    Then Verifies that Your Shopping Cart is Empty
