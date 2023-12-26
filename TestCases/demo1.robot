*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${browser}  chrome

${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${username}  name:username
${password}  name:password
${submit}   xpath://button[@type='submit']

*** Test Cases ***
LoginTest
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    name:username
    Input Text    ${username}    Admin
    Input Text    ${password}    admin123
    Click Button    ${submit}
    Title Should Be    OrangeHRM
    Close Browser



*** Keywords ***

