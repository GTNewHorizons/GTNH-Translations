---
navigation:
  title: "Kademe Atlama, Hız Aşırtma ve Paraleller"
  icon: OpenComputers:item:27
  parent: /index.md
---

# Kademe Atlama, Hız Aşırtma ve Paraleller


Multiblok makinelerin davranışı şu temel kavramlarla belirlenir: **[kademe atlama](tierskipping.md)**, **[hız aşırtma](overclocking.md)**, **[paraleller](parallels.md)** ve bu sayfada ele alınan **anma gücü** ile **gerilim kademesi**.

**[Kademe atlama](tierskipping.md)**, bir Multiblokun daha yüksek temel tarif gücüne sahip tarifleri çalıştırmak için daha düşük kademeli Enerji Kapakları kullanabilme Yeteneğidir; genellikle aynı kademeden iki Enerji Kapağı takılarak yapılır.

**[Hız aşırtma](overclocking.md)**, Makinenin bir tarifi daha kısa sürede tamamlayabilmesi için anma gücünü artırmak anlamına gelir. Çoğu durumda bu, 4/2 kusurlu hız aşırtma kullanır; ancak bazı makineler 4/4 kusursuz hız aşırtmayı destekler.

**[Paraleller](parallels.md)**, bir Multiblok Makinenin aynı zaman aralığında aynı tarifin birden çok kopyasını işleyebilme Yeteneğidir.

# Tarifler ve Güç

Her tarifin bir **temel tarif gücü** vardır; bu, NEI'de hız aşırtmadan ve herhangi bir indirim uygulanmadan önce gösterilen güçtür. <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:687" showIcon="left" /> gibi birçok Multiblok, tariflere özel güç indirimleri uygulayabilir. İndirimlerden sonra ancak hız aşırtmadan önceki güce **gerçek tarif gücü** denir. İpucu metinleri "tarif kademesi"nden bahsettiğinde, gerçek tarif gücünü değil temel tarif gücünü kasteder.

# Anma Gücü

**Anma gücü**, Makinenin çalışırken tüketebileceği maksimum güçtür. **[Hız aşırtma](overclocking.md)** ve **[paraleller](parallels.md)** için birincil Girdidir. Hem Makinenin bir tarifi çalıştırıp çalıştıramayacağını hem de o tarifi nasıl çalıştıracağını belirler. Anma gücü ve gerilim kademesi Makinenin kendi özellikleridir ve yerel güç ağındaki enerji paketi taşıma kurallarından bağımsızdır.

## Bir Tarifi Başlatmak İçin Gereken Koşullar

Makine bir tarifi yalnızca **anma gücü >= gerçek tarif gücü** ve **gerilim kademesi >= temel tarif gücü** ise başlatabilir.

- Anma gücü çok düşük -> Kontrolcü "Tarif daha fazla güç gerektiriyor." bildirir.
- Gerilim kademesi çok düşük -> Kontrolcü "Tarifin başlaması için daha yüksek gerilim gerekiyor." bildirir.

## Tek Bloklu Makineler

Tek bloklu makineler genellikle 1A x standart gerilime eşit anma gücüne sahiptir. İstisnalar arasında 2A'daki Termal Santrifüj, 3A'daki Ark Fırını ve tükettiği akım farklı gerilim seviyelerine göre 8A'dan 1A'ya kadar değişen tek bloklu Kütle İmalatçısı yer alır.

## Multiblok Makineleri

Multibloklar, bir veya birkaç Enerji Kapağı kullanmalarına göre anma gücünü farklı hesaplar. Standart bir Enerji Kapağı, 2A x standart gerilime eşit anma gücüne sahiptir. Çok Amperli veya Lazer Kapak, amperajı x standart gerilime eşit anma gücüne sahiptir.

- **Yalnızca bir Enerji Kapağı takılı**: çoğu Makine anma gücü = 1A x standart gerilim olur; bu, Enerji Kapağının anma gücünün yarısıdır. Çok Amperli veya Lazer Kapakları doğrudan destekleyen bazı makineler, kapağın tam anma gücünü kullanır.
- **Birden çok Enerji Kapağı takılı**: anma gücü, tüm Enerji Kapaklarının anma gücünün toplamıdır.

Yalnızca bir Enerji Kapağı takılıyken Makinenin gerilim kademesi genellikle anma gücünün bir kademe üstündedir; bu 4x'lik bir farktır. Bu, Makinenin o daha yüksek gerilim kademesindeki tarifleri çalıştırmak için hâlâ yeterli anma gücüne sahip olmadığı anlamına gelir. Bu eksik anma gücünü telafi etmek için aynı kademeden daha fazla Enerji Kapağı yerleştirirsin; buna **[kademe atlama](tierskipping.md)** denir. Aynı kademeden iki standart Enerji Kapağı takmak anma gücünü gerilim kademesine eşitler; buna **çift kapaklı kademe atlama** denir.

# Gerilim Kademesi

**Gerilim kademesi**, Makinenin çalıştırmasına izin verilen en yüksek temel tarif gücüdür. Anma gücüyle birlikte yalnızca bir tarifin başlatılmasına izin verilip verilmediğini etkiler. Gerilim kademesinin **[hız aşırtma](overclocking.md)** ile hiçbir ilgisi yoktur.

## Tek Bloklu Makineler

Gerilim kademeleri anma güçleriyle aynıdır.

## Multiblok Makineleri

Multibloklar için dört farklı gerilim kademesi davranışı vardır:

| Davranış | Açıklama | Tipik Makineler |
|----------|-------------|------------------|
| **Bir kademe artış** | 4A x ortalama Enerji Kapağı gerilimi. Bu, çoğu Makine için varsayılan davranıştır. | Elektrikli Yüksek Fırın ve çoğu diğeri |
| **Artış yapamaz** | 1A x Enerji Kapağı gerilimi | <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:32018" showIcon="left" /> |
| **Bir kademe düşüş** | 1/4 A x Enerji Kapağı gerilimi | <ItemLink id="gregtech:gt.blockmachines:12735" showIcon="left" /> öğesinin Devre Montajcısı modu |
| **Kısıtlamasız** | İpucu metni "yeterli enerji sağlandığı sürece bu Makine her kademeden tarif çalıştırabilir" der | <ItemLink id="gregtech:gt.blockmachines:15517" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:1004" showIcon="left" /> |
