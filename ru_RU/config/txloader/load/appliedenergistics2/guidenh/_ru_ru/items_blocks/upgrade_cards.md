---
navigation:
  parent: /items_blocks_index.md
  title: Карты улучшений
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

# Upgrade Cards
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
Карты улучшения изменяют поведение устройств и механизмов из AE2, повышая их скорость, улучшая их
фильтры, обеспечивая возможность управления с помощью редстоуна и т.д.

## Карты-компоненты

<Row>
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:25" scale="2" />

  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:28" scale="2" />
</Row>

Карты улучшения создаются на основе базовых или продвинутых карт.

<Row>
  <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:25" />

  <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:28" />
</Row>

## Карта красного камня

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" />

Карта красного камня добавляет возможность контролировать устройство при помощи красного камня, добавляя переключать в интерфейс для выбора режима работы.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:26" />

## Карта ёмкости

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:27" scale="2" />

Карта ёмкости увеличивает количество слотов для фильтров в плоскости формирования и в шинах: импорта, экспорта и хранения.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:27" />

## Пустотная карта переполнения

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:68" scale="2" />

Пустотная карта переполнения применяется к [ячейкам хранения](storage_cells.md) в <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" />.
Она удаляет поступающие предметы, когда ячейка переполнена. Настройте [разделы](cell_workbench.md) перед этим.
При использовании вместе с картой равного распределения предметы удаляются, как только его собственный раздел заполняется, даже если в других разделах ещё есть свободное место.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:68" />

## Карта нечёткости

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:29" scale="2" />

Карта нечёткости позволяет сопоставлять устройства и инструменты по прочности и/или игнорировать NBT-атрибуты предметов. Это дает возможность экспортировать все железные топоры независимо от их прочности или зачарований, либо экспортировать только поврежденные алмазные мечи вместо полностью целых.

Ниже приведен пример того, как работают режимы нечёткого сравнения прочности. Слева показана конфигурация шины, а в верхней строке — сравниваемый предмет.

| 25%                    | Кирка сломана на 10% | Кирка сломана на 30% | Кирка сломана на 80% | Кирка полностью цела |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Почти сломанная кирка  | ✔                   | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            |
| Полностью целая кирка  | \*\*\*\*            | ✔                   | ✔                   | ✔                   |

---

| 50%                    | Кирка сломана на 10% | Кирка сломана на 30% | Кирка сломана на 80% | Кирка полностью цела |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Почти сломанная кирка  | ✔                   | ✔                   | \*\*\*\*            | \*\*\*\*            |
| Полностью целая кирка  | \*\*\*\*            | \*\*\*\*            | ✔                   | ✔                   |

---

| 75%                    | Кирка сломана на 10% | Кирка сломана на 30% | Кирка сломана на 80% | Кирка полностью цела |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Почти сломанная кирка  | ✔                   | ✔                   | \*\*\*\*            | \*\*\*\*            |
| Полностью целая кирка  | \*\*\*\*            |                     | ✔                   | ✔                   |

---

| 99%                    | Кирка сломана на 10% | Кирка сломана на 30% | Кирка сломана на 80% | Кирка полностью цела |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Почти сломанная кирка  | ✔                   | ✔                   | ✔                   | \*\*\*\*            |
| Полностью целая кирка  | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            | ✔                   |

---

| любое соответствие      | Кирка сломана на 10% | Кирка сломана на 30% | Кирка сломана на 80% | Кирка полностью цела |
| :--------------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| Почти сломанная кирка  | ✔                   | ✔                   | ✔                   | **✔**               |
| Полностью целая кирка | **✔**               | **✔**               | **✔**               | ✔                   |

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:29" />

## Карта ускорения

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />

Эта карта ускоряет процессы. Она позволяет шинам импорта и экспорта переносить больше предметов за одну операцию, а также ускоряет работу высекателя и молекулярного сборщика.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:30" />

## Карта гиперускорения

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:56" scale="2" />

Карта гиперускорения это улучшенная версия обычной карты ускорения, однако её можно использовать только в МЭ порту ввода/вывода,
на MЭ шинах импорта и экспорта, а также жидкостных шинах импорта и экспорта.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:56" />

## Карта сверхсветового ускорения

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:67" scale="2" />

Карта сверхсветового ускорения это самая быстрая карта из AE для перемещения предметов или жидкостей, однако её можно использовать только в МЭ порту ввода/вывода и на шинах импорта/экспорта MЭ.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:67" />

## Карта инвертирования

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" />

Карта инвертирования меняет в устройстве или инструменте фильтр с белого на чёрный список.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:31" />

## Карта создания

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />

Карта создания позволяет устройствам отправлять запросы в твою систему [автокрафта](../ae2-mechanics/autocrafting.md) для получения необходимых предметов.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:53" />

## Карта равного распределения

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:69" scale="2" />

Карта равного распределения применяется к [ячейкам хранения](storage_cells.md) в <ItemLink id="appliedenergistics2:tile.BlockCellWorkbench" />.
Они разделяют ячейку на равные секции в соответствии с [разделами](cell_workbench.md), что не позволяет одному типу предметов заполнить всю ячейку.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:69" />

## Карта ёмкости интерфейса

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:54" scale="2" />

Каждая карта ёмкости интерфейса добавляет дополнительных 9 слотов для шаблонов в интерфейсе. Максимум - 3 карты на интерфейс.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:54" />

## Карта фильтрации по словарю руд

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:55" scale="2" />

Позволяет фильтровать по словарю руд и поддерживает поиск с использованием регулярных выражений(RegExp).

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:55" />

## Липкая карта

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:64" scale="2" />

Любые предметы, жидкости или эссенция размещенные в этой ячейке, могут храниться только в ячейках или шинах хранения, в которых также имеется липкая карта и нигде больше в сети.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:64" />

## Продвинутая карта блокировки

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:63" scale="2" />

Продвинутая карта блокировки распространяет действие блокировки на всю ME сеть, а не только на соседние хранилища. При включении, интерфейс предотвращает добавление материалов крафта, если в целевой сети уже присутствуют соответствующие предметы или жидкости.

В режиме по умолчанию блокировка срабатывает только при наличии в сети предметов или жидкостей, относящихся к рецепту (за исключением катализаторов, таких как линзы, электросхем или форм).

В свободном режиме блокировка срабатывает при наличии в сети любого предмета или жидкости.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:63" />

## Карта запирания

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:65" scale="2" />

Эта карта имеет 4 режима работы:

*   Режим 1: Никогда не блокирует крафты
*   Режим 2: Блокирует крафты пока не будет получен импульс красного камня
*   Режим 3: Блокирует крафты пока есть сигнал красного камня
*   Режим 4: Блокирует крафты пока нет сигнала красного камня

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:65" />

## Карта поддельного создания

<ItemImage id="appliedenergistics2:item.ItemMultiMaterial:66" scale="2" />

Если интерфейс оснащён этой картой, он сразу завершает **крафт** после его отправки, не дожидаясь получения результата. Это работает только в том случае, если конечным результатом отправленного задания является нужный продукт.

<RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:66" />
