import os

banner = """
──────╔╗──╔╗────╔╗───────────────╔╗
╔╦╦═╦╦╣╚╦╦╣╚╦═╗╔╝╠═╦╦╦╦═╦╦╗╔═╦═╗╔╝║
║║║╬║║║╔╣║║╬║╩╣║╬║╬║║║║║║║╚╣╬║╬╚╣╬║
╠╗╠═╩═╩═╩═╩═╩═╝╚═╩═╩══╩╩═╩═╩═╩══╩═╝
╚═╝

     [!] Youtube-Download V.1
     [!] By : X3NUX
     [!] www.niasxploit.com
"""
print(banner)
x = input("Masukan Link Playlist Anda: ")
os.system(f"youtube-dl {x}")
