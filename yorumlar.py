from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # tuş basma
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tr.tradingview.com/script/pEckhHhg/")
basla = input("başlamak için enter")
yorumlar = driver.find_elements('class name',"comment-list-OcIQpQ2F")
veri = yorumlar[0].text.split('Cevap Gönder')
yorumcuListesi = []
for i in veri:
    boluk = i.splitlines()
    if len(boluk) > 0 :
        kid = boluk[1] if boluk[0]== '' else boluk[0]
        if kid not in yorumcuListesi:
            yorumcuListesi.append(kid)
   
yorumcuListesi.remove('only_fibonacci') #only_fibonacci listeden sil
print("Yorumcular : ")
for x in yorumcuListesi:
    print(x)

print("########################")
print(f"Yorumcu Sayısı : {len(yorumcuListesi)}")
print("########################")

kazanacakSayisi = input("Kazanacak Kişi Sayısı : ")
kazananListesi = []

while True : 
    kazanan = random.choice(yorumcuListesi)
    if kazanan not in kazananListesi:
        kazananListesi.append(kazanan)
        print(f"Kazanan : {kazanan}")
        print(f"Link : https://tr.tradingview.com/u/{kazanan}")
    if len(kazananListesi) == int(kazanacakSayisi):
        break
