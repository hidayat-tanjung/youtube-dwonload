import os
from colorama import init, Fore, Back, Style

# Inisialisasi colorama
init(autoreset=True)

banner = f"""
{Fore.YELLOW}▖▖▄▖ ▄ ▖  ▄▖▄▖▖ ▖▖▖▄▖▄▖▄▖
{Fore.CYAN}▌▌▐▄▖▌▌▌  ▌ ▌▌▛▖▌▌▌▙▖▙▘▐ 
{Fore.MAGENTA}▐ ▐  ▙▘▙▖ ▙▖▙▌▌▝▌▚▘▙▖▌▌▐{Style.RESET_ALL}

{Fore.WHITE}{Back.BLUE}  YouTube Downloader V3  {Style.RESET_ALL}
{Fore.YELLOW}  By: IZUMY
{Fore.CYAN}  Youtube.com/@izumy-n4o
"""

print(banner)

def check_dependencies():
    """Memeriksa dan menginstall dependensi"""
    required = ['yt-dlp', 'ffmpeg-python', 'colorama']
    print(f"\n{Fore.YELLOW}🔍 Memeriksa dependensi...{Style.RESET_ALL}")
    
    for package in required:
        try:
            __import__(package)
            print(f"{Fore.GREEN}✓ {package} terinstall{Style.RESET_ALL}")
        except ImportError:
            print(f"{Fore.RED}✗ {package} belum terinstall{Style.RESET_ALL}")
            os.system(f"pip install {package}")

check_dependencies()

# Menu utama
print(f"\n{Fore.CYAN}🎵 Pilihan Format:{Style.RESET_ALL}")
print(f"{Fore.YELLOW}[1]{Style.RESET_ALL} Video (MP4 720p)")
print(f"{Fore.YELLOW}[2]{Style.RESET_ALL} Video (MP4 1080p)")
print(f"{Fore.YELLOW}[3]{Style.RESET_ALL} Audio (MP3 320kbps)")
print(f"{Fore.YELLOW}[4]{Style.RESET_ALL} Playlist (Semua Video)")

choice = input(f"\n{Fore.GREEN}▸ Pilih opsi (1-4): {Style.RESET_ALL}")
url = input(f"{Fore.BLUE}▸ Masukkan URL: {Style.RESET_ALL}")

if choice == "1":
    print(f"\n{Fore.GREEN}⬇️ Mengunduh MP4 720p...{Style.RESET_ALL}")
    os.system(f'yt-dlp -f "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]" "{url}"')
elif choice == "2":
    print(f"\n{Fore.GREEN}⬇️ Mengunduh MP4 1080p...{Style.RESET_ALL}")
    os.system(f'yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]" "{url}"')
elif choice == "3":
    print(f"\n{Fore.GREEN}⬇️ Mengkonversi ke MP3...{Style.RESET_ALL}")
    os.system(f'yt-dlp -x --audio-format mp3 --audio-quality 320K "{url}"')
elif choice == "4":
    print(f"\n{Fore.GREEN}⬇️ Mengunduh playlist...{Style.RESET_ALL}")
    os.system(f'yt-dlp -o "%(playlist_index)s - %(title)s.%(ext)s" "{url}"')
else:
    print(f"\n{Fore.RED}❌ Pilihan tidak valid!{Style.RESET_ALL}")

print(f"\n{Fore.GREEN}✅ Selesai! File tersimpan di:{Style.RESET_ALL}")
print(f"{Fore.WHITE}{os.getcwd()}{Style.RESET_ALL}")
