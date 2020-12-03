# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:29:29 2020

@author: alessiosca
"""



from pywebcopy import save_webpage
print('ATTENZIONE:\nQUESTO PROGRAMMA FUNZIONA BENE SOLO CON SITI STATICI.\n')
sito=input('Quale sito vuoi rubare? (includi "http:// o https://") \n')
cartella=input('In quale cartella lo vuoi scaricare? (INVIO per scaricarlo in C:/).\n')
slash=sito.find('/')
nomesito=sito[slash+1:]
url = sito
download_folder = cartella

kwargs = {'bypass_robots': True, 'project_name': nomesito}

save_webpage(url, download_folder, **kwargs)
