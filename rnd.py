# -*- coding: utf-8 -*-
import os
import argparse
import random
import string
import sys

_2x_metni = u"""**********************************************************
**		!!! KRİTİK HATA !!!			**
** Python'ın 2.x sürümlerinden birini kullanıyorsunuz. 	**
** Programı çalıştırabilmek için sisteminizde Python'ın	**
** 3.x sürümlerinden biri kurulu olmalı.		**
**********************************************************"""

if sys.version_info.major < 3 :
	print (_2x_metni)
	sys.exit()
p = argparse.ArgumentParser(description="Rastgele Sayı&Parola Oluşturucu, \nEvrim Altay KOLUAÇIK tarafından oluşturulmuştur.\nDestek @ https://evrimaltay.net/pyparola")
p.add_argument('-u','--uzunluk', help='Oluşacak ürünlerin karakter uzunluğu. (Varsayılan: 10)', default=10, type=int)
p.add_argument('-a','--adet', help='Kaç adet ürün oluşacak. (Varsayılan: 3)',default=3, type=int)
p.add_argument('-t','--tip', help='Ürünlerin karakter tipi ne olacak (Varsayılan: hs)', default='hs', choices= ['h','s','hs','t'])

a = p.parse_args()
chars = {
'h' : string.ascii_letters,
's' : string.digits,
'hs': string.ascii_letters + string.digits,
't' : string.ascii_letters + string.digits + '%+-_!@.',
}

for i in range(int(a.adet)) :
	print(''.join(random.choice(chars[a.tip]) for i in range(int(a.uzunluk))))
raise SystemExit
