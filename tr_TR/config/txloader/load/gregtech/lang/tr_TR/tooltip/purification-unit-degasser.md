{aqua:{bold:Su Kademesi: }}{color_tier:{var:tier}}
Çalışması için bir Arıtma Tesisi'ne {color_name:{item:gregtech:gt.metaitem.01:32708}} kullanarak bağlanmalı
{hr}
İşlem başlarken {color_name:{var:control_hatch}} bir kızıltaş sinyali verecek
Tarifin başarılı olması için sinyaldeki talimatları başarıyla çözmen gerekir
Sinyali çözmek için sinyal gücünü 0-15 arasında 4 bitlik bir sayı olarak yorumla
En düşük biti bit 1, en yükseğini bit 4 olarak adlandır
{hr}
{white:{bold:Bit 1: }}{color_misc:{bold:İnert Gaz ile Ozon Gazlama}}
Bu bit açıksa makineye bir {color_name:asal gaz} eklemelisin
Hangi gazı ekleyeceğini belirlemek için {color_misc:2-3} bitlerini 2 bitlik bir sayı olarak yorumla
0: {white:{var:gas0_amount} {L} {var:gas0}} / 1: {white:{var:gas1_amount} {L} {var:gas1}} / 2: {white:{var:gas2_amount} {L} {var:gas2}} / 3: {white:{var:gas3_amount} {L} {var:gas3}}
{hr}
{white:{bold:Bit 2: }}{color_misc:{bold:Süper İletken Deiyonizasyon}}
Bu bit açıksa {white:{var:supercon_amount} {L}} kadar {white:Eriyik Süper İletken Baz} eklemelisin
Daha yüksek kademe süper iletken kullanmak bonus çıktı sağlar
Çıktı çarpanı: {tier-color-name:tier0}: {white:{var:mult0}x} / {tier-color-name:tier1}: {white:{var:mult1}x} / {tier-color-name:tier2}: {white:{var:mult2}x} / {tier-color-name:tier3}: {white:{var:mult3}x} / {tier-color-name:tier4}: {white:{var:mult4}x}
{hr}
{white:{bold:Bit 3: }}{color_misc:{bold:Yerçekimiyle Üretilen Diferansiyel Vakum Ekstraksiyonu}}
Bu bit açıksa {white:{var:catalyst_amount} {L}} kadar {white:{var:catalyst}} eklemelisin
{hr}
{white:{bold:Bit 4: }}{color_misc:{bold:Seldonian Çökelme Süreci}}
Bu bit açıksa diğer tüm bitleri {color_note:YOK SAY} ve hiçbir şey ekleme
{hr}
{white:{bold:Bit yok: }}{color_misc:{bold:Makine Aşırı Yüklenmesi}}
Nadir durumlarda makine aşırı yüklenebilir ve hiç kontrol sinyali vermeyebilir
Makine hasarını önlemek için {color_cold:{var:coolant_amount} {L}} kadar {color_cold:{var:coolant}} ekle
{hr}
Tarif ancak sinyalin tamamı doğru şekilde çözülürse başarılı olabilir
Sinyalin istemediği herhangi bir sıvıyı eklemek tarifi her zaman geçersiz kılar
{hr}
{aqua:{italic:Su arıtımının sondan bir önceki aşaması olan yedinci adım, önceki adımlardaki kir gidericilerin bıraktığı}}
{aqua:{italic:herhangi bir enerjik iyon, asit, durulaştırıcı veya gaz gibi kalıntı materyalleri temizlemek için}}
{aqua:{italic:tasarlanmış düzensiz bir dizi karmaşık süreçtir. Gaz Giderici'nin suda ne tespit ettiğine bağlı olarak,}}
{aqua:{italic:yukarıda listelenen süreçleri tamamlamak için çeşitli materyaller isteyecektir.}}