---
navigation:
  parent: /items_blocks_index.md
  title: Kalıp
  icon: appliedenergistics2:item.ItemMultiMaterial:52
  position: 410
categories:
- tools
item_ids:
- appliedenergistics2:item.ItemMultiMaterial:52
---

# Kalıplar

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:52" scale="4" />

Kalıplar, boş kalıplardan bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:340" /> içinde yapılır. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> ve <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> blokları içine yerleştirilebilirler.

Farklı işleme yöntemleri için birkaç kalıp türü vardır:

*   <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" /> üretim tezgahı tariflerini kodlar. Girdi maddeleri yerleştirildiğinde sonucu üretmesi için doğrudan bir <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> içine konabilirler, ancak asıl kullanımları bir Moleküler Montajcının yanındaki <ItemLink id="appliedenergistics2:tile.BlockInterface" /> içindedir. ME Arayüzleri kalıbı ve girdilerini yanlarındaki montajcılara gönderir; onlar da sonuçlarını otomatik olarak dışarı atar.

*   <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> işleme kalıplarıdır ve en fazla esnekliği sunar. Yalnızca şunu belirtirler: bir ME Arayüzü listelenen girdileri yanındaki envanterlere gönderirse, ME Ağı bir noktada listelenen çıktıları alacaktır. Girdiler ile çıktılar arasındaki makine veya işlem önemli değildir.

Kaynak ayrıca yalnızca tünel kalıbı düzeneklerinde kullanılan bir işleme kalıbı varyantı olan <ItemLink id="appliedenergistics2:item.ItemTunnelPattern" /> öğesini de kaydeder.

Aynı kalıplara sahip birden çok arayüz paralel çalışır. Bir kalıp bütün bir yığını da temsil edebilir; örneğin 1 kırıktaş = 1 taş yerine 8 kırıktaş = 8 taş, böylece arayüz her işlemde sekiz girdi gönderir.

Bu fork ayrıca <ItemLink id="appliedenergistics2:item.ItemMultiPart:473" /> öğesini de ekler. Ayrı ME Ağlarına birbirine bakan bir çift yerleştir, ardından bir tekrarlayıcıya Certus Kuvars İngiliz Anahtarı kullanarak onu **Provider** ve **Accessor** modu arasında geçiş yaptır. Provider, önündeki Ağdaki üretim kalıplarını ve üretilebilir eşyaları yansıtır ve diğer Ağın bunları otomatik üretim için kullanmasını sağlar. Her iki tekrarlayıcı da güç verilmiş ME Ağlarına bağlı olmalıdır.

## Tarifler

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:52" />