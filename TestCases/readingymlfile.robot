# Created by SPURGE at 24-11-2023
*** Settings ***
Variables   ../resources/Data.yml
*** Keywords ***

*** Test Cases ***
PrintData
   Log To Console    ${Employee.Name}
   Log To Console    ${Employee.Job}
