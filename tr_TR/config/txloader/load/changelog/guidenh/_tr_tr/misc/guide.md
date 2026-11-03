---
navigation:
  title: GuideNH
  parent: misc.md
  icon: minecraft:book
categories:
    - Miscellaneous Changes
author: Skorched
date: 2026-05-27
---

# GuideNH
GuideNH, 2.9'a eklenen yepyeni bir moddur; daha önce görev kitabında veya viki gibi harici sitelerde gömülü kalan oyun içi bilgilere daha kolay erişim sağlamak için tasarlanmıştır.

> [!IMPORTANT]
> Bu, vikinin __yerine geçmeyi__ amaçlamaz; bunun yerine başlamak için gereken hayati oyun içi bilgileri sağlar

## Kullanım
Fareni sol tarafın üzerine getirdiğinde "Gezinme" çubuğu açılır. Bu çubuk, rehberler tarafından tanımlanan "üst düzey" kategorileri gösterir. Rehberler genellikle ilgili modlara ayrılır (örneğin, AppliedEnergistics2 altında AE2 rehberleri), ancak şu anda okumakta olduğun değişiklik günlüğü gibi bazı istisnalar da vardır!

Buradan bu kategoriler, içlerindeki rehberleri göstermek için genişler. Kategorinin temel bir özeti ve tüm alt sayfalara bağlantılar için kategori dizini sayfasına da tıklayabilirsin

Sayfalar, Gezinme çubuğunun sağ tarafından yer imlerine eklenebilir; ana sayfa (üst çubuktan erişilir) önerilen rehberleri geçmişinle birlikte gösterir!

Arama da yerleşiktir; ihtiyacın olanı dışarıda arama yapmadan bulmanı sağlar.

Rehber yazarları ayrıca sayfa için bir eşya veya bloğu "item_id" olarak ayarlayabilir; böylece envanterde ya da doğrudan NEI içinde "Rehberi açmak için [G] tuşunu basılı tut" seçeneğini kullanabilirsin.

## Özellikler
Özellikler o kadar çok ki hepsini burada düzgünce listelemek mümkün değil; bu yüzden bu modda nelerin işlenebileceğini göstermek için derlenmiş bu yarı rastgele seçkiyi kabul et:

<Color id="GREEN">Bu _gerçekten_ ~~aynı~~ <u>farklı</u> ___biçimlerin___ bir __örneğidir__</Color>

<GameScene width="420" height="280" zoom={3} interactive={true}>
  <ImportStructure src="../assets/reworks/coke_oven.snbt" />
  <ImportPonder src="../assets/reworks/coke_oven.json"/>
</GameScene>

<br clear="all"/>

<Latex tooltip="Look mom! A tooltip!" color="FF55FF" formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: Mevcut <Color id="GREEN">Akış</Color> Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
</Latex>

<br clear="all"/>

<FunctionGraph title="Promotör Oranına Göre Yakıtların Verimi" xRange="0..2" domain="0..2" xLabel="Yanma Promotörünün Yakıta Oranı ($$R$$)" yLabel="Verim (%)"> <Plot expr="1.5*e^((-0.04)/x)*100" color="#ff55ff" label="Gaz/Dizel Yakıtları (C=0.04)"/>
<Plot expr="1.5*e^((-0.005)/x)*100" color="#ffff55" label="Roket Yakıtları (C=0.005)"/>
</FunctionGraph>

<br clear="all"/>

<RecipeFor id="gregtech:gt.blockmachines:15529" input="gregtech:gt.blockmachines:1246"/>

<br clear="all"/>

<GameScene>
  <ImportStructureLib controller="gregtech:gt.blockmachines:9500" />
</GameScene>

## Teknik Ayrıntılar
GuideNH, YAML frontmatter ve MDX tarzı çalışma zamanı etiketleri içeren <Color id="GREEN">Markdown</Color> sayfalarıyla çalışır. Sayfaların hangi dilde olduğu, `_en_us` gibi bir dil klasörü altına konularak belirtilir.

Etiketlerin tam listesi ve gezinme ile diğer ayrıntıların nasıl işlendiği için [Viki'ye](https://github.com/ABKQPO/GuideNH) göz at!