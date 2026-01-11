#Kullanıcıdan gerekli bilgileri alınız
ad_soyad= input("Adinizi ve soyadinizi nedir?")
bio= input("Kisaca kendinizi tanitir misiniz?")
dersler= input("Hangi dersleri aliyorsunuz? (virgülle ayirin):")

#Kullanıcının aldığı dersleri listele ve virgülle ayır
ders_liste= dersler.split(",")

#HTML için ders listesini olusturuyoruz
ders_html = ""

#Dersleri <li> etiketine icine alıyoruz
for ders in ders_liste:
    ders_html += "<li>" + ders.strip() +"</li>\n"

#HTML sayfasını string olarak olusturuyoruz
html= f"""
<!DOCTYPE html>
<html> 
<head>
  <meta charset="UTF-8">
  <title>Kisisel Sayfa</title>

  <!-- Basit CSS ile sayfa renklendirme --> 
  <style> 
    body {{ 
          background-color: lightyellow; 
          }}
    h1 {{ 
        color: darkblue; 
        }}
    h3{{
       color: blueviolet;
    }}
  </style>
</head<
</body>
    <!--Kullanicinin adi baslik olrak yazdir-->
    <h1>{ad_soyad}</h1>

    <!--Kullanicinin biyografi bilgisi yazdir-->
    <p>{bio}</p>

    <!--Kullanicinin aldigi dersleri liste halinde yazdir-->
    <h3>Alinan Dersler</h3>
    <ul>
      {ders_html}
    </ul>
</body>
</html>
"""

# HTML içeriğini index.html adlı dosyaya yazıyoruz
dosya = open("index.html", "w", encoding="utf-8")
dosya.write(html)
dosya.close()

#Programın başarıyla bittiğini ekrana yazzdırıyoruz
print("index.html olusturuldu")
