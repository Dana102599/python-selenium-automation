# Created by kusia at 3/4/21
Feature: Shopping Cart Test
  # Enter feature description here

  Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty' text present
