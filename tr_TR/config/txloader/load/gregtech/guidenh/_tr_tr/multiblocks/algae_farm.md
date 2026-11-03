---
item_ids:
  - gregtech:gt.blockmachines:15545
quest_ids:
  - Ds_ok-hRS2ODJNs3LUP9kw==
navigation:
  title: Yosun Çiftliği
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15545
  position: -2001
---

# Yosun Çiftliği

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15545" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15545" showIcon="left" />, farklı yosun türlerini yetiştirmek için MV kademesinde bir Multibloktur. Yosun Çiftliği'nin çalışması için güç dışında girdi gerekmez ve kirlilik üretmez. Yosunun tipi ve miktarı enerji kapağının kademesine bağlıdır ve GT++ kompostu sağlanarak bir kademe daha artırılabilir. Yosun, esas olarak [<ItemLink id="gregtech:gt.blockmachines:998" showIcon="left" />](./exxonmobil_chemical_plant.md) için yenilenebilir bir hammadde olarak kullanılır.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | MV |
| Yapı Boyutu (UxGxY) | 10x3x6 |
| Güç | Normal |
| Hız Aşırtmalar | Benzersiz |
| Bakım | Bakım Gerekli |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa

### Üretim

<RecipesFor id="gregtech:gt.blockmachines:15545" handlerId="gt.recipe.assembler" />

<RecipesFor id="gregtech:gt.blockcasings12:15" />

<RecipesFor 
  id="gregtech:gt.blockframes:306" 
  handlerBlacklist="neicustomdiagram.diagramgroup.gregtech.materialtools, neicustomdiagram.diagramgroup.gregtech.materialparts" />

<RecipesFor id="gregtech:gt.blockcasings3:11" />

### Yapı

Yosun Çiftliği'nin kademeli tek bir Bileşeni vardır. Cam, enerji kapağının maksimum kademesini belirler. UMV kademesi cam tüm kısıtlamaları kaldırır. 

Yosun Çiftliği döndürülemez.

Yollar/kapaklar yapı üzerinde herhangi bir yerdeki yosun kasalarının yerine geçebilir. 

Çok amperli ve lazer enerji kapakları desteklenmez ve yalnızca BİR normal enerji kapağı olabilir. 

Su, makineyi beslemek için tek seferlik bir maliyettir ve yapıya rezervuar kapağı ya da girdi kapağı ile konur. 

Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15545" showIcon="left" /> | 1, Ön Orta, 3. Katman |
| <ItemImage id="bartworks:BW_TieredGlass" /><Color id="blue">Kademeli</Color> Cam | 64 |
| <ItemLink id="gregtech:gt.blockcasings12:15" showIcon="left" /> | 20-25 |
| <ItemLink id="gregtech:gt.blockframes:306" showIcon="left" /> | 6 |
| <ItemLink id="gregtech:gt.blockcasings3:11" showIcon="left" /> | 5 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Yalnızca normal Kapak kullanılabilir, kademe camla sınırlıdır</Tooltip> | 1, Herhangi bir kasa |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1, Herhangi bir kasa |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 0+, Herhangi bir kasa |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, Herhangi bir kasa |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1+, Herhangi bir kasa |

### Duvar Paylaşımı

Yosun Çiftlikleri kasa, cam ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımıyla kullanabilir. Hiçbir tarif 1A'dan fazla güç kullanmadığından iki makine arasında tek bir enerji kapağı paylaşmak mümkündür.

## Kullanım

Her döngünün süresi ve üretilen yosunun tipi/miktarı, aşağıdaki tabloda görüldüğü gibi enerji kapağının kademesine bağlıdır. Birçok çıktı garantili değildir, bunun yerine %90 üretilme Şansı vardır. Örneğin, bir HV Yosun Çiftliği her zaman 1 kahverengi yosun üretir ve zamanın %90'ında 4 tane daha üretir; bu da döngü başına toplam 5 ve saniyede ortalama 0.066 yosun demektir.

LuV ve üzerinde iyileştirilmiş ölçeklemeye dikkat et. Tarif süresi her kademede 10 saniye azaltılmak yerine yarıya iner, bu da üretilen ortalama yosunu büyük ölçüde artırır. En son kademe şu anda elde edilemez çünkü UXV'nin üzerinde üretilebilir enerji kapağı yok.

İsteğe bağlı olarak, makinenin kademesini bir artırmak için bir giriş yolu üzerinden GT++ kompostu sağla. Örneğin, bir MV Yosun Çiftliği normalde üretemeyeceği kahverengi yosunu üretebilir ve tarif süresi 80s'den 70s'ye düşerdi. İşlem başına gereken kompost miktarı her kademede iki katına çıkar, en fazla 64'e kadar.

Aşağıdaki tablo, her kademede tarif süresini, artırma için gereken kompostu ve saniyede üretilen ortalama yosunu gösterir.

| Gerilim | Tarif Süresi | Gereken Kompost | <ItemImage id="miscutils:item.BasicAgrichemItem" /> Yosun | <ItemImage id="miscutils:item.BasicAgrichemItem:1" /> Yeşil | <ItemImage id="miscutils:item.BasicAgrichemItem:2" /> Kahverengi | <ItemImage id="miscutils:item.BasicAgrichemItem:3" /> Altın-Kahverengi | <ItemImage id="miscutils:item.BasicAgrichemItem:4" /> Kırmızı |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ULV | 100.0s | 1 | 0.060 /s | 0.018 /s | - | - | - |
| LV | 90.0s | 1 | 0.111 /s | 0.082 /s | - | - | - |
| MV | 80.0s | 2 | 0.125 /s | 0.245 /s | - | - | - |
| HV | 70.0s | 4 | 0.143 /s | 0.337 /s | 0.066 /s | - | - |
| EV | 60.0s | 8 | 0.167 /s | 0.393 /s | 0.160 /s | 0.060 /s | - |
| IV | 50.0s | 16 | 0.200 /s | 0.472 /s | 0.272 /s | 0.112 /s | 0.072 /s |
| LuV | 25.6s | 32 | 0.391 /s | 1.078 /s | 0.648 /s | 0.453 /s | 0.539 /s |
| ZPM | 12.8s | 64 | 0.781 /s | 2.781 /s | 1.766 /s | 1.219 /s | 1.234 /s |
| UV | 6.40s | 64 | 1.563 /s | 7.438 /s | 4.938 /s | 3.375 /s | 2.938 /s |
| UHV | 3.20s | 64 | 3.125 /s | 19.88 /s | 13.63 /s | 9.250 /s | 7.125 /s |
| UEV | 1.60s | 64 | 6.250 /s | 52.25 /s | 36.63 /s | 24.75 /s | 17.38 /s |
| UIV | 0.80s | 64 | 12.50 /s | 134.5 /s | 95.75 /s | 64.50 /s | 42.25 /s |
| UMV | 0.40s | 64 | 25.00 /s | 339.0 /s | 244.0 /s | 164.0 /s | 102.0 /s |
| UXV | 0.20s | 64 | 50.00 /s | 838.0 /s | 608.0 /s | 408.0 /s | 244.0 /s |
| MAX | 0.10s | 64 | 100.0 /s | 2,036 /s | 1,486 /s | 996.0 /s | 578.0 /s |
| MAX+ | 0.05s | 64 | 200.0 /s | 4,872 /s | 3,572 /s | 2,392 /s | 1,356 /s |

Yosun, başlıca metan, sülfürik asit, etilen ve amonyak için yenilenebilir bir alternatif olarak [<ItemLink id="gregtech:gt.blockmachines:998" showIcon="left" />](./exxonmobil_chemical_plant.md) içinde kullanılır. Kahverengi yosun ayrıca MAR-Ce-M200 külçelerini eritmek için lityum klorür yapımında, kırmızı yosun ise prizmarin parçaları yapımında kullanılır.

## Kaynaklar

- [GTNH Wiki: Yosun Çiftliği](https://wiki.gtnewhorizons.com/wiki/Algae_Farm)