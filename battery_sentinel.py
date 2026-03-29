import time # Libraty time untuk jeda

print("Baterai sentinel (tekan 'X^C' untuk benhenti)")

# Path dari log batterai linux
path_baterai = "/sys/class/power_supply/BAT0/capacity"
path_charger = "/sys/class/power_supply/AC/online"

# Membuka file dengan mode 'r'
while True: 
    try:
        with open(path_baterai, 'r') as file_baterai: # Gunakan with open (jangan langsung open biar aman)
            angka_baterai = int(file_baterai.read().strip()) # Baca seluruh file lalu strip

        with open(path_charger, 'r') as file_charger:
            status_charger = int(file_charger.read().strip())

    except FileNotFoundError:
            angka_baterai = 0
            status_charger = 0
            print("Battery not Found Error")

    status_baterai = f"Baterai: {angka_baterai} | Charger: {'YA' if status_charger else 'TIDAK'}"

    if angka_baterai < 20 and not status_charger:
        pesan = "Tolong Sambungkan Charger"

    elif angka_baterai > 80 and status_charger:
        pesan = "Baterai diatas 80% Cabut Charger Sekarang!!"
    
    else:
        pesan = "Harusnya teks ini tidak muncul"
    
    print(f"{status_baterai} {pesan}           ", end='\r')

    time.sleep(5) # Delay 5 detik