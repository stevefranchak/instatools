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
      | ausername     | apasswd        |
      | aaaaaaaaaaaa1 | aaaaaaaaaaaaa2 |
  

  Scenario Outline: The encapsulation should throw an error when provided with an invalid username or password
    Given we have username "<username>"
      and we have password "<password>"
    When we create an instance of the encapsulation
    Then it should raise a "<exception>" exception

    Examples: Invalid Username/Password Pairs
      | username       | password       | exception  |
      |                |                | ValueError |
      |                | apasswd        | ValueError |
      | ausername      |                | ValueError |
      | None           | None           | TypeError  |
      | None           | apasswd        | TypeError  |
      | ausername      | None           | TypeError  |
      | ["ausername"]  | apasswd        | TypeError  |
      | {}             | apasswd        | TypeError  |
