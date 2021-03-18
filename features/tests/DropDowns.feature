# Created by kusia at 3/17/21
Feature: Test to verify dropdown functionality
  # Enter feature description here

  Scenario: User can select and search in a department
    Given Open Amazoni page
    When Select electronics department
    When Input Watch into Amazon search field
    And Click on search icon
    Then Verify Electronics department is selected