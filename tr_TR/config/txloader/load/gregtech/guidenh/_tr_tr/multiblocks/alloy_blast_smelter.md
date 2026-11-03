---
item_ids:
  - gregtech:gt.blockmachines:810
quest_ids:
  - AAAAAAAAAAAAAAAAAAAFiA==
navigation:
  title: Alaşım Yüksek İzabesi
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:810
  position: -5001
---

# Alaşım Yüksek İzabesi

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:810" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" /> (ABS), tozları eriyik alaşımlara eritmek için kullanılan IV kademe bir multibloktur. [<ItemLink id="gregtech:gt.blockmachines:15566" showIcon="left" />](./industrial_mixing_machine.md) ve [<ItemLink id="gregtech:gt.blockmachines:31023" showIcon="left" />](./zyngen.md) ile karşılaştırıldığında, tozları doğrudan eriyik alaşıma işlemek ABS'nin temel alaşım tariflerini daha hızlı ve daha verimli işlemesini sağlar. Ancak o makinelerden farklı olarak ABS kademe atlayamaz; bu da ABS'yi kademe ilerlemesinden çok seri üretime uygun kılar.

ABS, başka hiçbir makinede tarifi olmayan Indalloy 140 gibi daha zorlu alaşımlardan bazılarını eritmek için bile kullanılabilir. 

Kademeli bileşeni ya da herhangi bir bonusu yoktur; birden fazla enerji kapağıyla overclock yapsan bile kademe atlama olmaz. 

Tüm ABS tariflerini işlemek için 12 benzersiz programlanmış devre olduğundan, çok sayıda yol/kapağa izin vermek adına minimum kasa gereksinimi çok düşüktür. ABS'nin yerini UV'de [<ItemLink id="gregtech:gt.blockmachines:31150" showIcon="left" />](./mega_alloy_blast_smelter.md) alır.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | IV |
| Yapı Boyutu (GxUxY) | 3x3x4 |
| Güç | Normal |
| Overclock | Kusurlu |
| Bakım | Bakım Gerekli |
| Kirlilik | 200 gibbl/s kirlilik üretir ve Egzoz Çıkışı gerektirir |

## Üretim ve İnşa

### Üretim

<RecipesFor id="gregtech:gt.blockmachines:810" />

<RecipesFor id="miscutils:miscutils.blockcasings:14" />

<RecipesFor id="miscutils:miscutils.blockcasings:15" />

### Yapı

ABS'de kademeli bileşen yoktur. 

ABS döndürülebilir veya ters çevrilebilir.

Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı bulunabilir. Tek uyarı, kademe atlamanın OLMAMASIDIR (yani 2 IV enerji kapağı ABS'yi LuV geriliminde çalıştırabilir ama LuV tariflerini işleyemez).

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:810" showIcon="left" /> | 1, Ön Alt Merkez |
| <ItemLink id="miscutils:miscutils.blockcasings:14" showIcon="left" /> | 16, 2. ve 3. katman, ortasında boşluk olacak şekilde  |
| <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> | 3-12, 1. ve 4. katmanı doldurur  |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Enerji Kapağı">Yalnızca Normal Kapaklara izin verilir</Tooltip> | 1+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Egzoz Çıkışı | 1+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 0+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Çıkış Kapağı | 1+, herhangi bir <ItemLink id="miscutils:miscutils.blockcasings:15" showIcon="left" /> yerine geçebilir |

Birden fazla <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Egzoz Çıkışı takabilirsin, ancak kirlilik azaltımı takılan tüm susturucuların toplamı değil **ortalamasıdır**. Örneğin <ItemLink id="gregtech:gt.blockmachines:96" /> ve <ItemLink id="gregtech:gt.blockmachines:95" /> kullanmak kirliliği %43'e düşürür; bu da yalnızca bir <ItemLink id="gregtech:gt.blockmachines:96" /> kullanmaktan daha fazla kirlilik oluşturur.

Biraz kasa tasarrufu için birkaç <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu da ekleyebilirsin; yalnızca minimum gereksinimlere dikkat et.

### Duvar Paylaşımı

ABS, kasa, bobin ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Ancak tariflerdeki programlanmış devrelerin çokluğu düşünüldüğünde, benzersiz giriş yolu sayısını azaltmak pek yardımcı olmayabilir.

## Kullanım

Aşağıdaki tablolar 71 tarifin tamamını gerilim kademesine ve programlanmış devreye (PC) göre listeler. Toplamda, son birkaçı birleştirilirse 8 giriş yoluna dağıtılacak 12 benzersiz programlanmış devre var. Bazıları, [<ItemLink id="gregtech:gt.blockmachines:31150" showIcon="left" />](./mega_alloy_blast_smelter.md) açılmadan önce pek de kullanışlı değildir.

Farklı giriş yollarındaki KATI bileşenlerin, programlanmış devreler dahil, aynı tarifte kullanılmasını önlemek için ABS'de giriş ayrıştırması<FloatingImage src="gregtech:textures/gui/overlay_button/input_separation_on.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> etkinleştirilmelidir. Bu, çok sayıda giriş yoluna sahip tek bir ABS'nin aynı anda birçok farklı programlanmış devreyi destekleyebileceği anlamına gelir. Minimum kasa bloğu sayısının üzerinde kalmayı da unutma. 
SIVI bileşenler, girdi kapağı renklendirilmediği sürece **giriş ayrıştırmasından bağımsız olarak her zaman paylaşılır**.

<ContentTabs
  title="Düzenlenmiş ABS Tarifleri"
>

<Tab title="Gerilim Kademesine Göre Düzenlenmiş Tarifler">

| Kademe | PC | Eriyik Alaşım | Yalnızca ABS |
| ---- | -- | ------------ | -------- |
| LV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1054" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1033" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1056" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1034" /> | <Color id="red">✗</Color> |
| ^^ | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1079" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(Temelden) | <Color id="red">✗</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1096" /> | <Color id="red">✗</Color> |
| MV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1057" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:346" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1341" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1095" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1035" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1040" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1041" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1042" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(Doğrudan) | <Color id="red">✗</Color> |
| ^^ | 7 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1043" /> | <Color id="green">✓</Color> |
| ^^ | 11 | <ItemLink id="NotEnoughItems:neiFluidDisplay:620" /> | <Color id="red">✗</Color> |
| HV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:624" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1030" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1031" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1055" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1032" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1050" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1051" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1036" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1037" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1045" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1046" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1047" /> | <Color id="green">✓</Color> |
| EV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1065" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1064" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1053" /> | <Color id="red">✗</Color> |
| ^^ | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1028" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1052" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1044" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:701" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1048" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1059" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1049" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1358" /> | <Color id="red">✗</Color> |
| ^^ | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:351" /> | <Color id="red">✗</Color> |
| IV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1038" /> | <Color id="red">✗</Color> |
| ^^ | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1058" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1080" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1063" /> | <Color id="green">✓</Color> |
| ^^ | 14 | <ItemLink id="NotEnoughItems:neiFluidDisplay:981" /> | <Color id="red">✗</Color> |
| ^^ | 15 | <ItemLink id="NotEnoughItems:neiFluidDisplay:979" /> | <Color id="red">✗</Color> |
| ^^ | 20 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1003" /> | <Color id="red">✗</Color> |
| ^^ | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1005" /> | <Color id="red">✗</Color> |
| LuV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:748" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1066" /> | <Color id="red">✗</Color> |
| ^^ | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1372" /> | <Color id="red">✗</Color> |
| ^^ | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1062" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1069" /> | <Color id="green">✓</Color> |
| ^^ | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1373" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1039" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1070" /> | <Color id="green">✓</Color> |
| ZPM | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1067" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1074" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1071" /> | <Color id="green">✓</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1072" /> | <Color id="green">✓</Color> |
| UV | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1075" /> | <Color id="red">✗</Color> |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1076" /> | <Color id="red">✗</Color> |
| ^^ | -- | <ItemLink id="NotEnoughItems:neiFluidDisplay:1078" /> | <Color id="green">✓</Color> |
| UHV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1077" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1073" /> | <Color id="green">✓</Color> |
| UEV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:826" /> | <Color id="green">✓</Color> |
| ^^ | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1081" /> | <Color id="green">✓</Color> |
| UIV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:172" /> | <Color id="green">✓</Color> |
| UXV | -- | <ItemLink id="NotEnoughItems:neiFluidDisplay:184" /> | <Color id="green">✓</Color> |
{: widths="60, 60, 400, 80"}

</Tab>

<Tab title="Programlanmış Devreye Göre Düzenlenmiş Tarifler">

| Kademe | PC | Eriyik Alaşım | Yalnızca ABS |
| ---- | -- | ------------ | -------- |
| LV | 2 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1054" /> | <Color id="red">✗</Color>  |
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1033" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1056" /> | <Color id="red">✗</Color> | 
| MV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1057" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:346" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1341" /> | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:624" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1030" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1031" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1055" /> | <Color id="red">✗</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1065" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1064" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1053" /> | <Color id="red">✗</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1038" /> | <Color id="red">✗</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:748" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1066" /> | <Color id="red">✗</Color> | 
| LV | 3 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1034" /> | <Color id="red">✗</Color> | 
| MV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1095" /> | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1032" /> | <Color id="red">✗</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1372" /> | <Color id="red">✗</Color> | 
| LV | 4 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1079" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(Temelden) | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1050" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1051" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1036" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1037" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1045" /> | <Color id="red">✗</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1028" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1052" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1044" /> | <Color id="red">✗</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1058" /> | <Color id="red">✗</Color> | 
| UV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1075" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1076" /> | <Color id="red">✗</Color> | 
| MV | 5 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1035" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1040" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1041" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1042" /> | <Color id="green">✓</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1046" /> | <Color id="green">✓</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:701" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1048" /> | <Color id="green">✓</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1080" /> | <Color id="green">✓</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1062" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1069" /> | <Color id="green">✓</Color> | 
| ZPM | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1067" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1074" /> | <Color id="green">✓</Color> | 
| UHV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1077" /> | <Color id="green">✓</Color> | 
| UEV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:826" /> | <Color id="green">✓</Color> | 
| UIV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:172" /> | <Color id="green">✓</Color> | 
| MV | 6 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1061" />(Doğrudan) | <Color id="red">✗</Color> | 
| HV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1047" /> | <Color id="green">✓</Color> | 
| EV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1059" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1049" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1358" /> | <Color id="red">✗</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1373" /> | <Color id="red">✗</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1039" /> | <Color id="green">✓</Color> | 
| MV | 7 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1043" /> | <Color id="green">✓</Color> | 
| LV | 8 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1096" /> | <Color id="red">✗</Color> | 
| IV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1063" /> | <Color id="green">✓</Color> | 
| LuV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1070" /> | <Color id="green">✓</Color> | 
| ZPM | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1071" /> | <Color id="green">✓</Color> | 
| ^^ | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1072" /> | <Color id="green">✓</Color> | 
| UHV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1073" /> | <Color id="green">✓</Color> | 
| UEV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:1081" /> | <Color id="green">✓</Color> | 
| MV | 11 | <ItemLink id="NotEnoughItems:neiFluidDisplay:620" /> | <Color id="red">✗</Color> | 
| IV | 14 | <ItemLink id="NotEnoughItems:neiFluidDisplay:981" /> | <Color id="red">✗</Color> | 
| IV | 15 | <ItemLink id="NotEnoughItems:neiFluidDisplay:979" /> | <Color id="red">✗</Color> | 
| IV | 20 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1003" /> | <Color id="red">✗</Color> | 
| EV | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:351" /> | <Color id="red">✗</Color> | 
| IV | 21 | <ItemLink id="NotEnoughItems:neiFluidDisplay:1005" /> | <Color id="red">✗</Color> | 
| UV | -- | <ItemLink id="NotEnoughItems:neiFluidDisplay:1078" /> | <Color id="green">✓</Color> | 
| UXV | ^^ | <ItemLink id="NotEnoughItems:neiFluidDisplay:184" /> | <Color id="green">✓</Color> | 
{: widths="60, 60, 400, 80"}

</Tab>

</ContentTabs>

## Kaynaklar

- [GTNH Wiki: Alaşım Yüksek İzabesi](https://wiki.gtnewhorizons.com/wiki/Alloy_Blast_Smelter)