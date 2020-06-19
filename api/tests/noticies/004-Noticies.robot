/** 1. QUAN ENTRO A LA SECCIÓ DE NOTICIES
2. PUC VEURE TOTS ELS ELEMENTS DE FORMA CORRECTA **/

*** Settings ***
Documentation     Escenaris
Resource          ../common.robot
Library           Selenium2Library
#Test Setup        Login
Test teardown     Tanca Test

*** Variables ***

*** Test Cases ***

Noticies
    
    Quan entro a la pàgina principal

    I clico l'apartat Noticies

    Llavors puc veure tots els elements de forma correcta
    
*** Keywords ***

Quan entro a la pàgina principal

    Open Browser    ${BROWSER_URL}
    Maximize Browser Window

I clico l'apartat Noticies

    Wait Until Element Is Visible   //*[@id="noticies-link"]
    Click Link   //*[@id="noticies-link"]

Llavors puc veure tots els elements de forma correcta

    Wait Until Element Contains     xpath:/html/body/div[1]/div/div/div/h1  Notícies