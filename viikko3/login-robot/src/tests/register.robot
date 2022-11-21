*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  seppo  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long and contain only lowercase letters

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  ka
    Output Should Contain  Password must be at least 8 characters long and contain at least one non-letter character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  kalleasdasd
    Output Should Contain  Password must be at least 8 characters long and contain at least one non-letter character

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123