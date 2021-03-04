# Created by kusia at 3/3/21
Feature: Sign In page test
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazonu page
 When Click Amazon Orders link
 Then Verify Sign In page is opened