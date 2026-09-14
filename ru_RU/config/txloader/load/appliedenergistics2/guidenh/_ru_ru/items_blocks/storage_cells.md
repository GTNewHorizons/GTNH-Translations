---
navigation:
  parent: /items_blocks_index.md
  title: Ячейки хранения
  icon: appliedenergistics2:item.ItemBasicStorageCell.1k
categories:
- tools
item_ids:
- appliedenergistics2:item.ItemMultiMaterial:39
- appliedenergistics2:item.ItemMultiMaterial:61
- ae2fc:fluid_storage_housing
- ae2fc:fluid_storage_housing:2
- ae2fc:fluid_storage_housing:1
- ae2fc:fluid_storage_housing:3
- thaumicenergistics:storage.casing
- appliedenergistics2:item.ItemMultiMaterial:39
- ae2fc:fluid_storage_housing
- appliedenergistics2:item.ItemMultiMaterial:61
- ae2fc:fluid_storage_housing:1
- appliedenergistics2:item.ItemBasicStorageCell.1k
- appliedenergistics2:item.ItemBasicStorageCell.4k
- appliedenergistics2:item.ItemBasicStorageCell.16k
- appliedenergistics2:item.ItemBasicStorageCell.64k
- appliedenergistics2:item.ItemAdvancedStorageCell.256k
- appliedenergistics2:item.ItemAdvancedStorageCell.1024k
- appliedenergistics2:item.ItemAdvancedStorageCell.4096k
- appliedenergistics2:item.ItemAdvancedStorageCell.16384k
- appliedenergistics2:item.ItemExtremeStorageCell.Quantum
- appliedenergistics2:item.ItemExtremeStorageCell.Singularity
- appliedenergistics2:item.ItemExtremeStorageCell.Universe
- appliedenergistics2:item.ItemExtremeStorageCell.Container
- appliedenergistics2:item.ToolPortableCell
- appliedenergistics2:item.ItemVoidStorageCell
- appliedenergistics2:item.ItemMultiMaterial:35
- appliedenergistics2:item.ItemMultiMaterial:36
- appliedenergistics2:item.ItemMultiMaterial:37
- appliedenergistics2:item.ItemMultiMaterial:38
- appliedenergistics2:item.ItemMultiMaterial:57
- appliedenergistics2:item.ItemMultiMaterial:58
- appliedenergistics2:item.ItemMultiMaterial:59
- appliedenergistics2:item.ItemMultiMaterial:60
- ae2fc:fluid_storage1
- ae2fc:fluid_storage4
- ae2fc:fluid_storage16
- ae2fc:fluid_storage64
- ae2fc:fluid_storage256
- ae2fc:fluid_storage1024
- ae2fc:fluid_storage4096
- ae2fc:fluid_storage16384
- ae2fc:fluid_storage.quantum
- ae2fc:fluid_storage.singularity
- ae2fc:fluid_storage.Universe
- ae2fc:multi_fluid_storage1
- ae2fc:multi_fluid_storage4
- ae2fc:multi_fluid_storage16
- ae2fc:multi_fluid_storage64
- ae2fc:multi_fluid_storage256
- ae2fc:multi_fluid_storage1024
- ae2fc:multi_fluid_storage4096
- ae2fc:multi_fluid_storage16384
- ae2fc:portable_fluid_cell
- ae2fc:fluid_storage.void
- ae2fc:fluid_storage.infinity.water
- ae2fc:fluid_part
- ae2fc:fluid_part:1
- ae2fc:fluid_part:2
- ae2fc:fluid_part:3
- ae2fc:fluid_part:4
- ae2fc:fluid_part:5
- ae2fc:fluid_part:6
- ae2fc:fluid_part:7
- thaumicenergistics:storage.essentia
- thaumicenergistics:storage.essentia:1
- thaumicenergistics:storage.essentia:2
- thaumicenergistics:storage.essentia:3
- thaumicenergistics:storage.essentia:4
- thaumicenergistics:storage.essentia:5
- thaumicenergistics:storage.essentia:6
- thaumicenergistics:storage.essentia:7
- thaumicenergistics:storage.essentia:8
- thaumicenergistics:storage.essentia:9
- thaumicenergistics:storage.essentia:10
- thaumicenergistics:storage.component
- thaumicenergistics:storage.component:1
- thaumicenergistics:storage.component:2
- thaumicenergistics:storage.component:3
- thaumicenergistics:storage.component:5
- thaumicenergistics:storage.component:6
- thaumicenergistics:storage.component:7
- thaumicenergistics:storage.component:8
- appliedenergistics2:item.ItemCreativeStorageCell
- ae2fc:creative_fluid_storage
---

# Ячейки хранения

<Column>
  <Row>
    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemExtremeStorageCell.Quantum" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemExtremeStorageCell.Singularity" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemExtremeStorageCell.Universe" scale="4" />
  </Row>

  <Row>
    <ItemImage id="ae2fc:fluid_storage1" scale="4" />

    <ItemImage id="ae2fc:fluid_storage16384" scale="4" />

    <ItemImage id="ae2fc:fluid_storage.quantum" scale="4" />

    <ItemImage id="ae2fc:fluid_storage.singularity" scale="4" />

    <ItemImage id="ae2fc:fluid_storage.Universe" scale="4" />
  </Row>
  
  <Row>
    <ItemImage id="thaumicenergistics:storage.essentia" scale="4" />

    <ItemImage id="thaumicenergistics:storage.essentia:8" scale="4" />

    <ItemImage id="thaumicenergistics:storage.essentia:9" scale="4" />

    <ItemImage id="thaumicenergistics:storage.essentia:10" scale="4" />

    <ItemImage id="thaumicenergistics:storage.essentia:4" scale="4" />
  </Row>
</Column>

Ячейки хранения - один из основных способов хранения в Applied Energistics 2. Их можно установить в <ItemLink id="appliedenergistics2:tile.BlockDrive" /> или <ItemLink id="appliedenergistics2:tile.BlockChest" />.

Объяснение того, как считается их вместимость в байтах и типах, смотри в разделе [Байты и типы](../ae2_mechanics/bytes_and_types.md).

Если ячейка хранения пуста, возьми её в руку и нажми Shift+ПКМ, чтобы извлечь компонент хранения из корпуса.

## Вместимость при разном количестве типов

[Типы забирают байты вперёд](../ae2_mechanics/bytes_and_types.md), поэтому ячейка с 1 типом вмещает вдвое больше, чем ячейка, где заняты все 63 типа.

| Ячейка хранения | Общая вместимость при 1 занятом типе | Общая вместимость при максимуме занятых типов |
| --- | ---: | ---: |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />            |       8 128 |      4 160 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />            |      32 512 |     16 640 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />           |     130 048 |     66 560 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />           |     520 192 |    266 240 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />       |   2 080 768 |  1 064 960 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />      |   8 323 072 |  4 259 840 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />      |  33 292 288 | 17 039 360 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" />     | 133 169 152 | 68 157 440 |
| <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Container" scale="4" />   |     524 224 |          - |
| <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Quantum" scale="4" />     |       1,07G |          - |
| <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Singularity" scale="4" /> |       4,61E |          - |
| <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Universe" scale="4" />    |       4,61E |      4,61E |

---

| Жидкостная ячейка хранения | Общая вместимость (мБ) при 1 занятом типе | Общая вместимость (мБ) при максимуме занятых типов |
| --- | ---: | ---: |
| <ItemLink id="ae2fc:fluid_storage1" scale="4" />            |      2 080 768 |      2 015 232 |
| <ItemLink id="ae2fc:fluid_storage4" scale="4" />            |      8 372 224 |      8 060 928 |
| <ItemLink id="ae2fc:fluid_storage16" scale="4" />           |     33 538 048 |     32 243 712 |
| <ItemLink id="ae2fc:fluid_storage64" scale="4" />           |    134 201 344 |    128 974 848 |
| <ItemLink id="ae2fc:fluid_storage256" scale="4" />          |    536 854 528 |    515 899 392 |
| <ItemLink id="ae2fc:fluid_storage1024" scale="4" />         |  2 147 467 264 |  2 063 597 568 |
| <ItemLink id="ae2fc:fluid_storage4096" scale="4" />         |  8 589 918 208 |  8 254 390 272 |
| <ItemLink id="ae2fc:fluid_storage16384" scale="4" />        | 34 359 721 984 | 33 017 561 088 |
| <ItemLink id="ae2fc:fluid_storage.quantum" scale="4" />     |           275G |              - |
| <ItemLink id="ae2fc:fluid_storage.singularity" scale="4" /> |          4,61E |              - |
| <ItemLink id="ae2fc:fluid_storage.Universe" scale="4" />    |          9,22E |          9,22E |

---

| Ячейка хранения эссенции | Типы | Общая вместимость эссенции (без затрат на типы) |
| --- | ---: | ---: |
| <ItemLink id="thaumicenergistics:storage.essentia" scale="4" />   | 12 |      2 048 |
| <ItemLink id="thaumicenergistics:storage.essentia:1" scale="4" /> | 12 |      8 192 |
| <ItemLink id="thaumicenergistics:storage.essentia:2" scale="4" /> | 12 |     32 768 |
| <ItemLink id="thaumicenergistics:storage.essentia:3" scale="4" /> | 12 |    131 072 |
| <ItemLink id="thaumicenergistics:storage.essentia:5" scale="4" /> | 24 |    524 288 |
| <ItemLink id="thaumicenergistics:storage.essentia:6" scale="4" /> | 36 |  2 097 152 |
| <ItemLink id="thaumicenergistics:storage.essentia:7" scale="4" /> | 48 |  8 388 608 |
| <ItemLink id="thaumicenergistics:storage.essentia:8" scale="4" /> | 60 | 33 554 432 |
| <ItemLink id="thaumicenergistics:storage.essentia:9" scale="4" /> |  1 |       268M |

## Разметка

Ячейкам можно задать фильтр, чтобы они принимали только определённые предметы, - так же, как фильтр на <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />. Делается это в <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" />.

Ячейки также поддерживают ограничения: и максимальную вместимость в байтах, и количество типов можно урезать ниже их обычных значений.

Эти настройки задаются в <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" />.

Предметы можно перетаскивать в слоты прямо из NEI, даже если самого предмета у тебя нет.

## Улучшения
Ячейки хранения поддерживают следующие улучшения, которые вставляются через <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" />:

*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" /> (недоступна для жидкостных ячеек) позволяет размечать ячейку по степени повреждения и/или игнорировать NBT предмета
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> переключает фильтр с белого списка на чёрный
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:69" /> выделяет каждому типу одинаковый объём байт ячейки, так что один тип не сможет заполнить собой всю ячейку
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:68" /> уничтожает поступающие предметы, если ячейка заполнена (или заполнено место, выделенное под этот тип, при использовании карты равного распределения), - полезно, чтобы фермы не забивались. Не забудь настроить разметку!
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:55" /> позволяет фильтровать по словарю руд и поддерживает регулярные выражения
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:64" /> (работает только при включённой разметке) назначает предпочтительное место хранения для определённых предметов или жидкостей. Отмеченные предметы и жидкости будут храниться только в ячейках с Липкой картой, а не в другом доступном хранилище сети

# Корпуса

Большинство ячеек хранения собираются из компонента хранения и соответствующего корпуса. Для разной вместимости и разных типов хранения нужны разные корпуса. Некоторые особые ячейки хранения крафтятся напрямую и корпуса не требуют.

*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:39" /> используется для крафта предметных ячеек хранения от 1k до 64k
<br> <RecipesFor id="appliedenergistics2:item.ItemBasicStorageCell.1k" output="appliedenergistics2:item.ItemBasicStorageCell.1k" />
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="appliedenergistics2:item.ItemMultiMaterial:39" limit="3" />

*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:61" /> используется для крафта предметных ячеек хранения от 256k до 16384k
<br> <RecipesFor id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" output="appliedenergistics2:item.ItemAdvancedStorageCell.256k" />
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="appliedenergistics2:item.ItemMultiMaterial:61" />

*   <ItemLink id="ae2fc:fluid_storage_housing" /> используется для крафта жидкостных ячеек хранения от 1k до 64k
<br> <RecipesFor id="ae2fc:fluid_storage1" output="ae2fc:fluid_storage1"/>
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="ae2fc:fluid_storage_housing" handlerId="gt.recipe.assembler" />

*   <ItemLink id="ae2fc:fluid_storage_housing:1" /> используется для крафта жидкостных ячеек хранения от 256k до 16384k
<br> <RecipesFor id="ae2fc:fluid_storage256" output="ae2fc:fluid_storage256"/>
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="ae2fc:fluid_storage_housing:1" />

*   <ItemLink id="ae2fc:fluid_storage_housing:2" /> используется для крафта мульти-жидкостных ячеек хранения от 1k до 64k
<br> <RecipesFor id="ae2fc:multi_fluid_storage1" output="ae2fc:multi_fluid_storage1" />
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="ae2fc:fluid_storage_housing:2" />

*   <ItemLink id="ae2fc:fluid_storage_housing:3" /> используется для крафта мульти-жидкостных ячеек хранения от 256k до 16384k
<br> <RecipesFor id="ae2fc:multi_fluid_storage256" output="ae2fc:multi_fluid_storage256" />
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="ae2fc:fluid_storage_housing:3" />

*   <ItemLink id="thaumicenergistics:storage.casing" /> используется для крафта ячеек хранения эссенции
<br> <RecipesFor id="thaumicenergistics:storage.essentia" output="thaumicenergistics:storage.essentia" />
<br> Сами корпуса крафтятся так:
<br> <RecipesFor id="thaumicenergistics:storage.casing" />

# Компоненты хранения

Компоненты хранения - это основа МЭ ячеек хранения, они определяют их вместимость.

Каждый следующий тир вмещает в четыре раза больше, а для его крафта нужны четыре компонента предыдущего тира. Также их можно производить напрямую в сборщике электросхем.

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

# Предметные ячейки хранения

Стандартные предметные ячейки хранения вмещают до 63 разных типов предметов и существуют во всех стандартных размерах.

<Column>
  <Row>
    <Recipe id="appliedenergistics2:item.ItemBasicStorageCell.1k" handlerName="Shaped Crafting" />

    <Recipe id="appliedenergistics2:item.ItemBasicStorageCell.4k" handlerName="Shaped Crafting" />

    <Recipe id="appliedenergistics2:item.ItemBasicStorageCell.16k" handlerName="Shaped Crafting" />

    <Recipe id="appliedenergistics2:item.ItemBasicStorageCell.64k" handlerName="Shaped Crafting" />
  </Row>

  <Row>
    <Recipe id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" handlerName="Shaped Crafting" />

    <Recipe id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" handlerName="Shaped Crafting" />

    <Recipe id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" handlerName="Shaped Crafting" />

    <Recipe id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" handlerName="Shaped Crafting" />
  </Row>
</Column>

## Особые предметные ячейки хранения

*   <ItemLink id="appliedenergistics2:item.ItemVoidStorageCell" /> уничтожает все помещённые в неё предметы
<br><Recipe id="appliedenergistics2:item.ItemVoidStorageCell" />
*   <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Container" /> хранит только один тип предметов и даёт 65 536 байт вместимости
<br><Recipe id="appliedenergistics2:item.ItemExtremeStorageCell.Container" />
*   <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Quantum" /> хранит только один тип предметов и даёт 134 217 727 байт вместимости
<br><Recipe id="appliedenergistics2:item.ItemExtremeStorageCell.Quantum" />
*   <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Singularity" /> хранит только один тип предметов и даёт 576 460 752 303 423 487 байт вместимости
<br><Recipe id="appliedenergistics2:item.ItemExtremeStorageCell.Singularity" />
*   <ItemLink id="appliedenergistics2:item.ItemExtremeStorageCell.Universe" /> хранит до 63 типов предметов и даёт 576 460 752 303 423 487 байт вместимости
<br><Recipe id="appliedenergistics2:item.ItemExtremeStorageCell.Universe" />

## Переносное хранилище предметов

Переносные ячейки работают как крошечный <ItemLink id="appliedenergistics2:tile.BlockChest" />, который можно носить с собой, - что-то вроде рюкзака.

Их можно заряжать в <ItemLink id="appliedenergistics2:tile.BlockCharger" />.

В отличие от стандартных ячеек хранения, они вмещают только 27 типов предметов, а их общая вместимость - 512 байт.

Они поддерживают только следующие карты улучшений:

*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:29" />
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" />
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:55" />
*   <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:64" /> 

<RecipesFor id="appliedenergistics2:item.ToolPortableCell" />

# Жидкостные компоненты хранения

Жидкостные компоненты хранения - это основа МЭ жидкостных ячеек хранения, они определяют их вместимость.

Каждый следующий тир вмещает в четыре раза больше, а для его крафта нужны четыре компонента предыдущего тира. Также их можно производить напрямую в сборщике электросхем.

# Жидкостные ячейки хранения

Стандартные жидкостные ячейки хранения делятся на две категории:

Жидкостные ячейки хранения хранят только один тип жидкости.

Мульти-жидкостные ячейки хранения хранят до пяти типов жидкостей.

Обе категории существуют во всех стандартных тирах вместимости.

## Особые жидкостные ячейки хранения

*   <ItemLink id="ae2fc:fluid_storage.void" /> уничтожает все помещённые в неё жидкости
<br><Recipe id="ae2fc:fluid_storage.void" />
*   <ItemLink id="ae2fc:fluid_storage.infinity.water" /> даёт неограниченный запас воды, до 4 503 599 627 370 495 мБ
<br><Recipe id="ae2fc:fluid_storage.infinity.water" />
*   <ItemLink id="ae2fc:fluid_storage.quantum" /> хранит только один тип жидкости и даёт 134 217 727 байт вместимости
<br><Recipe id="ae2fc:fluid_storage.quantum" />
*   <ItemLink id="ae2fc:fluid_storage.singularity" /> хранит только один тип жидкости и даёт 2 251 799 813 685 247 байт вместимости
<br><Recipe id="ae2fc:fluid_storage.singularity" />
*   <ItemLink id="ae2fc:fluid_storage.Universe" /> хранит до 63 типов жидкостей и даёт 4 503 599 627 370 495 байт вместимости
<br><Recipe id="ae2fc:fluid_storage.Universe" />

## Переносная жидкостная ячейка

Переносные жидкостные ячейки хранят до пяти типов жидкостей, а их общая вместимость - 256 байт.

Карты улучшений они не поддерживают.

<RecipesFor id="ae2fc:portable_fluid_cell" />

# Компоненты хранения эссенции

Компоненты хранения эссенции - это основа МЭ ячеек хранения эссенции, они определяют их вместимость.

Каждый следующий тир вмещает в четыре раза больше, а для его крафта нужны четыре компонента предыдущего тира. Также их можно производить напрямую в сборщике электросхем.

# Ячейки хранения эссенции

Ячейки хранения эссенции от 1k до 64k поддерживают 12 типов эссенции.

Начиная с 256k, каждый тир добавляет ещё 12 поддерживаемых типов эссенции.

## Особые ячейки хранения эссенции

*   <ItemLink id="thaumicenergistics:storage.essentia:9" /> хранит только один тип эссенции и даёт 134 217 727 байт вместимости
<br><Recipe id="thaumicenergistics:storage.essentia:9" />
*   <ItemLink id="thaumicenergistics:storage.essentia:10" /> хранит только один тип эссенции и даёт 2 305 843 009 213 693 951 байт вместимости
<br><Recipe id="thaumicenergistics:storage.essentia:10" />
*   <ItemLink id="thaumicenergistics:storage.essentia:4" /> даёт бесконечный запас эссенции каждого типа, до 4 503 599 627 370 495 единиц на тип
<br><Recipe id="thaumicenergistics:storage.essentia:4" />

# Творческие ячейки хранения

<Row>
  <ItemImage id="appliedenergistics2:item.ItemCreativeStorageCell" scale="2" />

  <ItemImage id="ae2fc:creative_fluid_storage" scale="2" />
</Row>

Творческие ячейки **не дают бесконечного хранилища**. Вместо этого они работают как бесконечный источник и бесконечный сток для того предмета или жидкости, под который ты их [разметил](cell_workbench.md), до 4 503 599 627 370 495 единиц.