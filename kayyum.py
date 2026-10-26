#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayyum Kararı Üretici v1.0
Dünyanın en gereksiz ama en eğlenceli hukuki yazılımı.
Kullanım: python kayyum.py
"""

import random
import time

def kayyum_karari_uret():
    kurbanlar = [
        "Twitter hesabı",
        "GitHub profili",
        "Kedi mama kabı",
        "Buzdolabındaki son ayran",
        "Komşunun WiFi şifresi",
        "Kaynananın salça kavanozu",
        "Eski sevgilinin Spotify çalma listesi",
        "Devlet dairesindeki çay ocağı"
    ]
    
    gerekceler = [
        "çok fazla 'abi' demesi sebebiyle",
        "çayı şekersiz içmesi yüzünden",
        "kahvaltıda peynir yerine sucuk yemesi dolayısıyla",
        "trafikte selektör yapmaması nedeniyle",
        "WhatsApp'ta 'tamam' yazması sonucu",
        "fatura ödemeyi unutması yüzünden",
        "kediye 'oğlum' demesi sebebiyle",
        "GitHub'a saçma repo açması dolayısıyla"
    ]
    
    kararlar = [
        "hesaba kayyum atanmasına",
        "tüm şifrelerin değiştirilmesine",
        "çay ocağının mühürlenmesine",
        "ayranın devlet malı ilan edilmesine",
        "kedinin yasal vasisi olmaya",
        "WiFi şifresinin '12345678' yapılmasına"
    ]
    
    kurban = random.choice(kurbanlar)
    gerekce = random.choice(gerekceler)
    karar = random.choice(kararlar)
    
    print("\n" + "="*50)
    print("     RESMİ KAYYUM KARARI")
    print("="*50)
    print(f"\n{kurban.upper()} üzerinde {gerekce}")
    print(f"{karar} karar verilmiştir.")
    print("\nBu karar kesindir, itiraz edilemez, çayı da bitmiştir.")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("Kayyum kararı üretiliyor... Mahkeme heyeti toplanıyor...")
    time.sleep(2)
    kayyum_karari_uret()
    print("Karar uygulandı. İyi günler dileriz. (veya dilemeyiz)")
