# Kodlama: Evrim Altay KOLUAÇIK
# https://evrimaltay.net
# 17.04.2020
import random
import numbers
from time import sleep
bakiye = 100
while True:
	isim = input('İsim ver hacı: ')
	if isim:
		break
	else:
		print('İsmini yazsana lan.')
sleep(0.8)
print('\n\nHeyt ' + isim + ' gelmiş hoş gelmiş.')
sleep(0.8)
print('Sana bizden bir ' + str(bakiye) + '₺ çalışır.')
sleep(0.8)
print('Doya doya harca.')
sleep(0.5)
print('Hepsini kaptırırsan da ağlama.')
sleep(0.8)
while True:
		sleep(0.5)
		print('\n')
		print('*'*45)
		print('Şu Anki Bakiyen:' +str(bakiye)+'₺')
		oyunuBitir = False
		sistemTahmini = random.choice(('yazı', 'tura'))
		while True and bakiye > 0:
			bahisMiktarı = input('Bir bahis yap veya çıkış yapmak için çık yaz: ')
			try:
				bahisMiktarı = int(bahisMiktarı)
			except ValueError:
				oyunuBitir = True
				break
			if bahisMiktarı > bakiye:
				print('Lan Fakir sende o para ne gezer. Adam gibi bahis yap.') 
			else:
				sleep(0.3)
				print(str(bahisMiktarı) + '₺ bahis yapıldı.')
				break
		
		if bakiye <= 0:
			oyunuBitir = True

		if oyunuBitir:
			break

		while True:
			kullanıcıTahmini = input('Tahminini yap (yazı/tura): ')
			if kullanıcıTahmini in ('yazı', 'tura'):
				break
			else:
				print('Sadece (yazı/tura) yaz, adamın asabını bozma.')
		sleep(0.8)
		if kullanıcıTahmini == sistemTahmini:
			bakiye += bahisMiktarı
			print('Tebrikler amcık '+str(bahisMiktarı)+'₺ kazandın. Yeni bakiyen: '+str(bakiye)+'₺')
		else:
			bakiye -= bahisMiktarı
			print('Sende şans ne gezer göt. '+str(bahisMiktarı)+'₺ kaybettin. Yeni bakiyen: '+str(bakiye)+'₺')
sleep(0.8)
if bakiye > 0:
	print('\nGörüşürüz. ' + str(bakiye) + '₺ ile oyunu bitirdin. Bidahaki sefere acımaz yolarız ha.')
else:
	print('\nKoyduk mu!!! Hadi şimdi git anana ağla.')
		
		
	
