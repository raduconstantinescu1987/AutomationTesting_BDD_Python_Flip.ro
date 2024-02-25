# BDD_Automated_Test_Project

### TESTED LOGIN PAGE ON WWW.FLIP.RO WEBSITE

https://flip.ro/autentifica-te/

I chose to check the functionality of the Flip.ro Login Page using automation testing. In this testing module I used different Login Scenarios in the "e-mail" and "password" input such as : invalid username & password, too short username or password, " " username or password etc 

### LANGUAGE, IDE, BOOKSTORES
I chose to perform the testing using the Python programming language and the PyCharm IDE. After installing Cucumber, Gherking & Ini plugins, I used the Selenium, webdriver-manager, behave and behave-html-formatter libraries to automate the interaction with the Flip.ro website. The "Python Packages" section of PyCharm can be accessed to install these libraries. After adding the name of the desired library in the field, I pressed the "Install" button.

### THE IMPORTANCE OF AUTOMATED TESTING
Efficiency in software development depends on automated testing. Speed, reproducibility, extended coverage, reusability, ease of integration with agile development practices and early detection of errors are the main benefits. This constantly helps to ensure the quality of the software.

### THE CHOSEN METHODOLOGY
The software development methodology called BDD (Behavior-Driven Development) focuses on the collaboration of team members and on describing the behavior of the application in a simple language, such as Gherkin. We chose BDD to facilitate communication between developers, testers and other interested parties and to create automated tests that reflect the behavior clearly specified by stakeholders. Benefits include: clear communication, easy-to-understand and up-to-date tests, and alignment between requirements and implementation. BDD encourages teamwork and guarantees that development focuses on developing useful functionalities that meet user expectations.

### DESIGN PATTERN 
I chose to organize the code of the automated tests using the "Page Object Model" (POM). Reusability, encapsulation, ease of maintenance, readability and resistance to change are some of its benefits. POM improves the development and maintenance of automated tests and code structure.

### USE OF THE PROJECT
Using the project starts by cloning it from GitHub. Access the project, press the green "Code" button, copy the link, navigate on the computer to the desired folder, open Git Bash, write the command "git clone" followed by the link and press "Enter". The cloned project can be opened in PyCharm. To run tests, use the command "behave" in the terminal. To view the generated report, open the *"behave-report.html"* file in Chrome.

### STRUCTURE OF THE PROJECT
The project has a structure consisting of a series of files and directories. We find settings for opening Chrome, maximizing the window and a default wait of three seconds in the "browser" file. We have the structure of the pages tested in the "environment". "features", "pages" and "steps" are the three directories that make up the general structure. The test scenarios are written in Gherkin syntax and can be found in the "features" category. We have general methods for actions such as clicking, finding the element, typing, etc. defined in "pages". The other files contain locators and specific methods for the suggested scenarios. The Gherkin syntax defines the functions of the "steps" directory. This structure organizes the code for automated tests.

### SCREENSHOTS WITH THE CODE

![behave report scenarios](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/2e7bc744-ffae-4778-a05e-232c8118d417)

![behave](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/9af2905a-43c8-4dee-91d9-fd290e06b013)

![context](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/063308ab-3d9e-481d-b1d2-fad8d6e23aa3)

![HTML](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/d14aac53-d42e-4bf5-9c2c-048c7b9b6c6d)

![import](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/2caa3157-7d19-4a45-9dc2-ddb74419bfb2)

![login](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/8712ddcf-5c32-4d83-b816-b2a341f561d3)

![plug in](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/154634d1-f8e8-4f4f-ab89-f5e9f8d29578)

![steps](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/052d6100-0986-4567-ae6a-715ceca09302)

![raport html behave](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/d064e7a6-c2c2-43eb-920f-2a68bd02da0b)

![scen 5](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/d6345276-4c69-4856-bfe3-5f47fd1b81ea)

![scen4 4](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/7800b450-6cbb-40f7-9658-c3bda6df986e)

![scen3 3](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/e12f042d-3279-4753-bbfd-cbb8ae361193)

![scen1 1](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/aa8b077e-55bb-4815-9de0-f8290ce7b19e)

![git status](https://github.com/raduconstantinescu1987/AutomationTesting_BDD_Python_Flip.ro/assets/147180342/d9607aea-16df-4320-9682-3bff202b4b40)

### SCENARIOS

Test scenarios chosen for evaluation include:

* Submitting an unregistered e-mail & password
* Using an invalid username & valid password
* Using an invalid password & a valid username
* Using an invalid username & too short password
* Log in to the customer account using a valid username & password

