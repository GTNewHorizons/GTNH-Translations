---
navigation:
  title: "Kademe Atlama, Overclock ve Paralel İşlemler"
  icon: OpenComputers:item:27
  parent: /index.md
---

# Kademe Atlama, Overclock ve Paralel İşlemler


Multiblok makinelerin davranışı şu temel kavramlarla belirlenir: **[kademe atlama](tierskipping.md)**, **[overclock](overclocking.md)**, **[paralel işlemler](parallels.md)** ve bu sayfada ele alınan **nominal güç** ile **gerilim kademesi**.

**[Kademe atlama](tierskipping.md)**, bir multibloğun daha yüksek temel tarif gücüne sahip tarifleri çalıştırmak için genellikle aynı kademeden iki Enerji Kapağı takarak daha düşük kademeli Enerji Kapaklarını kullanabilme yeteneğidir.

**[Overclock](overclocking.md)**, makinenin bir tarifi daha kısa sürede tamamlayabilmesi için nominal gücü artırmak anlamına gelir. Çoğu durumda bu 4/2 kusurlu overclock kullanır, ancak bazı makineler 4/4 kusursuz overclock destekler.

**[Paralel işlemler](parallels.md)**, bir multiblok makinenin aynı zaman aralığında aynı tarifin birden fazla kopyasını işleyebilme yeteneğidir.

# Tarifler ve Güç

Her tarifin bir **temel tarif gücü** vardır; bu, NEI'de overclock'tan ve herhangi bir indirim uygulanmadan önce gösterilen güçtür. <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:687" showIcon="left" /> gibi birçok multiblok tariflere özel güç indirimleri uygulayabilir. İndirimlerden sonra ancak overclock'tan önceki güce **gerçek tarif gücü** denir. İpuçları "tarif kademesi"nden bahsettiğinde gerçek tarif gücünü değil, temel tarif gücünü kasteder.

# Nominal Güç

**Nominal güç**, makinenin çalışırken tüketebileceği maksimum güçtür. **[Overclock](overclocking.md)** ve **[paralel işlemler](parallels.md)** için birincil girdidir. Hem makinenin bir tarifi çalıştırıp çalıştıramayacağını hem de o tarifi nasıl çalıştıracağını belirler. Nominal güç ve gerilim kademesi makinenin kendi özellikleridir ve yerel güç ağındaki enerji paketi taşıma kurallarından bağımsızdır.

## Bir Tarifi Başlatmak İçin Gereken Koşullar

Makine bir tarifi yalnızca **nominal güç >= gerçek tarif gücü** ve **gerilim kademesi >= temel tarif gücü** ise başlatabilir.

- Nominal güç çok düşük -> kontrolcü "Tarif daha fazla güç gerektiriyor." bildirir.
- Gerilim kademesi çok düşük -> kontrolcü "Tarif başlamak için daha yüksek gerilim gerektiriyor." bildirir.

## Tek Bloklu Makineler

Tek bloklu makineler genellikle 1A x standart gerilime eşit nominal güce sahiptir. İstisnalar arasında 2A ile Termal Santrifüj, 3A ile Ark Fırını ve tüketilen akımı farklı gerilim seviyelerine göre 8A'dan 1A'nın altına kadar değişen tek bloklu Kütle İmalatçısı bulunur.

## Multiblok Makineler

Multibloklar, bir veya birkaç Enerji Kapağı kullanmalarına göre nominal gücü farklı hesaplar. Standart bir Enerji Kapağı, 2A x standart gerilime eşit nominal güce sahiptir. Çok Amperli veya Lazer Kapağı, amperajı x standart gerilime eşit nominal güce sahiptir.

- **Yalnızca bir Enerji Kapağı takılı**: çoğu makinede nominal güç = 1A x standart gerilim, yani Enerji Kapağının nominal gücünün yarısıdır. Çok Amperli veya Lazer Kapaklarını doğrudan destekleyen bazı makineler kapağın tam nominal gücünü kullanır.
- **Birden fazla Enerji Kapağı takılı**: nominal güç, tüm Enerji Kapaklarının nominal güçlerinin toplamıdır.

Yalnızca bir Enerji Kapağı takılıyken makinenin gerilim kademesi genellikle nominal gücünün bir kademe üstündedir; bu 4 katlık bir farktır. Bu, makinenin o daha yüksek gerilim kademesindeki tarifleri çalıştırmak için hâlâ yeterli nominal güçten yoksun olduğu anlamına gelir. Eksik nominal gücü telafi etmek için aynı kademeden daha fazla Enerji Kapağı yerleştirirsin; buna **[kademe atlama](tierskipping.md)** denir. Aynı kademeden iki standart Enerji Kapağı takmak nominal gücü gerilim kademesine eşitler; buna **çift kapaklı kademe atlama** denir.

# Gerilim Kademesi

**Gerilim kademesi**, makinenin çalıştırmasına izin verilen en yüksek temel tarif gücüdür. Nominal güçle birlikte yalnızca bir tarifin başlatılmasına izin verilip verilmediğini etkiler. Gerilim kademesinin **[overclock](overclocking.md)** ile hiçbir ilgisi yoktur.

## Tek Bloklu Makineler

Gerilim kademeleri nominal güçleriyle aynıdır.

## Multiblok Makineler

Multibloklar için dört farklı gerilim kademesi davranışı vardır:

| Davranış | Açıklama | Tipik Makineler |
|----------|-------------|------------------|
| **Bir kademe artış** | 4A x ortalama Enerji Kapağı gerilimi. Bu, çoğu makine için varsayılan davranıştır. | Elektrikli Yüksek Fırın ve çoğu diğerleri |
| **Artış yok** | 1A x Enerji Kapağı gerilimi | <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:32018" showIcon="left" /> |
| **Bir kademe azalma** | 1/4 A x Enerji Kapağı gerilimi | <ItemLink id="gregtech:gt.blockmachines:12735" showIcon="left" /> makinesinin Devre Montajcısı modu |
| **Kısıtlamasız** | İpucu "yeterli enerji sağlandığı sürece bu makine her kademeden tarif çalıştırabilir" der | <ItemLink id="gregtech:gt.blockmachines:15517" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:1004" showIcon="left" /> |
