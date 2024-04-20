from PyQt5 import uic
def dosyaAdiniDuzenle(dosyaadi):
    uzunluk = len(dosyaadi) - 3
    yeniad=""
    for i in dosyaadi:
        if(i=="."):
            break
        yeniad+=i
        
    yeniad+=".py"
    return yeniad


dosya_adi = input("aynı klasörde bulunan ui dosyasının adını uzantısıyla birlikte girin(örnek : sexy-ui.ui):")
with open(f"{dosyaAdiniDuzenle(dosya_adi)}","w",encoding="utf-8") as fout:
    uic.compileUi(dosya_adi,fout)



