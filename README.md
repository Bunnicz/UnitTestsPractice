# Python Unit Tests Practice with pytest and coverage plugin

![Tests](https://github.com/Bunnicz/UnitTestsPractice/actions/workflows/linter_check.yml/badge.svg)
![Tests](https://github.com/Bunnicz/UnitTestsPractice/actions/workflows/static_code_analysis_check.yml/badge.svg)
![Tests](https://github.com/Bunnicz/UnitTestsPractice/actions/workflows/tests_check.yml/badge.svg)

Repo is based on the simple order payment processor which checks credit card credentials e.g. card number via Luhn algorithm and card validity (expiration date).
Running the script CLI asks user for credit card information and charges the card with static Line Items defined in main.py

Additionally **github Actions (workflows)** were tested with the use of the repository secret variable API_KEY.

Main point of this repo was to learn how to write basic and more advanced unit tests with **pytest** package. After that it was easier to notice where refactoring will simplify the code and our unit tests as a result. 
More difficult tests were done with the use of **MonkeyPatch** to override the built-in OS input reading system. Other thing was creating **mock** function to replace current charge method so that running the tests won’t charge provided credit card.
**Coverage plugin** for pytest was helpful to check which part of the code still needs to be  included in the unit tests.

Main points of the refactored code:
-	Used **dependency injection** so that the objects that are needed are provided as a arguments instead of being created by the class itself.
-	Dependency inversion allows to replace payment processor with other one without the need to change the code in previous function.
-	Created payment processor mock class.
-	Removed input patching.
-	Used a fixture for the credit card and payment processor object so that they can be easily supplied to the unit tests without the repetition of the code.
-	Removed hardcoded dates from the unit tests so that the tests will be always passing.
-	Turned Luhn checksum into a function cause it didn’t use any of the class variables.
-	Hidden API_KEY with .env file and used python-dotenv package to load environmental variable into the script.

Source: https://github.com/ArjanCodes/2022-test-existing-code
