/** 1. QUAN ENTRO A LA SECCIÓ DE QUI SOM
2. PUC VEURE TOTS ELS ELEMENTS DE FORMA CORRECTA **/

*** Settings ***
Documentation     Escenaris
Resource          ../common.robot
Library           Selenium2Library
#Test Setup        Login
Test teardown     Tanca Test

*** Variables ***

*** Test Cases ***

Qui Som
    
    Quan entro a la pàgina principal

    I clico l'apartat Qui Som

    Llavors puc veure tots els elements de forma correcta
    
*** Keywords ***

Quan entro a la pàgina principal

    Open Browser    ${BROWSER_URL}
    Maximize Browser Window

I clico l'apartat Qui Som

    Wait Until Element Is Visible   //*[@id="quiSom-link"]
    Click Link   //*[@id="quiSom-link"]

Llavors puc veure tots els elements de forma correcta

    Wait Until Element Contains     xpath:/html/body/div[3]/div[1]/div/div[1]/h1  Qui Som