*******Read me **********

I.Project Details -------------------------------------------------------------------------------------------------------------------------------------
Project Name :- SennderQAAssignment
tech and IDE used - Python ,Selenium, PyCharm IDE

Directory structure

Directory1 :-Config
Filename :- config.py 
this file contains all contant values , so that in case We want to change any value, 
we can direclty change in this file instead of going through the code. example username, password...

Directory2 :-Pages
Filename :- SprintBoard.py 
this file contains all methods which covers all Test senarios and Assertions

Directory3 :-Test_cases
Filename :- test_SprintBoard.py 
this file is used to run test automation. It contains class in which all methods are getting called 
and We need to run this file for executing the smoke test plan.

II. Steps to Setup---------------------------------------------------------------------------------------------------------------------------------------
1) Import project in pycharm
2) Install Chrome driver, Enter local path of Chrome Driver from your P.C and update in Config/config.py File,
   against key : CHROME_EXECUTABLE_PATH
3) Open project in terminal and install selenium by command - pip install selenium
4) Run test_SprintBoard.py. (open the file --> right click on it and run)
5) In case any test is faild, assertion error will be thrown on the console.


III Project Enhancements
Below objectives can also be achieved:
1) Report can be generated using pytest/ Unittest/ Allure Report. for pytest , we just need to import pytest in the test class 
and on setup method @pytest.facture need to be added. and the method name should start with test_***.
2) To follw POM completely , we can seggregate code for each page, we can have one class per page. 
As of now one class is created to deal end to end scenario.
