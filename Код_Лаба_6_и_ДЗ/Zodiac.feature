Feature: Zodiac
  Scenario: Love compatibility
    Given I have Zodiac signs numbers {'2'} and {'3'} and I have a relation type {'Любовь'}
    When I check their compatibility in this relation type
    Then I expect to get a result True

  Scenario: Work compatibility
    Given I have Zodiac signs numbers {'0'} and {'1'} and I have a relation type {'Работа'}
    When I check their compatibility in this relation type again
    Then I expect to get a result False