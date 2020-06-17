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

Alta d'un usuari [Dependència]
    
    Quan entro a la secció de registre
    
    Omplo les dades de forma correcta al registre

    Clico al botó de Registrar-se
    
    I el sistema no m'indica que manca informació per completar
    
    Llavors s'ha pogut generar un nou usuari

Login d'un usuari

    Quan entro a la secció de login

    Omplo les dades de forma correcta al login

    Clico al botó d'iniciar sessió

    I el sistema de login no m'indica que manca informació per completar

    Llavors a la part superior dreta del menú surt el nom d'usuari

Error login d'un usuari

    Quan entro a la secció de login

    Em deixo la contrasenya

    Clico al botó d'iniciar sessió

    Llavors el sistema de login m'indica que manca informació per completar
    
*** Keywords ***

# KEYWORDS ALTA D'UN USUARI --> common.robot

# KEYWORDS LOGIN --> common.robot

Em deixo la contrasenya

    # Username

    Click Element   //*[@id="username"]
    Input Text      //*[@id="username"]     ${PERSONALDATA}[6]

    # Password

    # EMPTY!

Llavors el sistema de login m'indica que manca informació per completar

    Wait Until Element Is Visible   //*[@id="loginerror"]