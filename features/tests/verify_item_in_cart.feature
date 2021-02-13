# Created by kusia at 2/12/21
Feature: Test Scenarios for Shopping Cart functionality

  Scenario: User can add item to shopping cart
   Given Open Amazon page
    When Input Purse into search field
    When Click on search icon
    When Click on first item from the list
    When Add item to the Shopping Cart
    Then Item is present in the Shopping cart