---
item_ids:
  - gregtech:gt.blockmachines:15516
navigation:
  title: Mega Damıtma Kulesi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15516
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Mega Damıtma Kulesi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15516"/>
</GameScene>
<Color id="GREEN">Mega Damıtma Kulesi (MDT)</Color>, sıvıları aynı anda TÜM bileşen fraksiyonlarına toplu olarak damıtmak veya tek bir fraksiyonu artırılmış hızda damıtmak için LuV kademe bir multibloktur. Yapı, yanında bir boru bulunan büyük bir merkezi kuleden oluşur ve yapıya "dilimler" ekleyerek yüksekliği artırabilirsin. Damıtma Kulesi modundaysa çıktıların sırası tarifin NEI önizlemesini takip eder ve çıktı sayısı yapının minimum yüksekliğini belirler. <Color id="GREEN">MDT</Color>, Damıtma Kulesi <ItemImage id="gregtech:gt.blockmachines:1126"/> için doğrudan bir yükseltmedir; çünkü Kule modunda 256, damıtıcı modunda 1024 paralele kadar sunar, ciddi overclock için <Color id="GREEN">Çok Amperli ve Lazerli Enerji Kapaklarını</Color> destekler ve sınırsız kademe atlamaya sahiptir. 
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> Hem Damıtıcı hem de Damıtma Kulesi modlarını destekler
> Damıtma Kulesi Modu: Aynı paralel (256), %120 hız, %90 EU kullanımı
> Damıtıcı Modu: $$256 \times (1 + \text{Tower Height} \div 2)$$ paralel, %150 hız, %50 EU kullanımı
> Naquadah işleme ile LuV'a kilitli
> Yapının parçası olarak eklenebilen "dilimler" içerir, yani değişken boyut

## İnşaat
<Color id="GREEN">MDT</Color>'nin kademeli bileşenleri yoktur. Yükseklik, eklenen çıkış dilimi sayısına bağlı olarak 30-54 blok arasında değişir. Yapı doğal olarak 5 bölüme ayrılır ve hepsi zorunludur. Yapının tabanı, kontrolcünün yerleştirildiği ve giriş yolları, bakım kapakları ile enerji kapaklarının yerleştirilmesi gereken yerdir. Yapının sol tarafında küçük bir bronz "çıkış borusu" vardır; girdi kapağı buraya yerleştirilmelidir. Yapının karşı tarafında benzer bir çelik boru bulunur ve çıkış yolu buraya konur. Çelik giriş borusunun üzerinde, çıkış kapakları için yuvaları olan yoğuşturucu kulesi bulunur (eklenen dilimlere bağlı olarak 3-11 arası). Son olarak yapının ana maliyeti, herhangi bir türde kapak veya yol için yeri olmayan kulenin kendisindedir.

## Temel Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15516"/><ItemImage id="gregtech:gt.blockmachines:15516"/>
- 361 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 215 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.2"/>
- 179 <ItemLink id="gregtech:gt.sheetmetal:324"/><ItemImage id="gregtech:gt.sheetmetal:324"/>
- 100-166 <ItemLink id="gregtech:gt.blockcasings14:5"/><ItemImage id="gregtech:gt.blockcasings14:5"/>
- 99 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 80-81 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 43-44 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 41 <ItemLink id="gregtech:gt.blockcasings2"/><ItemImage id="gregtech:gt.blockcasings2"/>
- 1+ Enerji Kapağı (herhangi bir merkezi naquadah kasası) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir merkezi naquadah kasası) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Giriş Yolu (herhangi bir merkezi naquadah kasası) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0-1 Girdi Kapağı (sol taraftaki bronz boru muhafazasının yerini alır) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0-1 Çıkış Yolu (sağ taraftaki çelik boru muhafazasının yerini alır) <ItemImage id="gregtech:gt.blockmachines:80" />
- 3 Çıkış Kapağı (sağ taraftaki bronz boru muhafazalarının yerini alır) <ItemImage id="gregtech:gt.blockmachines:60" />

## Dilim Başına Gereksinimler:
- 57 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.2"/>
- 48 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 32 <ItemLink id="gregtech:gt.sheetmetal:324"/><ItemImage id="gregtech:gt.sheetmetal:324"/>
- 27 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 16 <ItemLink id="gregtech:gt.blockcasings14:5"/><ItemImage id="gregtech:gt.blockcasings14:5"/>
- 16 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 1 Çıkış Kapağı (sağ taraftaki bronz boru muhafazalarının yerini alır) <ItemImage id="gregtech:gt.blockmachines:60" />

## Maksimum Boyut Gereksinimleri:
- 1 <ItemLink id="gregtech:gt.blockmachines:15516"/><ItemImage id="gregtech:gt.blockmachines:15516"/>
- 553 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 443 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.2"/>
- 307 <ItemLink id="gregtech:gt.sheetmetal:324"/><ItemImage id="gregtech:gt.sheetmetal:324"/>
- 164-230 <ItemLink id="gregtech:gt.blockcasings14:5"/><ItemImage id="gregtech:gt.blockcasings14:5"/>
- 207 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 135-136 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 66-67 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 41 <ItemLink id="gregtech:gt.blockcasings2"/><ItemImage id="gregtech:gt.blockcasings2"/>
- 1+ Enerji Kapağı (herhangi bir merkezi naquadah kasası) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir merkezi naquadah kasası) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Giriş Yolu (herhangi bir merkezi naquadah kasası) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0-1 Girdi Kapağı (sol taraftaki bronz boru muhafazasının yerini alır) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0-1 Çıkış Yolu (sağ taraftaki çelik boru muhafazasının yerini alır) <ItemImage id="gregtech:gt.blockmachines:80" />
- 11 Çıkış Kapağı (sağ taraftaki bronz boru muhafazalarının yerini alır) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">MDT'ler</Color> kasa, yol ve kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Ancak yapıyı paylaşmak biraz zahmetlidir ve dikey olarak duvar paylaşılmadıkça tasarruf minimal kalır; bu durumda toplam yapı 105 blok yüksekliğe ulaşır.

## Kullanım
<Color id="GREEN">MDT</Color> artık aşağıda açıklanan iki modla gelir:

### Damıtma Kulesi Modu:
Bu modda <Color id="GREEN">MDT</Color>, normal Damıtma Kulesine benzer şekilde sıvıları aynı anda tüm bileşen fraksiyonlarına damıtır. Her fraksiyon, tarifin NEI önizlemesine göre yapının farklı bir katmanında çıkar. Sıra soldan sağa ve aşağıdan yukarıyadır. Örneğin petrol damıtırken çıktıların sırası sülfürik ağır yakıt, sülfürik hafif yakıt, sülfürik nafta ve sülfürik gazdır. Bu modda makine 256 paralele, normal Damıtma Kulesine kıyasla %120 hıza ve %90 EU kullanımına erişir.

### Damıtıcı Modu:
Bu modda <Color id="GREEN">MDT</Color>, tek girdi ve tek çıktılı normal damıtma tariflerini çalıştırır. Bir girdinin çıktısı, gereken çıktılar için kontrolcüye veya giriş yoluna programlanmış bir devre koyarak belirlenir. Bu modu kullanmak %150 hız ve %50 EU kullanımı sağlar. Yalnızca alt çıkış kapağının kullanıldığını, ancak yapının oluşması için tüm kapakların yerinde olması gerektiğini unutma. Bu makinenin kazandırdığı paralel sayısı şu şekilde verilir
<Latex formula="256 \times \Biggl( 1+\frac{\text{Tower Height}}{2} \Biggr)"/>
burada "Tower Height", yapıdaki dilim sayısıdır (en üst dilim hariç). Bu, yapı yüksekliğine bağlı olarak 512-1024 paralel aralığı verir