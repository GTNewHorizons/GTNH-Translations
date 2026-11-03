---
navigation:
  title: "Kademe Atlama, Hız Aşırtma ve Paraleller"
  icon: OpenComputers:item:27
  parent: /index.md
---

# Kademe Atlama, Hız Aşırtma ve Paraleller


Multiblokların davranışı şu temel kavramlarla belirlenir: **[kademe atlama](tierskipping.md)**, **[hız aşırtma](overclocking.md)**, **[paraleller](parallels.md)** ve bu sayfada anlatılan **anma gücü** ile **gerilim kademesi**.

**[Kademe atlama](tierskipping.md)**, bir multiblokun daha yüksek temel tarif gücüne sahip tarifleri çalıştırmak için daha düşük kademedeki Enerji Kapaklarını kullanabilmesidir; genellikle aynı kademeden iki Enerji Kapağı takılarak yapılır.

**[Hız aşırtma](overclocking.md)**, makinenin bir tarifi daha kısa sürede tamamlayabilmesi için anma gücünün artırılması anlamına gelir. Çoğu durumda bu 4/2 kusurlu hız aşırtma kullanır, ancak bazı makineler 4/4 kusursuz hız aşırtmayı destekler.

**[Paraleller](parallels.md)**, bir multiblok makinenin aynı zaman aralığında aynı tarifin birden fazla kopyasını işleyebilme yeteneğidir.

# Tarifler ve Güç

Her tarifin bir **temel tarif gücü** vardır; bu, NEI'de hız aşırtmadan ve herhangi bir indirim uygulanmadan önce gösterilen güçtür. <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:687" showIcon="left" /> gibi pek çok multiblok, tariflere özel güç indirimleri uygulayabilir. İndirimlerden sonra ama hız aşırtmadan önceki güce **gerçek tarif gücü** denir. İpuçlarında "tarif kademesi" dendiğinde kastedilen temel tarif gücüdür, gerçek tarif gücü değildir.

# Anma Gücü

**Anma gücü**, makinenin çalışırken tüketebileceği maksimum güçtür. **[Hız aşırtma](overclocking.md)** ve **[paraleller](parallels.md)** için birincil girdidir. Hem makinenin bir tarifi çalıştırıp çalıştıramayacağını hem de o tarifi nasıl çalıştıracağını belirler. Anma gücü ve gerilim kademesi makinenin kendi özellikleridir ve yerel güç ağındaki enerji paketi taşıma kurallarından bağımsızdır.

## Bir Tarifi Başlatmak İçin Gereken Koşullar

Makine bir tarifi ancak **anma gücü >= gerçek tarif gücü** ve **gerilim kademesi >= temel tarif gücü** ise başlatabilir.

- Anma gücü çok düşük -> kontrolcü "Tarif daha fazla güç gerektiriyor." der.
- Gerilim kademesi çok düşük -> kontrolcü "Tarifin başlaması için daha yüksek gerilim gerekiyor." der.

## Tek Bloklu Makineler

Tek bloklu makinelerin anma gücü genellikle 1A x standart gerilime eşittir. İstisnalar arasında 2A ile Termal Santrifüj, 3A ile Ark Fırını ve farklı gerilim seviyelerine göre tükettiği akım 8A'den 1A'ya kadar değişen tek bloklu Kütle İmalatçısı bulunur.

## Multiblok Makineler

Multibloklar, tek bir Enerji Kapağı mı yoksa birkaç tane mi kullandıklarına göre anma gücünü farklı hesaplar. Standart bir Enerji Kapağının anma gücü 2A x standart gerilime eşittir. Çok Amperli veya Lazer Kapağın anma gücü, amperajı x standart gerilime eşittir.

- **Yalnızca bir Enerji Kapağı takılı**: çoğu makinede anma gücü = 1A x standart gerilim olur, bu da Enerji Kapağının anma gücünün yarısıdır. Çok Amperli veya Lazer Kapakları doğrudan destekleyen bazı makineler, kapağın tam anma gücünü kullanır.
- **Birden fazla Enerji Kapağı takılı**: anma gücü, tüm Enerji Kapaklarının anma güçlerinin toplamıdır.

Yalnızca bir Enerji Kapağı takılıyken makinenin gerilim kademesi genellikle anma gücünün bir kademe üstündedir; yani 4x bir fark vardır. Bu, makinenin o daha yüksek gerilim kademesindeki tarifleri çalıştırmak için hâlâ yeterli anma gücüne sahip olmadığı anlamına gelir. Bu eksik anma gücünü telafi etmek için aynı kademeden daha fazla Enerji Kapağı takarsın; buna **[kademe atlama](tierskipping.md)** denir. Aynı kademeden iki standart Enerji Kapağı takmak anma gücünü gerilim kademesine eşitler; buna **çift kapaklı kademe atlama** denir.

# Gerilim Kademesi

**Gerilim kademesi**, makinenin çalıştırmasına izin verilen en yüksek temel tarif gücüdür. Anma gücüyle birlikte yalnızca bir tarifin başlatılmasına izin verilip verilmeyeceğini etkiler. Gerilim kademesinin **[hız aşırtma](overclocking.md)** ile hiçbir ilgisi yoktur.

## Tek Bloklu Makineler

Gerilim kademeleri anma güçleriyle aynıdır.

## Multiblok Makineler

Multibloklar için dört farklı gerilim kademesi davranışı vardır:

| Davranış | Açıklama | Tipik Makineler |
|----------|-------------|------------------|
| **Bir kademe artış** | 4A x ortalama Enerji Kapağı gerilimi. Çoğu makine için varsayılan davranıştır. | Elektrikli Yüksek Fırın ve çoğu diğerleri |
| **Artış yok** | 1A x Enerji Kapağı gerilimi | <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:32018" showIcon="left" /> |
| **Bir kademe düşüş** | 1/4 A x Enerji Kapağı gerilimi | <ItemLink id="gregtech:gt.blockmachines:12735" showIcon="left" /> makinesinin Devre Montajcısı modu |
| **Kısıtlamasız** | İpucunda "yeterli enerji sağlandığı sürece bu makine her kademeden tarifi çalıştırabilir" yazar | <ItemLink id="gregtech:gt.blockmachines:12730" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:1004" showIcon="left" /> |
