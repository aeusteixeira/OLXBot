"""
Bot Selenium - Busca de imóveis no site OLX

Objetivo:
- Acessar o site da OLX
- Realizar busca por termo e local
- Coletar dados dos anúncios
- Salvar os dados em JSON

Autor: Matheus Teixeira
Data: 19/04/2025
"""

from app.OLXBot import OLXBot
import time

if __name__ == "__main__":

    print("""
                    
            ░█████╗░██╗░░░░░██╗░░██╗  ██████╗░░█████╗░████████╗
            ██╔══██╗██║░░░░░╚██╗██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝
            ██║░░██║██║░░░░░░╚███╔╝░  ██████╦╝██║░░██║░░░██║░░░
            ██║░░██║██║░░░░░░██╔██╗░  ██╔══██╗██║░░██║░░░██║░░░
            ╚█████╔╝███████╗██╔╝╚██╗  ██████╦╝╚█████╔╝░░░██║░░░
            ░╚════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
    """)

    print("O que você deseja buscar?")
    termo = input()

    print("Em qual local?")
    local = input()

    print("Iniciando busca...")

    bot = OLXBot(termo, local)
    bot.acessar_site()
    bot.realizar_busca()
    bot.mudar_localizacao()
    anuncios = bot.coletar_anuncios()
    bot.salvar_json(anuncios)
    time.sleep(3)
    bot.encerrar()
