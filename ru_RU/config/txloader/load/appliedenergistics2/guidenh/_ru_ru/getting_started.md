---
navigation:
  title: Начнём
  position: 10
  parent: /index.md
---

# Быстрый старт

# Простая система хранения
Чтобы было проще начать работу с AE2, давай сначала создадим простую сеть, которая обеспечит основную функцию AE2: хранение.

## Что нам понадобится
Applied Energistics 2 — это, по сути, инопланетная технология. По всему миру разбросаны [метеориты](./ae2-mechanics/meteorites.md). В их центре может находиться <ItemLink id="appliedenergistics2:tile.BlockSkyChest" showIcon="true"/>. Внутри этих сундуков у вас есть шанс найти основные предметы AE2: <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:13" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:14" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:15" showIcon="true"/> и <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:19" showIcon="true"/>. Они нужны для крафта компонентов и блоков из мода. В сборке AE2 также интегрирована в GregTech, поэтому для создания системы МЭ вам необходимо достичь EV тира и добыть титан.

## Материалы
Когда ты достигнешь технологического уровня, необходимого для постройки МЭ системы, тебе также понадобятся следующие материалы:
- <ItemImage id="gregtech:gt.blockores2:516" label="right"/>
  - Из него надо будет добыть <ItemImage id="gregtech:gt.metaitem.01:2516"  label="right"/> и <ItemImage id="gregtech:gt.metaitem.01:8516" label="right"/> которые являются важным сырьем для крафта предметов и блоков из мода.
- <ItemImage id="gregtech:gt.blockores2:28" label="right"/>
  - Множество блоков из AE для крафта требуют <ItemImage id="gregtech:gt.metaitem.01:17028" label="right" />.
- А вот и остальные основные материалы: <ItemImage id="minecraft:redstone" label="right" />, <ItemImage id="minecraft:diamond" label="right"/> и <ItemImage id="dreamcraft:CircuitHV"  label="right"/>. Ты наверняка уже сталкивался с ними на пути к EV тиру, поэтому их подробного описания здесь не будет.

## Постройка
И вот когда всё готово, давай построим простенькую сеть хранения. Тебе надо построить по сцене ниже.

<GameScene zoom="5" interactive={true} width="400" height="300">
  <ImportStructure src="../assets/structures/getting_started.snbt" />
  <IsometricCamera yaw="200" pitch="30" />
  <BlockAnnotation pos="5 0 0" color="#e5e90c" alwaysOnTop={true}>
  <Color color="#e5e90c">Это отладочный генератор, установленный для демонстрации. Его невозможно получить в выживании. Для нормального использования подключите МЭ сеть к энергосети.</Color>
  </BlockAnnotation>
</GameScene>

МЭ система в этой сцене получает питание от GT энергосети, расположенной слева. Она обеспечивает базовые функции хранения предметов:
- <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="true"/> обеспечивает [каналы](./ae2-mechanics/channels.md) для всей сети.
- <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" showIcon="true"/> подключает все компоненты к сети.
- <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" showIcon="true"/> кладётся в <ItemLink id="appliedenergistics2:tile.BlockDrive" showIcon="true"/> для получения места для хранения.
- <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" showIcon="true"/> размезается рядом с сундуком для того, чтобы объединить его объём с МЭ сетью.
- <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" showIcon="true"/> позволяет игрокам взаимодействовать с МЭ сетью и её хранилищем.

Теперь ты можешь нажать ПКМ по терминалу для открытия МЭ сети хранения, класть и доставать предметы из терминала также, как делали бы с обычным сундуком. Предметы вручную помещённые в сундук будут отображаться в МЭ терминале . На этом этапе ты успешно построил МЭ сеть хранения, но это лишь верхушка айсберга МЭ сетей. Продолжайте изучать руководство, чтобы узнать больше

[Предметы и блоки](items_blocks_index.md)

[Механики AE2](ae2_mechanics_index.md)

[Советы и примеры](tricks_example_index.md)