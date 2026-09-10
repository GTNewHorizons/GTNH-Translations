---
navigation:
  parent: /ae2_mechanics_index.md
  title: Байты и типы
  icon: appliedenergistics2:item.ItemExtremeStorageCell.Universe
---

# Байты и типы

<Column>
  <Row>
    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />
  </Row>

  <Row>
    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" />
  </Row>
</Column>

[Ячейки хранения](../items_blocks/storage_cells.md) описываются двумя величинами: *байтами* и *типами*. Байты, как и в
настоящем компьютере, показывают общий объём "всего подряд" в ячейке хранения. Типы показывают, сколько разных,
собственно, *типов* вещей лежит в ячейке. Каждый тип - это уникальный предмет, так что 4 096 булыжника - это 1 тип, а 16 разных
мечей с разными чарами - это 16 типов.

Каждая ячейка хранения вмещает фиксированный объём
данных. Каждый тип сразу забирает некоторое количество байт (зависит от размера
ячейки), а каждый предмет занимает один бит, так что восемь предметов занимают один
байт, а полный стак из 64 - 8 байт, независимо от того, как этот предмет
стакается за пределами МЭ сети. Например, 64 одинаковых седла займут
не больше места, чем 64 камня.

Ещё раз: каждый предмет - это 1 бит, то есть 8 предметов равны 1 байту. Для жидкостных ячеек это 2 048 мБ на байт.

Многие жалуются на ограниченное число типов в ячейке, но это ***необходимое ограничение***.
Ячейки хранят свои данные в NBT-теге на самом предмете, что делает их довольно надёжными. Но из-за этого, если запихать в ячейку
слишком много данных, игроку будет отправлено слишком много данных, и получится эффект вроде "Book Banning" из ванильного Minecraft.
Кроме того, чем больше разных типов в системе, тем выше нагрузка на сортировку и обработку предметов. При этом на практике
ограничение не такое уж жёсткое. Один <ItemLink id="appliedenergistics2:tile.BlockDrive" />, полностью забитый ячейками, даёт 630 типов, а это
довольно много, если не хранить кучу уникальных нестакающихся предметов.

Именно поэтому типы и существуют: чтобы "настойчиво отбить желание" сваливать сотни случайно повреждённых доспехов и инструментов
с фермы мобов прямо в МЭ систему. Каждый кусок брони с уникальной прочностью и чарами приходится хранить отдельной записью,
и система пухнет. Лучше отфильтровать такое ещё на подходе, до того как оно попадёт в систему.

Гнаться сразу за ячейками высшего тира обычно не лучшая идея:
ресурсов уходит больше, а типов больше не становится. Поэтому ячейки всех размеров остаются полезными даже
в позднем этапе игры - у каждой свои плюсы и минусы.

Ниже таблица со сравнением тиров ячеек хранения: сколько они вмещают и
примерно во сколько обходятся.

## Вместимость ячеек хранения против стоимости

| Ячейка | Байты | Типы | Байт на тип |
| --- | ---: | ---: | ---: |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />        |      1,024 | 63 |       8 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />        |      4,096 | 63 |      32 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />       |     16,384 | 63 |     128 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />       |     65,536 | 63 |     512 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />   |    262,144 | 63 |   2,048 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />  |  1,048,576 | 63 |   8,192 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />  |  4,194,304 | 63 |  32,768 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" /> | 16,777,216 | 63 | 131,072 |

<Column>
  <Row>
    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:35" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:37" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:57" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:59" />
  </Row>

  <Row>
    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:35" handlerId="gt.recipe.circuitassembler" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:37" handlerId="gt.recipe.circuitassembler" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:57" handlerId="gt.recipe.circuitassembler" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:59" handlerId="gt.recipe.circuitassembler" />
  </Row>
</Column>

## Вместимость при разном количестве типов

Типы забирают байты вперёд, поэтому ячейка с 1 типом вмещает вдвое больше, чем ячейка, где заняты все 63 типа.

| Ячейка | Общая вместимость при 1 занятом типе | Общая вместимость при 63 занятых типах |
| --- | ---: | ---: |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />            |       8,128 |      4,160 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />            |      32,512 |     16,640 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />           |     130,048 |     66,560 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />           |     520,192 |    266,240 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />       |   2,080,768 |  1,064,960 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />      |   8,323,072 |  4,259,840 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />      |  33,292,288 | 17,039,360 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" />     | 133,169,152 | 68,157,440 |

![Ячейка с 1 типом](../assets/images/1_type_cell.png)

![Ячейка с 63 типами](../assets/images/63_type_cell.png)