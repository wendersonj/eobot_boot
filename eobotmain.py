#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 09:49:14 2017

@author: wenderson

"""
from EobotAPI import EoBot
from __maker_login_file import make

try:
    with open("login_file", "r") as login_file:
        login_file = open("login_file", "r")
        dados=login_file.readlines()
        user = []
        for line in dados:
            user = line.split(";")
        login_file.close()
except IOError:
    print("Login_File não existe ! Executando maker ...\n")
    make()
    
#Cria o objeto
wjs = EoBot(user[0], user[1])
#Linha de Debugger da API
#wjs.set_debug(1)

saldoDOGE = wjs.get_coin_balance("DOGE")
print("Saldo disponível em DOGE:" + saldoDOGE)

if(str(input("\nQuer transferir todo o saldo de DOGE para a CLOUD ? (s/n): ")) == "s"):
        wjs.exchange_currency("DOGE", "GHS4", saldoDOGE)

#print(wjs.get_mining_coin())
