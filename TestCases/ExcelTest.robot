# Created by SPURGE at 23-11-2023
*** Settings ***

Library      ../resources/ExcelHandling.py

*** Keywords ***

*** Test Cases ***

TestExcelData
    ${data} =   ExcelHandling.Open And Read Excel File    Sheet1    1    D:\\exceldata.xlsx
    Log To Console    ${data}