---
item_ids:
  - gregtech:gt.blockmachines:15568
navigation:
  title: Drone Merkezi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15568
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-23
---

# Drone Merkezi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15568"/>
</GameScene>
<Color id="GREEN">Drone Merkezi</Color>, yakındaki makinelerin otomatik bakım onarımları, güç kontrolü ve izlenmesi için IV kademe bir multibloktur. <Color id="RED">Dronlar</Color> bir Giriş Yolu aracılığıyla yerleştirilir ve menzil içinde <Color id="BLUE">Drone Bağlantı Modülü</Color> <ItemImage id="gregtech:gt.blockmachines:9401" /> takılı olan tüm makinelere hizmet verir (bakım kapağının yerini alır). <Color id="GREEN">Merkez</Color> hiç güç tüketmez ve bakım onarımları ücretsizdir, ancak her saniye bir dronun düşüp yok olma ihtimali az da olsa vardır. Toplamda dört dron kademesi vardır ve menzilleri giderek büyür, ömürleri uzar. T4 dron ayrıca boyutlar arası çalışma yeteneğini açar. Ne yazık ki dronlar gerçekten uçmaz veya Drone Merkezinden ayrılmaz.
<br clear="all"/>

> [!NOTE]
> Aşağıdakiler multibloktaki ana değişikliklerdir:
> - Yeni Eşitleme Mantığı: Makine kontrolü artık görüş hattından bağımsız olarak gerçekten çalışıyor
> - Özel Makine Gruplaması: Daha iyi yönetim için makinelerini özel gruplara ayır
> - Geliştirilmiş Anahtar Düğmesi: Anahtar düğmesi artık tüm makineleri gruba göre açıp kapatıyor
> - Boyutlar Arası Bağlantılar: Boyutsal bağlantıları ve sonsuz menzili etkinleştirmek için yeni T4 Dronları kullan
> - Bağlantı Anahtarları: T4 dronlarının diğer oyuncuların sondaj tesislerine bağlanmasını önle!
> - Üretim Kaydedici: Fabrikanın gerçekte ne yaptığını takip et!


## İnşa
<Color id="GREEN">Drone Merkezi</Color> kademeli bileşenlere veya bakım kapağına, enerji kapağına ya da Egzoz Çıkışına sahip değildir. Tek ihtiyacı dronlar için bir Giriş Yoludur. Kenevir betonu her renkte olabilir ve makinenin çalışmasını etkilemez. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan.

<Color id="GREEN">Drone Merkezine</Color> özgü olan <Color id="BLUE">Drone Bağlantı Modülü</Color>, DİĞER makinelerdeki bakım kapağının yerini alarak onları otomatik bakım onarımları, güç kontrolü ve izleme için ağa bağlar. Drone Bağlantı Modülü, bir tane bulana kadar her 10 saniyede bir etkin bir Drone Merkezi arar; bu yüzden gecikme sıçramalarını önlemek için etkin bağlantısı olmayan çok sayıda modül bulundurmamaya çalış. Daha kolay tanımlamak için ana makineyi yeniden adlandırmak üzere Drone Bağlantı Modülüne sağ tıkla. 

### Gerekenler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15568" /> <ItemImage id="gregtech:gt.blockmachines:15568" />
- 61 <ItemLink id="gregtech:gt.blockcasings2:13" /> <ItemImage id="gregtech:gt.blockcasings2:13" />
- 47 <ItemLink id="gregtech:gt.blockframes:305" /> <ItemImage id="gregtech:gt.blockframes:305" />
- 29 <ItemLink id="chisel:hempcrete" /> (her renk) <ItemImage id="chisel:hempcrete" /> 
- 28 <ItemLink id="gregtech:gt.blockframes:32" /> <ItemImage id="gregtech:gt.blockframes:32" />
- 20-26 <ItemLink id="gregtech:gt.blockcasings2" /> <ItemImage id="gregtech:gt.blockcasings2" />
- 1+ Giriş Yolu (herhangi bir çelik makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:70" />

### Duvar Paylaşımı
Makineler aynı <Color id="BLUE">Drone Bağlantı Modülünü</Color> sorunsuzca duvar paylaşabilir; kontrolcüler güç kontrolü ve izleme altında ayrı ayrı görünür. 

## Kullanım
<Color id="RED">Dronlar</Color> yapıdaki bir Giriş Yolundan yerleştirilir. Makine başlatıldığında kontrolcü, menzil içinde <Color id="BLUE">Drone Bağlantı Modülü</Color> takılı tüm makinelere hizmet vermek için mevcut en yüksek kademe dronu tüketir. Etkin dron, her saniye rastgele bir şansa bağlı olarak "düşene" kadar çalışır. Bu olduğunda etkin dron yok edilir ve mevcut bir sonraki en yüksek kademe dron sorumluluğu devralır. Mevcut dronun kademesini kontrolcünün WAILA'sında gör ve gerekirse kontrolcüyü kırarak onu geri al. 

### Dronlar
Dört dron kademesi mevcuttur. Hepsi işlevsel olarak aynıdır, ancak aşağıdaki tabloda görüldüğü gibi daha yüksek kademeler daha geniş menzile ve daha uzun ortalama ömre sahiptir. T3 ve T4 dronlar kırılmaz bile; ancak otomatik bantlı bakım kapağından çok daha sonra açılırlar. Boyutlar arası çalışmayı etkinleştirmek için bağlantı modülü ile <Color id="GREEN">Drone Merkezinin</Color> aynı anahtara sahip olması gerekir. 

| Kademe | Menzil | Düşme Olasılığı | Ortalama Yaşam Ömrü | Boyutlar Arası |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| 1 | 128 | Her saniye 1 / 28.800 | 8 saat | ❌ |
| 2 | 512 | Her saniye 1 / 172.800 | 48 saat | ❌|
| 3 | 4096 | Asla | Sonsuz | ❌|
| 4 | 4096 | Asla | Sonsuz | ✅ |

Menzil, <Color id="RED">Öklid Mesafesi</Color> ile bir <Color id="BLUE">Drone Bağlantı Modülü</Color> ile <Color id="GREEN">Drone Merkezi</Color> kontrolcüsü arasındaki mesafeye göre belirlenir. Koordinatlarından mesafeyi hesaplamak için aşağıdaki denklemi kullan:

<Latex formula="\text{Distance} = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}" />

### Güç Kontrolü
<Color id="BLUE">Drone Bağlantı Modülü</Color> takılı tüm makineler kontrolcünün GUI'sindeki makine listesinde görünür. Makineler yeniden adlandırılabilir, dünyada vurgulanabilir ve uzaktan etkinleştirilip devre dışı bırakılabilir. Kontrolcünün GUI'sinde ayrıca mesafeden bağımsız olarak aynı boyuttaki TÜM makineleri etkinleştirmek/devre dışı bırakmak için düğmeler vardır. Güç kontrolü, elektrik kesintisinden sonra her şeyi yeniden etkinleştirmeye çalışırken veya bir <ItemLink id="gregtech:gt.blockmachines:13106" /> yükseltmeye/taşımaya hazırlanırken son derece kullanışlıdır. 
