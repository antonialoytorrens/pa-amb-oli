*** Settings ***
Documentation     Escenaris
Library           Selenium2Library

*** Variables ***
${BROWSER_URL}  http://127.0.0.1:8000


#NOM I LLINATGES, DATA NAIXEMENT, DIRECCIO, CONTRASENYA, EMAIL, TELEFON, USERNAME
@{PERSONALDATA}     Nom Llinatge Llinatge  30-11-2000  S'Esgleieta, 12, Palma  exemplecontrasenya  exemple4@exemple.com   971234567  exemple4

*** Keywords ***

# TEST CASES

Tanca Test
    Sleep   2s
    Close Browser

# ALTA D'UN USUARI

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


# LOGIN

Quan entro a la secció de login

    Open Browser    ${BROWSER_URL}/accounts/login/
    Maximize Browser Window

Omplo les dades de forma correcta al login

    # Username

    Click Element   //*[@id="username"]
    Input Text      //*[@id="username"]     ${PERSONALDATA}[6]

    # Password

    Click Element   //*[@id="password"]
    Input Text      //*[@id="password"]     ${PERSONALDATA}[3]

Clico al botó d'iniciar sessió

    Click Element   //*[@id="bLogin"]

I el sistema de login no m'indica que manca informació per completar

    Element Should Not Be Visible   //*[@id="errorusername"]
    Element Should Not Be Visible   //*[@id="errorpassword"]

Llavors a la part superior dreta del menú surt el nom d'usuari

    Wait Until Element Contains     css:.mr-auto > li:nth-child(1) > a:nth-child(1)     ${PERSONALDATA}[6]