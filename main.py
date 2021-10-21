# Önce bir sözlük kurduk, ve burada Türkçe isimleri kullanıyoruz.
# Buradaki veri yapısı bir 'tuple' listesi, yani değer çiftleridir.
# Python aslında sadece bu tür anahtar/değer aramasını verimli bir şekilde yapmak için yerleşik bir 'sözlük' veri yapısına sahiptir, ancak onu burada kullanmıyoruz.

sozlukdb = [
("alev","Yanan maddelerin veya gazların türlü biçimlerdeki ışıklı uzantısı, yalım, yalaz, alaz, şule"),
("bedel","Bir şeyin yerini tutabilen karşılık"),
("ciddi","Şaka olmayan, gerçek"),
("çentik","Bir şeyin kenarından kesilerek veya kırılarak açılan küçük kertik, tırtık"),
("deniz","Yer kabuğunun çukur bölümlerini kaplayan, birbiriyle bağlantılı, tuzlu su kütlesi."),
("erdem","Ahlakın övdüğü iyi olma, alçak gönüllülük, yiğitlik, doğruluk vb. niteliklerin genel adı, fazilet"),
("far","Taşıtların ön bölümünde bulunan, kısa ve uzun mesafeyi aydınlatmaya yarayan ışık düzeneği"),
("gemi","Su üstünde yüzen, insan ve yük taşımaya yarayan büyük taşıt, sefine"),
("ğ","Bunu kimse bulamaz :D"),
("halı","Yere veya mobilya üstüne serilmek, duvara gerilmek için, genellikle yünden dokunan, kısa ve sık tüylü, nakışlı, kalın yaygı"),
("ıslak","Suya batırılmış, üzerine su dökülmüş veya yağmurdan ıslanmış olan"),
("ilmek","Çözülmesi kolay düğüm, eğreti düğüm, ilmik"),
("jaguar","Kedigillerden, Orta ve Güney Amerika'da yaşayan, postu iri benekli bir tür memeli (Felis onca)."),
("keder","Acı, üzüntü, dert, sıkıntı, ızdırap, tasa"),
("lale","Zambakgillerden, yaprakları uzun ve sivri, çiçekleri kadeh biçiminde, türlü renkte bir süs bitkisi (Tulipa gesneriana)."),
("mezar","Ölünün gömülü olduğu yer, gömüt, kabir, sin(I), makber, metfen"),
("nardin","Maydanozgillerden, çayırlarda yetişen ve hayvanlara yem olarak verilen, başakçıkları tek çiçekli küçük bir bitki (Eryngium campestre)."),
("okaliptus","Mersingillerden, asıl yurdu Avustralya olan, boyu 100 metreyi aşabilen, toprağın suyunu çekerek yerin bataklık duruma gelmesini önleyen bir ağaç, sıtma ağacı (Eucalyptus globulus)."),
("ödev","Yapılması, yerine getirilmesi, insanlık duygusu, töre ve yasa bakımından gerekli olan iş veya davranış, vazife, vecibe"),
("perde","Görüşü, ışığı engellemek, bir şeyi gizlemek için pencereye veya bir açıklığın önüne gerilen örtü"),
("ralli","Yarışmacıların otomobille belli yolları izleyerek ve özel kurallara uyarak belirli bir yere ulaşmalarına dayanan otomobil yarışı."),
("sal","Birçok kalın direk yan yana bağlanarak yapılan, düz ve korkuluksuz deniz veya ırmak taşıtı"),
("şerit","Dar, uzun dokuma veya kumaş parçası"),
("tatlı","Acı olmayan, acı karşıtı"),
("uzak","Gidilmesi çok süren, çok ötelerde bulunan, ırak, yakın karşıtı"),
("üzüm","Asmanın taze veya kuru olarak yenilen ve salkım durumunda bulunan meyvesi."),
("veranda","Üstü kapalı ve çevresi camlı balkon"),
("yaprak","Bitkilerde solunum, karbon özümlenmesi, terleme vb. olayların oluştuğu, çoğu klorofilli, yeşil ve türlü biçimdeki bölümler"),
("zengin","Maddi anlamda parası çok olan kimse."),
("gürkan","Gürkan Tunca Youtube Kanalı: https://www.youtube.com/channel/UC5kRwyEszwFEybZscMnvGzw")
]

# Ask the user what they'd like to translate:
# Kullanıcıya neyi çevirmek istediğini sorun:

kelime = input('Neyi tercüme etmemi istersin?')

# A simple linear search through the sozlukdb (note, not in alphabetical order yet)
# Sözlükte basit bir doğrusal arama (not, henüz alfabetik sıraya göre değil)

for origin,hedef in sozlukdb:
    if origin == kelime:
        print (hedef)
        
# Now for the binary search:
# Şimdi ikili arama için:

sozlukdb.sort() 
# Binary search only works if the keys are in order, and putting a list into order takes time
# İkili arama yalnızca tuşlar sıralıysa çalışır ve bir listeyi sıraya koymak zaman alır

lower = 1
upper = len(sozlukdb)-1
found = False 
# this allows us to leave the loop as soon as we've found the word we're looking for
# bu, aradığımız kelimeyi bulur bulmaz döngüden çıkmamızı sağlar.

while lower <= upper and not found:
    midpoint = (lower + upper) // 2 
    # the // does whole number division
    # // tam sayı bölümü yapar
    origin,hedef = sozlukdb[midpoint]
#  print(lower,upper,midpoint,origin) # remove the comment at the beginning here to see what it does at each step
# her adımda ne yaptığını görmek için burada başlangıçtaki yorumu kaldırın
    if origin == kelime:
        found = True
    else:
        if origin > kelime:
            upper = midpoint - 1 # if the word we checked is after my word, only look before it
            # kontrol ettiğimiz kelime benim sözümden sonraysa, sadece ondan önce bak anlamına geliyor kelime
        else:
            lower = midpoint + 1 # if the word we checked is before my word, only look after it
            # kontrol ettiğimiz kelime benim sözümden önceyse, sadece ona bak demek oluyor.

if found:
    print(hedef)
#else:
   # print("Aradığınız Sözcük {sozlukdb} İçinde Bulunamadı.")

