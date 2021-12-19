Feature: my
  Scenario: similarity check
    Given I have the components {left caramel} and {left biscuit}
    When I request for their similarity
    Then I expect the result to be {Left caramel on the Left biscuit. We are the same.}

  Scenario: difference check
    Given I have the components {left caramel} and {right biscuit}
    When I request for their difference
    Then I expect the result to be {We are not the same.}

  Scenario: difference check 2
    Given I have the components {right caramel} and {left biscuit}
    When I request for their difference again
    Then I expect the result to be {We are not the same.} again

  Scenario: right stick check
    Given I have the {right stick}
    When I request for what it is made of
    Then I expect the result to be {I'm Right stick. I'm made of Right caramel on the Right biscuit. We are the same.}

  Scenario: left stick check
    Given I have the {left stick}
    When I request for what it is made of again
    Then I expect the result to be {I'm Left stick. I'm made of Left caramel on the Left biscuit. We are the same.}
