import os

banner = """
──────╔╗──╔╗────╔╗───────────────╔╗
╔╦╦═╦╦╣╚╦╦╣╚╦═╗╔╝╠═╦╦╦╦═╦╦╗╔═╦═╗╔╝║
║║║╬║║║╔╣║║╬║╩╣║╬║╬║║║║║║║╚╣╬║╬╚╣╬║
╠╗╠═╩═╩═╩═╩═╩═╝╚═╩═╩══╩╩═╩═╩═╩══╩═╝
╚═╝

     [!] Youtube-Download V.1
     [!] By : 4NDR0 R4T
     [!] www.hidayatcode.com
"""
print(banner)
x = input("Masukan Link Playlist Anda: ")
os.system(f"youtube-dl {x}")