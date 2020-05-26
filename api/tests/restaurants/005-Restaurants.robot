/** 1. QUAN ENTRO A LA PÀGINA PRINCIPAL
2. I CLICO A UN PUNT DEL CANVAS
3. LLAVORS PUC VEURE LA INFORMACIÓ DEL RESTAURANT **/

*** Settings ***
Documentation     Escenaris
Resource          ../common.robot
Library           Selenium2Library
Library           Process
#Test Setup        Login
Test teardown     Tanca Test

*** Variables ***

*** Test Cases ***

Restaurants
    
    Quan entro a la pàgina principal

    I Clico a un punt del canvas

    Llavors puc veure el popup d'informació del restaurant
    
*** Keywords ***

Quan entro a la pàgina principal

    Open Browser    ${BROWSER_URL}
    Maximize Browser Window

I Clico a un punt del canvas

    Wait Until Element Is Visible   //*[@id="mapaRestaurants"]
    Sleep   5s
    Select Frame    //*[@id="mapaRestaurants"]
    # 512, 205
    Execute Javascript   document.elementFromPoint(512, 205).click();
    #${result}=  Run Process     python      ${CURDIR}/click.py
    #Log    Num value is ${result}   console=yes

Llavors puc veure el popup d'informació del restaurant

    Wait Until Element Is Visible   //*[@id="popup"]
    Wait Until Element Contains     //*[@id="popup-content"]    Restaurant Miramar
