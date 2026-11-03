---
navigation:
  parent: /items_blocks_index.md
  title: Yazıcı
  icon: appliedenergistics2:tile.BlockInscriber
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockInscriber
---

# Yazıcı

<ItemImage id="appliedenergistics2:tile.BlockInscriber" scale="4" />

Yazıcı, [presleri](presses.md) kullanarak devre kartlarını ve [işlemcileri](processors.md) basar ve ayrıca birkaç eşyayı Toz haline getirebilir. AE2 Enerjisi (AE) ve Fabric/Forge Enerjisi (E/FE) kabul eder. Yönlü modda, farklı yönlerden yerleştirilen eşyalar farklı yuvalara girer; döndürmek için bir <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> kullan. Ayrıca sonuçları bitişik envanterlere itebilir.

Girdi tamponunun boyutu ayarlanabilir. Tek bir envanterden çok sayıda yazıcıyı beslerken materyallerin daha eşit dağılması için küçük bir tampon kullan.

Dört devre presi [işlemcileri](processors.md) üretir:

<Row>
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:13" scale="4" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:14" scale="4" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:15" scale="4" />
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:19" scale="4" />
</Row>

İsim presi, bir örs gibi eşyaları adlandırabilir; bu, bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:500" /> içindeki şeyleri etiketlemek için kullanışlıdır.

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:21" scale="4" />

## Ayarlar

* Yönlü mod, girdiyi ve çıkarmayı yöne göre yönlendirir. Yönlü olmayan modda dahili bir filtre hedef yuvayı seçer, ancak üst ve alt yuvalardan çıkarma yapılamaz.
* Sonuçlar bitişik envanterlere itilebilir.
* Girdi tamponu manuel besleme için büyük, büyük paralel kurulumlar içinse küçük olabilir.

## Arayüz ve Yönlülük

Yönlü modda, yerleştirme veya çıkarma için kullanılan yön yuvayı seçer.

![Yazıcı arayüzü](../assets/images/inscriber_gui.png) ![Yazıcı yönleri](../assets/images/inscriber_sides.png)

A. **Üst girdi** üst taraftan erişilir (eşyalar yerleştirilebilir ve çıkarılabilir).

B. **Orta girdi** sol, sağ, ön ve arka taraftan erişilir (eşyalar yerleştirilebilir ancak çıkarılamaz).

C. **Alt girdi** alt taraftan erişilir (eşyalar yerleştirilebilir ve çıkarılabilir).

D. **Çıktı** sol, sağ, ön ve arka taraftan çıkarılır (eşyalar çıkarılabilir ancak yerleştirilemez).

## Basit Otomasyon

Yönlülük ve döndürme, yarı otomatik kurulumlara olanak tanır:

<GameScene width="350" height="220" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/inscriber_hopper_automation.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Alternatif olarak, yönlü olmayan modda eşyaları borularla yazıcıya verip dışarı alabilirsin.

## Yükseltmeler

Yazıcı <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> (hızlandırma kartı) destekler.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockInscriber" />

