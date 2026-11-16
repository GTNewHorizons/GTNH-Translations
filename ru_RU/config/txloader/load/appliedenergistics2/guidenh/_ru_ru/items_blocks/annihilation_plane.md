---
navigation:
  parent: /items_blocks_index.md
  title: МЭ плоскость уничтожения
  icon: appliedenergistics2:item.ItemMultiPart:300
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:300
- appliedenergistics2:item.ItemMultiPart:301
---

# МЭ плоскость уничтожения

<GameScene zoom="8" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/annihilation_plane.snbt" />
</GameScene>

Плоскость уничтожения способна ломать блоки и подбирать предметы. Она помещает предметы в [сетевое хранилище](../ae2_mechanics/import_export_storage.md), работая аналогично <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />. В обычных условиях после разрушения блока она активно подбирает предметы рядом с целевой позицией. Для предметов, которые напрямую сталкиваются с плоскостью, она подбирает только те предметы, которые находятся в пределах зоны столкновения на поверхности плоскости.

Плоскость уничтожения может ломать только те блоки, которые отвечают определённым условиям. Например, она не может сломать воздух, жидкости, бедрок, порталы Края, рамки портала Края или командные блоки. Блок также должен иметь неотрицательную твёрдость и проходить проверку прав на добычу.

<ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> и инструменты с этим зачарованием ведут себя так же, но затраты энергии в 16 раз выше, чем у плоскости уничтожения.

Плоскость уничтожения является [кабельным модулем](../ae2_mechanics/cables_subparts.md).

**НЕ ЗАБУДЬТЕ ВКЛЮЧИТЬ ФЕЙК-ИГРОКОВ В НАСТРОЙКАХ ЗАНЯТЫХ ЧАНКОВ**

## Фильтрация

Плоскость уничтожения сломает блок или подберёт предмет только в том случае, если добычу или предметы можно сохранить в её сети. Это означает, что для фильтрации *необходимо ограничить то, что может храниться в её сети*, вероятнее всего, выделив её в [подсеть](../ae2_mechanics/subnetworks.md). Этого можно добиться с помощью <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> или [разметки](cell_workbench.md) [ячеек](storage_cells.md).

<GameScene width="300" height="200" zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
    Отфильтруйте добычу с целевого блока.
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
    Разметьте хранилище под добычу.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Плоскость уничтожения фильтрует *по выпадающим предметам*. Поэтому, если вы хотите ломать только <ItemLink id="etfuturum:amethyst_cluster_2:6" />, плоскость должна быть зачарована на шёлковое касание. Не полностью выросшие бутоны аметиста ничего не роняют, а сеть всегда может хранить "ничего", поэтому обычная плоскость уничтожения будет продолжать их ломать.

## Рецепт

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:300" />