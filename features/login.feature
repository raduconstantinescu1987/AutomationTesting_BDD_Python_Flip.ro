Feature: Check the functionality of the Login Page

  #  Scenariul 1: username neinregistrat + parola
  Scenario: Check "Aceasta adresa de e-mail nu este asociata unui cont existent" message is displayed when I enter an unregistered e-mail adress.
    Given I am on the Login Page
    When I accept cookies
    When I insert an unregistered e-mail in the e-mail adress input
    When I insert a password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "Această adresă de email nu este asociată unui cont existent." message

  #  Scenariul 2: username None + parola corecta
  Scenario: Check "Adresa de e-mail lipsește." message is displayed when I enter username None.
    Given I am on the Login Page
    When I insert " " in the e-mail adress input
    When I insert a valid password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "Adresa de e-mail lipsește." message

  #  Scenariul 3: username ok + parola incorecta

  Scenario: Check "Parola curentă nu corespunde cu cea pe care ai introdus-o." message is displayed when I enter a wrong password.
    Given I am on the Login Page
    When I insert "radu.constantinescu1987@gmail.com" in the e-mail adress input
    When I insert an invalid password in the password input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "Parola curentă nu corespunde cu cea pe care ai introdus-o." message

    #  Scenariul 4: username neinregistrat + parola doar 1 caracter
  Scenario: Check "Parola trebuie sa aiba cel putin 6 caractere" message is displayed when I enter an unregistered e-mail adress & short password
    Given I am on the Login Page
    When I insert "a@gmail.com" in the e-mail adress input
    When I insert "1" in the password adress input
    When I click on the login button
    Then The main error message is displayed
    Then The error message contains "Parola trebuie sa aiba cel putin 6 caractere" message

      # Scenariul 4 : username ok + parola ok
  Scenario: Check "Te-ai autentificat cu succes" message is displayed when I enter an registered e-mail & valid password
    Given I am on the Login Page
    When I insert "radu.constantinescu1987@gmail.com" in the e-mail adress input
    When I insert a correct password
    When I click on the login button
    Then The main error message is displayed
    Then The message "Te-ai autentificat cu succes" is displayed


  #  Scenariu 7: username None + parola incorecta
  #  Scenariu 8: username None + parola None
  #  Scenariu 9: username gresit + parola gresita
  #  Scenariu 10: username blocat (locked_out_user) + parola corecta