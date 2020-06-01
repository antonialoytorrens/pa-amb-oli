/** 1. QUAN ENTRO A LA SECCIÓ DE REGISTRE
2. OMPLO LES DADES DE FORMA CORRECTA
3. S'HA POGUT GENERAR UN NOU USUARI **/

*** Settings ***
Documentation     Escenaris
Resource          ../common.robot
Library           Selenium2Library
#Test Setup        Login
#Test teardown     Tanca Test

*** Variables ***

*** Test Cases ***

Alta d'un usuari
    
    Quan entro a la secció de registre
    
    Omplo les dades de forma correcta al registre

    Clico al botó de Registrar-se
    
    I el sistema no m'indica que manca informació per completar
    
    Llavors s'ha pogut generar un nou usuari

Error d'alta d'un usuari

    Quan entro a la secció de registre

    Em deixo l'email sense omplir

    Clico al botó de Registrar-se

    El sistema m'indica que manca informació per completar

    Llavors no s'ha pogut generar un nou usuari
    
*** Keywords ***

Quan entro a la secció de registre

    Open Browser    ${BROWSER_URL}/registre/
    Maximize Browser Window

Omplo les dades de forma correcta al registre

    # Nom i llinatges
    Click Element   //*[@id="nomillinatges"]
    Input Text      //*[@id="nomillinatges"]    ${PERSONALDATA}[0]

    # Nom d'usuari
    Click Element   //*[@id="username"]   
    Input Text      //*[@id="username"]     ${PERSONALDATA}[6]

    # Data de naixement
    Click Element   //*[@id="datanaixement"]
    Input Text      //*[@id="datanaixement"]    ${PERSONALDATA}[1]

    # Direcció
    Click Element   //*[@id="direccio"]
    Input Text      //*[@id="direccio"]     ${PERSONALDATA}[2]

    # Contrasenya
    Click Element   //*[@id="password"]
    Input Text      //*[@id="password"]     ${PERSONALDATA}[3]

    # Repeteix la Contrasenya
    Click Element   //*[@id="rpassword"]
    Input Text      //*[@id="rpassword"]    ${PERSONALDATA}[3]

    # Email
    Click Element   //*[@id="email"]   
    Input Text      //*[@id="email"]     ${PERSONALDATA}[4]

    # Telefon
    Click Element   //*[@id="telefon"]   
    Input Text      //*[@id="telefon"]     ${PERSONALDATA}[5]

Clico al botó de Registrar-se

    Click Element    //*[@id="registre"]
    Press Keys    //*[@id="registre"]    ENTER

I el sistema no m'indica que manca informació per completar

    Element Should Not Be Visible   //*[@id="errorusuaricreat"]

Llavors s'ha pogut generar un nou usuari

    Wait Until Page Contains Element           //*[@id="usuaricreat"]




Em deixo l'email sense omplir

    # Nom i llinatges
    Click Element   //*[@id="nomillinatges"]
    Input Text      //*[@id="nomillinatges"]    ${PERSONALDATA}[0]

    # Data de naixement
    Click Element   //*[@id="datanaixement"]
    Input Text      //*[@id="datanaixement"]    ${PERSONALDATA}[1]

    # Direcció
    Click Element   //*[@id="direccio"]
    Input Text      //*[@id="direccio"]     ${PERSONALDATA}[2]

    # Contrasenya
    Click Element   //*[@id="password"]
    Input Text      //*[@id="password"]     ${PERSONALDATA}[3]

    # Repeteix la Contrasenya
    Click Element   //*[@id="rpassword"]
    Input Text      //*[@id="rpassword"]    ${PERSONALDATA}[3]

    # Email
    #Click Element   //*[@id="email"]   
    #Input Text      //*[@id="email"]     ${PERSONALDATA}[4]

    # Telefon
    Click Element   //*[@id="telefon"]   
    Input Text      //*[@id="telefon"]     ${PERSONALDATA}[5]

El sistema m'indica que manca informació per completar

    Element Should Not Be Visible   //*[@id="usuaricreat"]

Llavors no s'ha pogut generar un nou usuari

    Wait Until Page Contains Element    //*[@id="errorusuaricreat"]
