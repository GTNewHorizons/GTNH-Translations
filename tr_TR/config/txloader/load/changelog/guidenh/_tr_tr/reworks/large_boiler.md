---
item_ids:
  - gregtech:gt.blockmachines:15529
  - gregtech:gt.blockmachines:15530
  - gregtech:gt.blockmachines:15531
  - gregtech:gt.blockmachines:15532
navigation:
  title: Büyük Kazan
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15529
categories:
    - Yapı Yenilemeleri
author: Skorched
date: 2026-05-27
---

# Büyük Kazan

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15529"/>
</GameScene>
<Color id="GREEN">Büyük Kazan</Color>, yanıcı yakıtları yakarak suyu buhara veya aşırı ısıtılmış buhara dönüştüren MV kademesinde bir Multibloktur. Daha iyi materyaller açıldıkça verimliliğini ve işlem hacmini daha da artıran dört Büyük Kazan kademesi vardır. Yüksek yoğunluklu yakıtlar yalnızca daha uzun süre yanmakla kalmaz, aynı zamanda toplam yanma süreleriyle orantılı bonus tik alırlar. Kazanlar hem katı hem de sıvı yakıt kabul edebilir, bu da %25 çıktı artışı sağlar. <Color id="GREEN">Büyük Kazan</Color> sonunda Railcraft Kazanının <ItemImage id="Railcraft:machine.beta:5"/> yerini alır, ancak bronz versiyonunun maksimum işlem hacmi biraz daha düşüktür. 

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit)
<br clear="all"/>

> [!NOTE]
> Önceki kazanlara göre değişiklikler şunlardır (yeni yapı dışında):
> - Temel çıktı %20 arttırıldı
> - Dizel yakıtlardaki %25 yanma süresi cezası kaldırıldı
> - %25 artış için aynı anda katı ve sıvı tüketilebilir
> - Kabul edilen yakıtlara yüksek yoğunluklu dizel yakıtlar eklendi
> - Bonus formülü $$\log(\text{Burn Time} \div 16,000) \times 0.025$$ olarak değiştirildi
> - Kazanlar artık kapatıldığında saniyede %0.2 verim kaybediyor

## Yapım
<Color id="GREEN">Büyük Kazan</Color> dört kademede mevcuttur ancak aralarındaki tek yapısal fark kasa tipleri ve kontrolcünün kendisidir. Girdi ve çıkış kapakları yapının herhangi bir yerindeki boru muhafazalarıyla sınırlıyken kalan yollar/kapaklar yapının herhangi bir yerindeki normal kasalarla sınırlıdır. Güç tüketmediği için enerji kapağı yoktur. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

Plakaların bir bükme makinesinde ve çubukların bir eğeyle yapıldığını varsayarsak, bir Büyük Bronz Kazan <ItemImage id="gregtech:gt.blockmachines:15529"/> inşa etmek için 382 bronz külçe ve 33 Tuğla Blokları gerekir, ancak son iki boru muhafazasını ULV girdi kapaklarıyla değiştirmek toplamı 342 bronz külçeye düşürür. Bir Büyük Çelik Kazan <ItemImage id="gregtech:gt.blockmachines:15530"/>, çubuklar bir ekstrüderde yapılırsa ve son iki boru muhafazası ULV girdi kapaklarıyla değiştirilirse, inşa etmek için 362 çelik külçe gerektirir. 

### Gereksinimler:
- 1 Büyük Kazan (Kademeli kontrolcü) <ItemImage id="gregtech:gt.blockmachines:15529"/>
- 24-36 Makine Gövdesi (Kademeli) <ItemImage id="gregtech:gt.blockcasings:10"/>
- 3-11 Külhan Kasası (Kademeli) <ItemImage id="gregtech:gt.blockcasings3:13"/>
- 0-2 Boru Muhafazası (Kademeli) <ItemImage id="gregtech:gt.blockcasings2:12"/>
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Büyük Kazanlar</Color> kasa ve yol/kapak tasarrufu sağlamak için her bir kenarını duvar paylaşımıyla kullanabilir. Buna yakıt ve su için girdi yolu/kapağı ile tüm paylaşılan makinelerin birleşik çıktısını tutacak kadar büyükse buhar için çıkış kapağı da dahildir. 

## Kullanım
<Color id="GREEN">Büyük Kazan</Color>, suyu buhara veya aşırı ısıtılmış (SH) buhara dönüştürmek için yanıcı yakıtları yakar. Yüksek yoğunluklu yakıtlar doğal olarak daha uzun süre yanar ancak toplam yanma süreleriyle orantılı bonus tik de alırlar. Yanma süresi 400'ün altında olan katı yakıtlar Büyük Bronz Kazanda, yanma süresi 1,000'in altında olan katı yakıtlar ise Büyük Çelik Kazanda kabul edilmez. Katı süper yakıt ve büyülü katı süper yakıt, Büyük Titanyum Kazan veya Büyük Tungsten Çeliği Kazanda izin verilen tek yakıtlardır.

<Color id="GREEN">Büyük Kazanlar</Color> çalışmadıkları zaman saniyede %0.2 oranında verim kaybeder, bu yüzden yüksek çalışma süresini hedeflemek idealdir. Uzun yanma süreli yakıtlara aşağıdaki formüle göre bonus verilir:

<Latex formula="\text{Time Bonus} = \log (\text{Burn Time} \div 16,000) \times 0.025"/>

Suyun tüketilme hızı ve buharın üretilme hızı makinenin kademesine göre sabittir. Ancak Büyük Bronz Kazan <ItemImage id="gregtech:gt.blockmachines:15529"/> ve Büyük Çelik Kazan <ItemImage id="gregtech:gt.blockmachines:15530"/> normal buhar üretirken Büyük Titanyum Kazan <ItemImage id="gregtech:gt.blockmachines:15531"/> ve Büyük Tungsten Çeliği Kazan <ItemImage id="gregtech:gt.blockmachines:15532"/> aşırı ısıtılmış (SH) buhar üretir. [Büyük Buhar Türbini](large_steam_turbine.md)<ItemImage id="gregtech:gt.blockmachines:15524"/> çıktısını Büyük Kazana geri döndürüyorsan normal su yerine damıtılmış su kullanılabilir. Bakım sorunlarının her biri üretilen buhar miktarını %10 azaltır.

İsteğe bağlı olarak, toplam buhar çıktısını her değer için 1,000 L/s azaltmak üzere kontrolcünün içine programlanmış bir devre yerleştirilebilir. Örneğin, 3 değerinde bir programlanmış devre buhar çıktısını 3,000 L/s azaltır. Türbinin optimal akış hızının üzerinde olsa bile LST'de daha fazla buhar her zaman daha fazla güç ürettiği için bu nadiren işe yarar. 

| Büyük Kazan | Kademe | Su | Buhar |
| --------------- | --------------- | --------------- | --------------- |
| Bronz | MV | 5.00 L/t | 800 L/t |
| Çelik | HV | 12.50 L/t | 2,000 L/t |
| Titanyum | EV | 16.67 L/t | 2,666 L/t (SH) |
| Tungsten Çeliği | IV | 66.67 L/t | 10,666 L/t (SH) |