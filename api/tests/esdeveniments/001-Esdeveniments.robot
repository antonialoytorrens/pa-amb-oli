/** 1. QUAN ENTRO A LA SECCIÓ DE LOGIN
2. OMPLO LES DADES DE FORMA CORRECTA
3. A LA PART SUPERIOR DRETA DEL MENÚ SURT EL NOM D'USUARI **/

*** Settings ***
Documentation     Escenaris
Resource          ../common.robot
Library           Selenium2Library
#Test Setup        Login
Test teardown     Tanca Test

*** Variables ***

*** Test Cases ***

Informació d'un esdeveniment

    Quan entro a la secció d'esdeveniments

    Clico a un esdeveniment existent

    Llavors puc veure la informació sobre aquest esdeveniment
    
*** Keywords ***

Quan entro a la secció d'esdeveniments

    Open Browser    ${BROWSER_URL}/esdeveniments/
    Maximize Browser Window

Clico a un esdeveniment existent

    Wait Until Element Is Visible   css:td.fc-event-container:nth-child(3)
    Click Element   css:td.fc-event-container:nth-child(3)

Llavors puc veure la informació sobre aquest esdeveniment

    Wait Until Element Contains     //*[@id="esdeveniment-seleccionat"]     Esdeveniment