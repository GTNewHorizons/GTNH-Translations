---
navigation:
  parent: /items_blocks_index.md
  title: Yükseltme Kartları
  icon: appliedenergistics2:item.ItemMultiMaterial:25
  position: 410
categories:
- tools
item_ids:
- appliedenergistics2:item.ItemMultiMaterial:25
- appliedenergistics2:item.ItemMultiMaterial:28
- appliedenergistics2:item.ItemMultiMaterial:26
- appliedenergistics2:item.ItemMultiMaterial:27
- appliedenergistics2:item.ItemMultiMaterial:68
- appliedenergistics2:item.ItemMultiMaterial:29
- appliedenergistics2:item.ItemMultiMaterial:30
- appliedenergistics2:item.ItemMultiMaterial:31
- appliedenergistics2:item.ItemMultiMaterial:53
- appliedenergistics2:item.ItemMultiMaterial:69
- appliedenergistics2:item.ItemMultiMaterial:64
- appliedenergistics2:item.ItemMultiMaterial:54
- appliedenergistics2:item.ItemMultiMaterial:55
- appliedenergistics2:item.ItemMultiMaterial:56
- appliedenergistics2:item.ItemMultiMaterial:63
- appliedenergistics2:item.ItemMultiMaterial:65
- appliedenergistics2:item.ItemMultiMaterial:66
- appliedenergistics2:item.ItemMultiMaterial:67
---

# Yükseltme Kartları
<Column>
  <Row>
    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:27" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:68" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:29" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:56" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:67" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" />
  </Row>

  <Row>
    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />   
   
    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:69" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:54" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:55" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:64" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:63" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:65" scale="2" />

    <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:66" scale="2" />
  </Row>
</Column>
Yükseltme kartları, AE2 cihazlarının ve makinelerinin davranışını değiştirir; hızlarını artırır, filtre kapasitelerini iyileştirir, Kızıltaş kontrolünü etkinleştirir vb.

## Kart Bileşenleri

<Row>
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:25" scale="2" />

  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:28" scale="2" />
</Row>

Yükseltme kartları, temel olarak bir Temel Kart veya Gelişmiş Kart kullanılarak üretilir.

<Row>
  <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:25" />

  <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:28" />
</Row>

## Kızıltaş Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" />

Kızıltaş Kartları bir cihaza Kızıltaş kontrolü ekler; GUI'sinde Kızıltaş modları arasında geçiş yapmak için bir düğme bulunur.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:26" />

## Kapasite Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:27" scale="2" />

Kapasite Kartları; İçe Aktarma Veriyolları, Dışa Aktarma Veriyolları, Depolama Veriyolları ve Oluşum Düzlemlerindeki filtre yuvası sayısını artırır.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:27" />

## Hiçlik Taşma Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:68" scale="2" />

Hiçlik Taşma Kartları, bir <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" /> içindeki [Depolama Hücrelerine](storage_cells.md) uygulanabilir.
Hücre dolduğunda gelen eşyaları yok ederler. Önce hücrelerini [bölümlediğinden](cell_workbench.md) emin ol.
Eşit Dağıtım Kartı ile birleştirildiğinde, diğer bölümlerde hâlâ yer olsa bile bir eşya kendi bölümü dolduğu anda yok edilir.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:68" />

## Bulanık Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:29" scale="2" />

Bulanık Kartlar, filtrelenen cihazların ve araçların dayanıklılığa göre eşleşmesini ve/veya eşya NBT'sini yok saymasını sağlar. Bu sayede dayanıklılık veya büyüler ne olursa olsun tüm demir baltaları dışa aktarabilir ya da tamamen tamir edilmiş elmas kılıçlar yerine yalnızca hasarlı olanları dışa aktarabilirsin.

Aşağıda bulanık dayanıklılık karşılaştırma modlarının nasıl çalıştığına dair bir örnek var. Sol taraf veriyolu yapılandırmasını, üst satır ise karşılaştırılan eşyayı gösterir.

| %25                    | %10 Hasarlı Kazma | %30 Hasarlı Kazma | %80 Hasarlı Kazma | Tam Onarımlı Kazma |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Neredeyse Kırık Kazma  | ✔                   | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            |
| Tamamen Onarılmış Kazma | \*\*\*\*            | ✔                   | ✔                   | ✔                   |

---

| %50                    | %10 Hasarlı Kazma | %30 Hasarlı Kazma | %80 Hasarlı Kazma | Tam Onarımlı Kazma |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Neredeyse Kırık Kazma  | ✔                   | ✔                   | \*\*\*\*            | \*\*\*\*            |
| Tamamen Onarılmış Kazma | \*\*\*\*            | \*\*\*\*            | ✔                   | ✔                   |

---

| %75                    | %10 Hasarlı Kazma | %30 Hasarlı Kazma | %80 Hasarlı Kazma | Tam Onarımlı Kazma |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Neredeyse Kırık Kazma  | ✔                   | ✔                   | \*\*\*\*            | \*\*\*\*            |
| Tamamen Onarılmış Kazma | \*\*\*\*            |                     | ✔                   | ✔                   |

---

| %99                    | %10 Hasarlı Kazma | %30 Hasarlı Kazma | %80 Hasarlı Kazma | Tam Onarımlı Kazma |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Neredeyse Kırık Kazma  | ✔                   | ✔                   | ✔                   | \*\*\*\*            |
| Tamamen Onarılmış Kazma | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            | ✔                   |

---

| Yok Say                | %10 Hasarlı Kazma | %30 Hasarlı Kazma | %80 Hasarlı Kazma | Tam Onarımlı Kazma |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Neredeyse Kırık Kazma  | ✔                   | ✔                   | ✔                   | **✔**               |
| Tamamen Onarılmış Kazma | **✔**               | **✔**               | **✔**               | ✔                   |

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:29" />

## Hızlandırma Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />

Hızlandırma Kartları işleri hızlandırır. İçe ve Dışa Aktarma Veriyollarının işlem başına daha fazla eşya taşımasını, Yontucuların ve Moleküler Birleştiricilerin daha hızlı çalışmasını sağlar.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:30" />

## Hiper Hızlandırma Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:56" scale="2" />

Hiper Hızlandırma Kartları, normal Hızlandırma Kartlarının daha hızlı sürümüdür ancak yalnızca ME G/Ç Bağlantı Noktasında, ME İçe/Dışa Aktarma Veriyollarında ve ME Sıvı İçe/Dışa Aktarma Veriyollarında kullanılabilir.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:56" />

## Işıktan Hızlı Hızlandırma Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:67" scale="2" />

Işıktan Hızlı Hızlandırma Kartı, eşya veya sıvı taşımak için en hızlı AE kartıdır ancak yalnızca ME G/Ç Bağlantı Noktasında ve ME İçe/Dışa Aktarma Veriyollarında kullanılabilir.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:67" />

## Evirici Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" />

Evirici Kartlar, bir cihazın veya aracın filtresini beyaz liste modundan kara liste moduna geçirir.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:31" />

## Üretim Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />

Üretim Kartları, cihazın ihtiyaç duyduğu eşyalar için [otomatik üretim](../ae2_mechanics/autocrafting.md) sistemine istek göndermesini sağlar.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:53" />

## Eşit Dağıtım Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:69" scale="2" />

Eşit Dağıtım Kartları, bir <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" /> içindeki [Depolama Hücrelerine](storage_cells.md) uygulanabilir. Hücreyi, kartın [bölümlenme](cell_workbench.md) biçimine göre eşit bölümlere ayırır; bu da tek bir eşya türünün hücrenin tamamını doldurmasını önler.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:69" />

## Kalıp Kapasite Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:54" scale="2" />

Her Kalıp Kapasite Kartı arayüze 9 ek kalıp yuvası sağlar; arayüz başına en fazla 3 kart kullanılabilir.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:54" />

## Cevher Sözlüğü Filtre Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:55" scale="2" />

Cevher Sözlüğü girdisine göre filtreleme yapmayı sağlar ve düzenli ifade eşleştirmesini destekler.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:55" />

## Yapışkan Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:64" scale="2" />

Bu hücreye bölümlenen eşyalar, sıvılar veya esanslar yalnızca Yapışkan Kartı olan hücrelerde veya Depolama Veriyollarında depolanabilir; ağın başka hiçbir yerinde depolanamaz.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:64" />

## Gelişmiş Engelleme Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:63" scale="2" />

Gelişmiş Engelleme Kartları, engellemeyi yalnızca bitişik envanterlerle sınırlamak yerine bağlı ME ağının tamamına uygular. Etkinleştirildiğinde arayüz, hedef ağda ilgili eşyalar veya sıvılar zaten varsa tarif bileşenlerinin eklenmesini engeller.

Varsayılan modda engelleme yalnızca ağda tarifle ilgili eşyalar veya sıvılar varsa tetiklenir (mercek, devre veya kalıp gibi katalizörler hariç).

Gevşek modda ağda herhangi bir eşya veya sıvının bulunması engellemeyi tetikler.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:63" />

## Kilitleme Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:65" scale="2" />

Bu kartın 4 modu vardır:

*   Mod 1: Üretimi asla kilitlemez
*   Mod 2: Bir Kızıltaş darbesi alınana kadar üretimi kilitler
*   Mod 3: Kızıltaş sinyali varken üretimi kilitler
*   Mod 4: Kızıltaş sinyali yokken üretimi kilitler

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:65" />

## Sahte Üretim Kartı

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:66" scale="2" />

Bir Arayüz bu kartla donatılırsa, **üretim işini** gönderdikten hemen sonra sonucun dönmesini beklemeden tamamlar. Bu yalnızca gönderilen işin nihai çıktısı amaçlanan ürünse çalışır.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:66" />