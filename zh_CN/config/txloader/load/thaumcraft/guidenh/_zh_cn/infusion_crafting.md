---
item_ids:
  - Thaumcraft:blockStoneDevice:2
  - Thaumcraft:blockStoneDevice:1
navigation:
  title: Infusion Crafting
  parent: ./index.md
  icon: 'Thaumcraft:blockStoneDevice:2'
  position: 50
---

# Infusion Crafting

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**Infusion Crafting** infuses essentia and surrounding ingredients into a central item to create wand components, magical devices, equipment, and materials for mod integration.<br>
As research progresses, the same altar can also handle equipment upgrades and infusion enchanting.

Using an Infusion Altar requires attention to <Color color="#B7A0D6">recipes, stability, and essentia supply</Color>.<br>
In GTNH, Thaumic Energistics, Infusion Claws, Infusion Intercepters, and other devices can handle supply and activation, allowing the altar to support continuous production.

## The Infusion Altar

<GameScene interactive={true} wrap="square" align="right" width="240" height="220" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/infusion_altar.snbt" />
</GameScene>

The altar's main structure consists of one <ItemLink id="Thaumcraft:blockStoneDevice:2" showIcon="left" />, a central <ItemLink id="Thaumcraft:blockStoneDevice:1" showIcon="left" />, and four pillars. The pillars are built from <ItemLink id="Thaumcraft:blockCosmeticSolid:6" showIcon="left" /> and <ItemLink id="Thaumcraft:blockCosmeticSolid:7" showIcon="left" />, becoming Infusion Pillars when activated with a wand.

The central pedestal sits two blocks directly below the matrix and holds the item being infused. Additional pedestals around it hold the recipe ingredients. The scene shows an activated altar and a set of outer pedestals, which can be expanded to suit recipes.

- **Structure activation:** Complete Infusion research, build the structure shown in the Thaumonomicon, and right-click the matrix with a wand. Leave the empty spaces within the main structure clear; logistics devices can be connected after activation.
- **Outer pedestal range:** Pedestals must be below the matrix, within 8 blocks along each horizontal axis, X and Z, and no more than 10 blocks below it.
- **Pedestal layers:** Only one outer pedestal is recognized per vertical column. Offset their horizontal positions when using multiple layers.
- **Space allocation:** Leave room below the central pedestal for an essentia connection and below the surrounding pedestals for item logistics. An Infusion Claw can be installed above the matrix.

## Recipes and the Crafting Process

An infusion recipe requires a central item, outer ingredients, the specified essentia, and the relevant research completed by the player activating it. The Thaumonomicon and NEI show the current recipe's items, essentia quantities, and instability.

A standard altar first draws essentia, then absorbs the outer ingredients one by one. The finished item remains on the central pedestal. Outer ingredient positions can be rearranged, provided their types and quantities match the recipe.

> [!WARNING]
> A standard altar does not check that all required essentia is available before starting. Missing essentia or ingredients knocked off pedestals stall the ritual while risk checks continue, increasing instability or essentia requirements. Prepare the essentia and ingredients and check altar stability before crafting.

Each outer ingredient entry occupies a separate pedestal. When a recipe requires the same ingredient several times, multiple pedestals are needed for matching. Returned containers or reusable ingredients may remain on their pedestals; arrange their collection for batch production.

## Pedestal Layout and Stability

The altar checks <Color color="#B7A0D6">central symmetry</Color>: two positions at the same height correspond when rotated 180° around the matrix's vertical axis. For example, a pedestal three blocks east and one block north of the matrix pairs with one three blocks west and one block south.

- **Pair pedestals:** Each outer pedestal should have a corresponding pedestal on the opposite side. Empty pedestals also count toward symmetry.
- **Pair occupied positions:** Two opposite pedestals remain balanced when both hold ingredients, which can be different items. Additional stabilizers can compensate for the occupancy imbalance caused by an odd number of ingredients.
- **Remove unused ingredients:** Items on other pedestals within range participate in recipe matching. Leaving ingredients from another craft may prevent the recipe from being recognized.
- **Check after adjustments:** Use an Arcane Abacus after adding or removing pedestals, moving stabilizers, or connecting addon devices.

The recipe's instability and the altar's environmental modifier together determine the initial risk of the ritual. Stabilizers should offset the target recipe's risk and leave a margin for shortages and automatic activation devices.

An <ItemLink id="WitchingGadgets:item.WG_Material:7" showIcon="left" /> reads the matrix's stability, identifies unpaired stabilizers, and shows risk and essentia cost information for the current or available recipe.<br>
Arrange the pedestals and stabilizers first, then place the target recipe's ingredients to check the result.

## Placing Stabilizers

Stabilizers include candles, skulls, crystals, and suitable blocks from addons. Blocks with a tooltip indicating that they can stabilize an Infusion Altar can be found in NEI and used around the altar.

A <ItemLink id="thaumicbases:quicksilverBlock" showIcon="left" /> is a common choice in GTNH and suits a foundation with multiple layers of stabilizers. Candles, skulls, and other valid stabilizers can also be used according to the materials available.

- **Effective range:** Up to 12 blocks along each of the X and Z axes, 5 blocks above, and 10 blocks below the matrix.
- **Pairing:** Place valid stabilizers at the same height in positions centrally symmetric about the matrix. Unpaired stabilizers increase instability.
- **Multiple layers:** Each layer needs its own symmetry. Stabilizers can be placed beneath the altar to leave space at ground level for access and logistics.
- **Central column:** The vertical column directly above and below the matrix is excluded from ordinary stabilizer symmetry checks.

Every 10 ordinary stabilizers placed in pairs provide 1 point of stability in total. For larger foundations, keep each layer's boundary complete and use an Arcane Abacus to locate missing blocks.

Other valid blocks within the stabilizer range also count. Nearby decorations, another altar's stabilizers, and blocks added later can affect the existing altar's stability.

## Essentia Supply

A standard altar draws the required aspects from essentia sources near the matrix. Each <ItemLink id="Thaumcraft:blockJar:0" showIcon="left" /> holds 64 points; prepare several jars of the same type when an aspect's requirement exceeds one jar.

- **Jar supply:** Suitable for a small set of recipes or occasional infusions. Prepare each required aspect separately.
- <ItemLink id="Thaumcraft:blockMirror:6" showIcon="left" />: Linked pairs supply the altar with essentia from a distant storage area.
- <ItemLink id="thaumicenergistics:thaumicenergistics.block.infusion.provider" showIcon="left" />: Once connected to an ME network, it lets the altar draw essentia from network stocks. Place it within the altar's draw range to reduce jar transport.

When a required aspect is out of stock, an Infusion Provider can request essentia autocrafting in batches of 32 points.<br>
This requires an available pattern and crafting CPU. Keeping common aspects in stock reduces waiting during continuous infusion.

A standard matrix still draws essentia in successive steps. More aspect types and larger quantities make this stage take longer. Recipes with high essentia demand can use an Infusion Intercepter or Advanced Infusion Provider.

Refer to the "Alchemy and Essentia" chapter for production, storage, and transport. When several altars share stocks, account for their combined demand during simultaneous operation.

## Infusion Accidents and Losses

Unstable infusions can knock ingredients off pedestals, destroy ingredients, release Flux, or harm nearby entities.<br>
Missing ingredients delay crafting, increasing the chance of further accidents.

- **Destroyed ingredients:** Replace the missing items. For valuable recipes, prepare spare outer ingredients where possible.
- **Essentia stops flowing:** Check which aspects the matrix still needs, jar contents, provider stocks, and supply paths.
- **Essentia demand increases:** Replenish the quantities currently required by the ritual and address the shortage. Further waiting may cause additional losses.
- **Flux spills:** Place Flux cleanup devices near the altar and leave access for replenishing ingredients and collecting items.

> [!WARNING]
> Essentia and ingredients already absorbed are not automatically returned when an infusion is interrupted. Removing or replacing the central item may terminate the ritual. Automatic product collection should also wait until crafting is complete to avoid extracting the input early.

If accidents recur, improve altar stability and resolve supply problems before consuming more materials. For high-risk recipes, reduce the time spent waiting for essentia or missing ingredients.

## Infusion Enchanting

After completing **Infusion Enchantment** research, the altar can apply supported enchantments to tools, weapons, and armor. These recipes require experience as well as items and essentia, drawing it from players near the altar.

- **Higher enchantment levels:** Repeat the same enchantment until its permitted maximum level. Higher levels require more essentia and experience.
- **Existing enchantments:** Other enchantments on the item increase resource costs and instability. Check the base requirements in the book against the target item's current state.
- **Applicability and compatibility:** Enchantment rules still determine whether an enchantment applies to an item and can coexist with its existing enchantments.

When preparing a set of equipment, plan the processing order around the desired final enchantments and use an Arcane Abacus to check the costs for the current item. Equipment with several enchantments benefits from an altar with a larger stability margin.

NH's addons also provide devices such as the Osmotic Enchanter and Overchanting Table. Their recipes, resource costs, and level rules are described in their own research entries.

## Automatic Activation and Item Logistics

An <ItemLink id="gadomancy:BlockInfusionClaw" showIcon="left" /> is installed above the Runic Matrix. With a wand or staff inside, it can trigger infusion through a redstone signal from a side. The device is bound to its owner and uses that player's research for recipe recognition.

The Infusion Claw needs Vis replenishment for its wand and can receive power from a Centi-Vis network.<br>
It adds instability to the rituals it activates. A wand with greater capacity or a suitable staff reduces this effect.

Item automation mainly handles the following tasks:

- **Central item allocation:** Send the central item and outer ingredients to their assigned pedestals. Maintain correct allocation rules when several recipes share an altar.
- **Individual outer inputs:** Each ingredient entry needs a pedestal, including repeated occurrences of the same ingredient.
- **Activation control:** Trigger the Infusion Claw after the ingredients are in place. For continuous production, wait for the previous craft to finish.
- **Product collection:** Identify and extract the finished item from the central pedestal. Also handle containers or reusable ingredients left on outer pedestals.

An ME network can manage inputs and products, while redstone, OC, or other control devices coordinate activation and collection.<br>
Handle returned containers or leftover ingredients before the next craft begins to prevent continuous production from stalling.

For Centi-Vis sources and connections, see [Wands, Vis and Nodes](./wands_vis_nodes.md).

## Increasing Infusion Speed

An <ItemLink id="thaumicinsurgence:infusionIntercepter" showIcon="left" /> is installed directly below the central pedestal and receives essentia through its bottom face.<br>
Connect essentia tubes or a Thaumic Energistics Essentia Provider below it to send the required essentia directly into the corresponding Runic Matrix.

With an ME Essentia Provider and sufficient stocks at the input, it can supply large amounts of essentia very quickly. With tubes, actual supply speed limits its performance. It serves only the altar directly above it; activate the main altar structure before installing it.

An <ItemLink id="thaumicenergistics:thaumicenergistics.block.advanced.infusion.provider" showIcon="left" /> supplies all required essentia to an active infusion at once and requests autocrafting for the quantities missing.<br>
It can bind to multiple matrices within 12 blocks along each of the X and Z axes and 5 blocks vertically.

- **Infusion Intercepters** provide fast essentia supply for individual altars.
- **Advanced Infusion Providers** let multiple altars share network stocks and essentia autocrafting.
- **World Accelerators** can speed up matrix operation further, but first ensure adequate stability and supply. Acceleration during shortages also speeds up risk checks while the ritual is stalled.

Once essentia supply takes less time, absorbing outer ingredients individually still contributes to crafting time. To expand production, arrange multiple altars according to the number of recipes and ingredients, with complete input and collection control for each.

## Troubleshooting

- **Right-clicking with a wand does not start infusion:** Check structure activation, research completion, the central item and outer ingredients, and any unrelated ingredients left within range.
- **Some outer ingredients are not recognized:** Check whether their pedestals are below the matrix, within range, and share a vertical column with another pedestal.
- **Risk remains high after placing stabilizers:** Use an Arcane Abacus to check asymmetric positions, stabilizer range, and occupied outer pedestals. Include the extra instability from an Infusion Claw when using one.
- **An Infusion Claw does not start the recipe:** Check the owner's research, the inserted wand, power supply, and redstone trigger, then verify the recipe ingredients on the altar.
- **An Intercepter supplies no essentia:** Check that it is directly below the central pedestal, its bottom face connects to a valid essentia source, and the source contains the required aspects.
- **Automation completes only the first craft:** Check collection of the central product and outer leftovers, allocation of the next set of ingredients, and whether the activation signal triggers again.

</Column>
