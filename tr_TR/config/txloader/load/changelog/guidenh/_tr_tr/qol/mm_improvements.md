---
navigation:
  title: Madde Manipülatörü İyileştirmeleri
  parent: qol.md
  icon: matter-manipulator:itemMatterManipulator3
categories:
    - Quality Of Life
author: Skorched
date: 2026-05-16
---

# Madde Manipülatörü İyileştirmeleri
<Color id="GREEN">Madde Manipülatörü</Color> <ItemImage id="matter-manipulator:itemMatterManipulator3" /> öğesinin çalışma biçiminde birkaç hoş değişiklik yapıldı! Aşağıda bunlar açıklanıyor

# Gelişmiş Kopyalama Seçenekleri (Akıllı Kopyalama)
Kopyala/Yapıştır radyal menüsü artık üç yeni anahtar içeren bir <Color id="BLUE">__Gelişmiş Seçenekler__</Color> alt menüsüyle geliyor:
- __Harici Merkezlere Bağla (MKII+)__: Kopyalanan bölgenin _dışındaki_ bir merkeze bağlı kablosuz bağlayıcıları kopyalarken, yapıştırılan bağlayıcılar o merkeze bağlı kalır!
- __Otomatik P2P Arayüzleri (MKII+)__: ME arayüzlerini P2P ME Arayüz tünelleriyle değiştirir. Kaynak "giriş tarafı" tüneli alır, yapıştırılan sürüm ise "çıkış tarafı" tünelini alır ve frekanslar otomatik olarak eşleştirilir. Kalıplar kaynakta kalır, böylece hepsi o tek kalıp setine yönlenen işleme düzeneklerini çoğaltabilirsin! (Bu, Sıvı P2P Arayüz tünelleriyle de çalışır)
- __Otomatik Proxy CRIB'ler (MKIII)__: Kopyalanan yapıdaki <Color id="RED">Üretim Giriş Veriyollarını</Color>, özgün veriyoluna geri bağlanan <Color id="BLUE">Üretim Giriş Proxileri</Color> ile değiştirir! Yine bağlantı otomatiktir!

<FloatingImage src="../assets/qol/mm_smart.png" wrap="square" align="left" displayWidth="256">
  <ImageAnnotation>
    Yeni Akıllı Kopyalama menüsü
  </ImageAnnotation>
</FloatingImage>
<br clear="all"/>
# Dekoratif Blok Desteği
Marangozun Blokları, Project Red veya Forge Microblocks tutkunuysan, <Color id="GREEN">Madde Manipülatörü</Color> artık onları tamamen destekliyor!

Bu blokları kopyalayıp yapıştırmak geçmişte bir türlü doğru yapılamıyordu, ama artık yalnızca yönlerini korumakla kalmayacak, dekoratif kaplamalarını da koruyacaklar!

## OpenComputers Kablo Desteği
Kablo Modu artık OpenComputers kablolarıyla çalışıyor. Bir kabloyu seçmek için sağ tıkla, sonra tıpkı GregTech/Applied Energistics kablolarında olduğu gibi çizgi çizmeye başla!