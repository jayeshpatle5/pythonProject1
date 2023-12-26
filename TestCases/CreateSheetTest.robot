*** Settings ***
Library  OperatingSystem

*** Test Cases ***
Create New Sheet Using Openpyxl
    ${file_path}=    Set Variable    path/to/your/excel/file.xlsx
    ${sheet_name}=   Set Variable    NewSheetName
    Run Keyword    Create New Sheet Using Openpyxl    ${file_path}    ${sheet_name}

*** Keywords ***
Create New Sheet Using Openpyxl
    [Arguments]    ${file_path}    ${sheet_name}
    # Python code to create a new sheet using openpyxl
    ${python_code}=    Catenate
    ...    Library openpyxl
    ...    | wb = load_workbook('${file_path}')
    ...    | if '${sheet_name}' not in wb.sheetnames:
    ...    | ... wb.create_sheet(title='${sheet_name}')
    ...    | ... wb.save('${file_path}')
    Run Keyword If    'openpyxl' not in sys.modules    Set Library Search Order    openpyxl

*** Variables ***
${file_path}    path/to/your/excel/file.xlsx
${sheet_name}   NewSheetName

