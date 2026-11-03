---
item_ids:
  - gregtech:gt.blockmachines:140
quest_ids:
  - AAAAAAAAAAAAAAAAAAAAQQ==
  - AAAAAAAAAAAAAAAAAAAATA==
  - AAAAAAAAAAAAAAAAAAACuQ==
  - AAAAAAAAAAAAAAAAAAACug==
navigation:
  title: Tuğlalı Yüksek Fırın
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:140
  position: -501
---
# Tuğlalı Yüksek Fırın
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:140" />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:140" showIcon="left">Tuğlalı Yüksek Fırın (BBF)</ItemLink>, demiri çeliğe dönüştürmek için kullanılan Buhar kademeli bir multibloktur. 

Gerekli ateş tuğlalarını üretmek için diğer şeylerin yanı sıra bazaltik mineral kumu damarlarından alçı taşı tozu ve Lapis damarlarından kalsit tozu toplaman gerekir. 

Oyuncular, oyunun başlarında çeliğe olan yüksek talebi karşılamak için genellikle sürekli olarak 4-8 BBF çalıştırır. 

BBF'in yerini [<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" />](./electric_blast_furnace.md) alır, ancak EYF diğer materyalleri eritirken ucuz ve kolay çelik üretimi için birkaç tanesini el altında bulundurmak faydalı olabilir.

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı Kademe | Buhar |
| Yapı Boyutu (GxDxY) | 3x3x4 |
| Güç | Yok |
| Hız Aşırtmalar | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | 200 gibbl/s kirlilik üretir |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:140" />

<Row>
<RecipesFor id="gregtech:gt.blockcasings4:15" handlerId="codechicken.nei.recipe.ShapedRecipeHandler" input="dreamcraft:clayBucketConcrete" />
<RecipesFor id="gregtech:gt.blockcasings4:15" handlerId="gt.recipe.assembler" input="NotEnoughItems:neiFluidDisplay:224" />
</Row>

### Yapı
BBF, bir kontrolcü blok ve içi boş bir merkezin etrafında birkaç katman ateş tuğlasından oluşur. 

Tüm eşyalar kontrolcüden elle yerleştirilip çıkarıldığı için veri yolu/kapak yoktur. 

Diğer multiblokların aksine, yapı kurulmadığında herhangi bir uyarı mesajı veya hata yoktur - BBF'in kurulu olup olmadığını anlamanın tek yolu bir tarif başlatmaktır; kontrolcü yanar ve yapının üstünden duman çıkar. 

BBF döndürülemez - Baca yukarı bakmalıdır.

Yapı gereksinimleri hakkında oyun içinde daha fazla bilgi edinmek için genişletilmiş ipucunu ve NEI yapı önizlemesini, yapıyı dünyada görselleştirmek/inşa etmek için de <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:140" showIcon="left" /> | 1, Ön merkez, 2. katman |
| <ItemLink id="gregtech:gt.blockcasings4:15" showIcon="left" /> | 32, Kontrolcü ve 2.-4. katmanların içi boş merkezi hariç her yer |

### Duvar Paylaşımı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructure src="/assets/structures/bbf_wallshare.snbt" />
</GameScene>

BBF'ler ateş tuğlalarından tasarruf etmek için yanlarını duvar paylaşımıyla birleştirebilir. Bu, ateş tuğlalarının üretimi çok pahalı ve zaman alıcı olduğundan oyunun başlarında son derece değerlidir. 

Bir Kontrolcünün duvar paylaşımına dahil edilemeyeceğini unutma; bu da genellikle BBF duvar paylaşımlarının 2xN sütun biçiminde olmasına yol açar.

BBF duvar paylaşımı örneği için sağdaki sahneye bak.

## Kullanım

BBF'in demiri çeliğe dönüştürmek için birçok farklı tarifi vardır. Aralarındaki tek önemli fark işlem kapasiteleridir. Her çelik külçesini kömür veya odun kömürüyle eritmek 360 sn sürer, kok ile ise yalnızca 240 sn sürer. Sıkıştırılmış yakıtlar, aynı miktarda kaynakla 9 yerine aynı anda 10 külçe işleyebildikleri için biraz daha yüksek yakıt verimliliğine de sahiptir. 

Demiri sıkıştırmak herhangi bir işleme avantajı sağlamaz.

İlgili tariflerin tam özeti aşağıda verilmiştir. Gerekirse demir külçelerinin demir tozuyla değiştirilebileceğini unutma.

<ContentTabs>
  <Tab title="Yakıt Türleri Arasındaki Karşılaştırma">
    | Yakıt Türü | Miktar | İşlem Süresi |
    | --- | --- | --- |
    | <ItemLink id="Railcraft:fuel.coke" showIcon="left" /> | 2 | 240s |
    | <ItemLink id="miscutils:itemCactusCoke" showIcon="left" /> | 8 | 240s |
    | <ItemLink id="miscutils:itemSugarCoke" showIcon="left" /> | 8 | 240s |
    | <ItemLink id="minecraft:coal" showIcon="left" /> | 4 | 360s |
    | <ItemLink id="minecraft:coal:1" showIcon="left" /> | 4 | 360s |
  </Tab>
  <Tab title="Sıkıştırılmış Yakıtla Karşılaştırma">
    | Yakıt Türü | Miktar | İşlenen Demir Külçeleri | İşlem Süresi |
    | --- | --- | --- | --- |
    | <ItemLink id="Railcraft:fuel.coke" showIcon="left" /> | 2 | 1 | 240s |
    | <ItemLink id="Railcraft:cube" showIcon="left" /> | 2(=<ItemImage id="Railcraft:fuel.coke" />18) | 10 | 2400s |
    | <ItemLink id="minecraft:coal:1" showIcon="left" /> | 4 | 1 | 360s |
    | <ItemLink id="gregtech:gt.blockgem3:4" showIcon="left" /> | 4(=<ItemImage id="minecraft:coal:1" />36) | 10 | 3600s |
  </Tab>
</ContentTabs>

BBF ayrıca belirli metal oksit tozlarının (pirit, magnetit, kasiterit vb.) çıktısını artırabilir. Daha spesifik olarak BBF, her 2 toz için 3 külçe verir - bu, vanilya fırınlarına veya [<ItemLink id="gregtech:gt.blockmachines:31087" showIcon="left" />](./steam_hearth.md) kıyasla %50'lik bir artıştır. Sorun, tariflerin kömür veya odun kömürüyle 120 sn, kok ile 80 sn sürmesi ve bunun çelik üretimini geciktirmesidir.

### Kirlilik
BBF aktifken havaya 200 gibbl/s kirlilik salar. Kontrol edilmezse kirlilik oyuncuya ciddi olumsuz etkiler verebilir ve çevredeki chunk'ları yavaşça aşındırır. Tam bir hazmat kıyafeti giyerek olumsuz etkilerden kaçınılabilir, ancak LV'ye kadar dünyadaki etkileri hiçbir şey durduramaz. Buhar çağında kirliliğin etkilerini azaltmak için gerçekten üç seçenek vardır:

- Kirliliği başka bir yerde konsantre etmek için BBF'leri üssünden uzağa yerleştir. Kaynakları taşımaya <ItemLink id="gregtech:gt.blockmachines:2701" showIcon="left" /> yardımcı olabilir.
- Kirliliği tamamen başka bir boyutta konsantre etmek için BBF'leri Nether'a yerleştir. Kirlilik Nether geçidinden geçmez.
- .minecraft\config\GregTech\Pollution.cfg dosyasında kirliliği devre dışı bırak.

Daha sonra kirliliği chunk'lardan gerçekten temizlemek için kirlilik temizleyicileri ve/veya [<ItemImage id="gregtech:gt.blockmachines:12020" />Elektrikli Hava Filtreleri](./electric_air_filter.md) kullan. Daha yüksek kademe zırhlar (ör. Nanosuit) da tam hazmat koruması sağlar. 

## Kaynaklar

- [GTNH Wiki : Tuğlalı Yüksek Fırın](https://wiki.gtnewhorizons.com/wiki/Bricked_Blast_Furnace)