# Created by SPURGE at 24-11-2023
*** Settings ***
Library    ExcelLibrary
Library    Collections
*** Keywords ***

*** Test Cases ***

Check created excel doc
    ${document}=    Create Excel Document   doc_id=exceldata.xlsx
               Write Excel Cell    1    1    Jayesh_patle
               Save Excel Document   filename=D://Excellibfile.xlsx
               Close Current Excel Document

Read data from Excel file
    Open Excel Document    D://Excellibfile.xlsx    doc1
    ${data}=  Read Excel Cell    1    1
    Log To Console    ${data}

Get All Sheet Names
    Open Excel Document    D://Excellibfile.xlsx    doc1
  #  Create Excel Document	doc_id=doc1
    ${sheets}=	Get List Sheet Names
    List Should Contain Value	${sheets}	Sheet 1
    Log To Console    ${sheets}
    Close All Excel Documents
