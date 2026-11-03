---
navigation:
  title: Arayüz Terminali Değişiklikleri
  parent: ae2.md
  icon: appliedenergistics2:item.ItemMultiPart:480
categories:
    - Applied Energistics 2
author: Skorched
date: 2026-05-27
---

# Arayüz Terminali Değişiklikleri
Onlarca arayüze sahip büyük bir ME ağını yönetmek her zaman bir tür tahmin oyunu olmuştur. Her şey aynı görünür ve dağınıklık neredeyse kaçınılmazdır. Bununla mücadele etmek için aşağıdaki değişiklikler yapıldı:
- __Bölüm başlıklarında Blok Simgeleri__: Artık her arayüz grubu, gerçek arayüz bloğunun küçük bir simgesini gösterir; böylece Normal <ItemImage id="appliedenergistics2:tile.BlockInterface"/> ile Çift <ItemImage id="ae2fc:fluid_interface"/> Arayüzler arasında bir bakışta ayrım yapabilirsin.
- __Öncelik İpuçları__: Arayüz simgesinin üzerine gelerek bloğun adını, geçerli önceliği ve o grupta kaç arayüz olduğunu görebilirsin
- __Yanlış Türde Kalıp Vurgulama__: Yanlışlıkla normal bir ME Arayüzüne sıvı kalıbı koyarsan, yuva hem ME Arayüzü GUI'sinde hem de Arayüz Terminalinde kırmızı yanar
- __Arayüzleri Terminalden Gizle__: Herhangi bir arayüz girişindeki vurgulama düğmesine Alt + Tıklayarak görünürlüğünü aç/kapat. Onları gizlemenin önceki yönteminde olduğu gibi, hâlâ ağına bağlıdırlar; sadece dağınıklıktan gizlenmişlerdir!
- __Gizlileri Göster Anahtarı__: Yeni bir kenar çubuğu düğmesi, tüm gizli arayüzleri tek seferde göstermene olanak tanır; böylece her birine tek tek gitmeden onları yönetebilirsin
- __Hayalet Devreler ve Tüketilmeyenler__: GT Makineleri ve Üretim Giriş Yolu/Tamponları artık tarif yapılandırmalarını terminal adına şu şekilde dahil ediyor: <Color id="GREEN">_Makine Adı_ [24] {Ekstrüder Şekli (Çubuk)}</Color>. Bu, `config/GregTech/Machines` içinde tamamen yapılandırılabilir