Feature: Encapsulation for username/password credentials (irrespective of API)

  Scenario Outline: The encapsulation should accept a valid username and password
    Given we have username "<username>"
      and we have password "<password>"
    When we create an instance of the encapsulation
    Then it should have the provided username and password
      and it should be of the proper type and class
      and it should not have a payload formatter

    Examples: Valid Username/Password Pairs
        | username      | password       |
        | steve         | somepasswd     |
        | aaaaaaaaaaaa1 | aaaaaaaaaaaaa2 |
