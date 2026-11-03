---
item_ids:
  - gregtech:gt.blockmachines:31087
navigation:
  title: Buhar Ocağı
  parent: multis.md
  icon: gregtech:gt.blockmachines:31087
categories:
    - New Multiblocks
author: Skorched
date: 2026-05-25
---

# Buhar Ocağı
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" />
</GameScene>
<Color id="GREEN">Buhar Ocağı</Color>, ham maddeleri eritmek, yüksek fırında işlemek ve tütsülemek için Buhar kademesinde bir multibloktur. <Color id="GREEN">Buhar Ocağı</Color>, tek bloklu buhar fırınına göre doğrudan bir yükseltmedir çünkü %125 hızda çalışır, normalde gereken buharın yalnızca %62,5'ini kullanır ve 8 paralel sunar. Makinenin iki kademesi vardır: temel (T1) ve yüksek basınç (T2). Diğer buhar çağı multibloklarında olduğu gibi yüksek basınçlı sürüm iki kat hızlı çalışmak için iki kat buhar tüketir. Ayrıca aralarından seçim yapabileceğin üç mod vardır. Varsayılan <Color id="GREEN">Ergitme</Color> modu herhangi bir tarifi kısıtlama veya ek avantaj olmadan işleyebilir. <Color id="RED">Yüksek Fırınlama</Color> modu makineyi iki kat hız ve buhar kullanımı karşılığında cevherler/metallerle sınırlar. <Color id="BLUE">Tütsüleme</Color> modu makineyi iki kat hız ve buhar kullanımı karşılığında yiyecek eşyalarıyla sınırlar. HV'de <Color id="GREEN">Buhar Ocağı</Color>'nın yerini <ItemLink id="gregtech:gt.blockmachines:1003"/> <ItemImage id="gregtech:gt.blockmachines:1003"/> alır.
<br clear="all"/>

## İnşaat:
Temel ve yüksek basınçlı Buhar Ocağı arasındaki tek yapısal fark kasaların malzemesidir. Buhar yalnızca bir <ItemLink id="gregtech:gt.blockmachines:31040" /> <ItemImage id="gregtech:gt.blockmachines:31040" /> aracılığıyla kabul edilir (girdi kapağı DEĞİL), tıpkı diğer buhar kademesi multibloklar gibi. Buhar giriş ve çıkış yolu bitişik envanterlere otomatik itmez veya onlardan otomatik çekmez, bu yüzden otomasyon için huniler, EnderIO eşya kanalı veya konveyör modülü gerekir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan; tek bir yığında tutulan projektör sayısı makinenin kademesini belirler (1=Temel, 2=Yüksek Basınç).

Levhaların bir <ItemLink id="gregtech:gt.blockmachines:112" /> <ItemImage id="gregtech:gt.blockmachines:112" /> içinde ve çubukların bir eğe ile yapıldığını varsayarsak, temel bir <Color id="GREEN">Buhar Ocağı</Color> (gerekli kapaklarla birlikte) inşa etmek için 395 bronz külçe ve 9 tuğla blok gerekir. Yüksek basınçlı bir <Color id="GREEN">Buhar Ocağı</Color> için 359 çelik külçe, 63 bronz külçe ve 3 tuğla blok gerekir. 
### Gereksinimler:
<Row gap="20" alignItems="center">
<Column gap="8" alignItems="center">
__Temel (T1) Gereksinimleri:__
  - 1 <ItemLink id="gregtech:gt.blockmachines:31087" /><ItemImage id="gregtech:gt.blockmachines:31087" />
  - 2-6 <ItemLink id="gregtech:gt.blockcasings:10" /><ItemImage id="gregtech:gt.blockcasings:10" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:2" /><ItemImage id="gregtech:gt.blockcasings2:2" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:12" /><ItemImage id="gregtech:gt.blockcasings2:12" />
  - 3 <ItemLink id="gregtech:gt.blockcasings3:13" /><ItemImage id="gregtech:gt.blockcasings3:13"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31040"/><ItemImage id="gregtech:gt.blockmachines:31040"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31046" /><ItemImage id="gregtech:gt.blockmachines:31046"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31047" /><ItemImage id="gregtech:gt.blockmachines:31047"/>
</Column>
<Column gap="8" alignItems="center">
__Yüksek Basınç (T2) Gereksinimleri:__
  - 1 <ItemLink id="gregtech:gt.blockmachines:31087" /><ItemImage id="gregtech:gt.blockmachines:31087" />
  - 2-6 <ItemLink id="gregtech:gt.blockcasings2" /><ItemImage id="gregtech:gt.blockcasings2" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:3" /><ItemImage id="gregtech:gt.blockcasings2:3" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:13" /><ItemImage id="gregtech:gt.blockcasings2:13" />
  - 3 <ItemLink id="gregtech:gt.blockcasings3:14" /><ItemImage id="gregtech:gt.blockcasings3:14"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31040"/><ItemImage id="gregtech:gt.blockmachines:31040"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31046" /><ItemImage id="gregtech:gt.blockmachines:31046"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31047" /><ItemImage id="gregtech:gt.blockmachines:31047"/>
</Column>
</Row>

### Duvar Paylaşımı:
<Color id="GREEN">Buhar Ocakları</Color> kasa ve veriyolu/kapak tasarrufu için her bir kenarını duvar paylaşımına açabilir. Bu kesinlikle önerilir çünkü önemli miktarda bronz ve çelik tasarrufu sağlar. Paylaşım, aynı tür kasayı kullanan diğer buhar kademesi multibloklarla da çalışır. 

## Kullanım:
<Color id="GREEN">Buhar Ocağı</Color>, tek bloklu buhar fırınına göre doğrudan bir yükseltmedir çünkü <Color id="GREEN">%125</Color> hızda çalışır, normalde gereken buharın yalnızca <Color id="BLUE">%62,5</Color>'ini kullanır ve <Color id="RED">8</Color> paralel sunar. Yüksek basınca (T2) yükseltmek hem işlem hızını hem de buhar tüketimini ikiye katlar; bu, aşağıdaki tabloda görülebilir. Tek bloklu makinelere göre büyük avantajları sayesinde <Color id="GREEN">Buhar Ocağını</Color> HV'ye kadar kullanmayı bekleyebilirsin.

<Color id="GREEN">Buhar Ocağının</Color> belirli tariflerde uzmanlaşarak makinenin verimini daha da artıran üç özgün modu vardır; bunlar aşağıda listelenmiştir. Bu modların vanilya fırınını, yüksek fırınını ve tütsüleyiciyi taklit ettiğine dikkat et. Modları kontrolcünün GUI'sinden veya kontrolcüye tornavida kullanarak değiştir.

- <Color id="GREEN">Ergitme</Color> - Kısıtlama veya ek avantaj yok. Varsayılan evrensel mod.
- <Color id="RED">Yüksek Fırınlama</Color> - İki kat hız ve buhar tüketimi karşılığında cevherler/metallerle sınırlı.
- <Color id="BLUE">Tütsüleme</Color> - İki kat hız ve buhar tüketimi karşılığında çiğ yiyeceklerle sınırlı.

Aşağıdaki tablolar <Color id="GREEN">Buhar Ocağının</Color> her iki kademesi ve üç farklı mod için buhar tüketimini ve hızı özetler. Referans olarak vanilya fırını saniyede 0,10 eşya eritir, vanilya yüksek fırını/tütsüleyicisi ise saniyede 0,20 eşya işler. 
### __Temel (T1)__
|  | <Color id="GREEN">Ergitme</Color> | <Color id="RED">Yüksek Fırınlama</Color> | <Color id="BLUE">Tütsüleme</Color> |
| --------------- | --------------- | --------------- | --------------- |
| Maks. Buhar | 800 L/s | 1.600 L/s | 1.600 L/s |
| Maks. Hız | 0,78 Eşya/s | 1,54 Eşya/s | 1,54 Eşya/s |

### __Yüksek Basınç (T2)__

|  | <Color id="GREEN">Ergitme</Color> | <Color id="RED">Yüksek Fırınlama</Color> | <Color id="BLUE">Tütsüleme</Color> |
| --------------- | --------------- | --------------- | --------------- |
| Maks. Buhar | 1.600 L/s | 3.200 L/s | 3.200 L/s |
| Maks. Hız | 1,54 Eşya/s | 3,08 Eşya/s | 3,08 Eşya/s |
