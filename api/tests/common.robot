*** Settings ***
Documentation     Escenaris
Library           Selenium2Library

*** Variables ***
${BROWSER_URL}  http://127.0.0.1:8000


#NOM I LLINATGES, DATA NAIXEMENT, DIRECCIO, CONTRASENYA, EMAIL, TELEFON
@{PERSONALDATA}     Nom Llinatge Llinatge   30/11/2000  S'Esgleieta, 12, Palma  exemplecontrasenya  exemple4@exemple.com   971234567

*** Keywords ***

Tanca Test
    Sleep   2s
    Close Browser