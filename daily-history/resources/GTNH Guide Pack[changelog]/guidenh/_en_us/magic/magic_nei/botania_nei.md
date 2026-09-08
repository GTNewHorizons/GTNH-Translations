---
navigation:
  title: Botania NEI Handler Cleanup
  parent: magic_nei.md
  icon: Botania:lexicon
categories:
    - Magic NEI
author: koolkrafter5
date: 2026-06-10
---

Various NEI handlers for Botania got some attention this update:
- Lexicon entries are now also shown when finding recipes for items, not just uses.
- The Floating Flower handler can now use NEI's Overlay Button to move items into the inventory/crafting table grid.
- You can now actually see all recipes for the Mana Infusion, Petal Apothecary, and Runic Altar handlers. They used to have items in the way of the area to click, so you used to only see that item's recipe. Now they are rendered before the clickable area is made.
- Crafting stations like the Mana Pool (and its Catalysts) and the Petal Apothecary are no longer added to the ingredients of bookmarked / patterned recipes.
- Botanical Brewery handler includes all items that can have brews applied as catalysts on the left.
- Petal Apothecary and Runic Altar recipes now include "Any seed" and livingrock in their ingredients respectively.

<Recipe id="minecraft:redstone" handlerId="botania.manaPool"/>
<Recipe id="Botania:rune:1" handlerId="botania.runicAltar"/>