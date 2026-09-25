---
navigation:
  parent: /ae2_mechanics_index.md
  title: Autocrafting
  icon: appliedenergistics2:item.ItemEncodedPattern
---

# Autocrafting

### The Big One

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/autocraft_setup_greebles.snbt" />
  <Block id="minecraft:furnace" x="9" y="1" z="0" facing="north" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Autocrafting is one of the primary functions of AE2. Instead of manually having to craft the correct number of each sub-ingredient
and labor away like some sort of *plebian*, you can ask your ME system to do it for you. Or automatically craft items and export them somewhere.
Or automatically keep certain amounts of items in stock through clever emergent behavior. It also works with fluids, and, if you have
certain addons for extra mod material types, like Thaumcraft essentia, those materials too. It's pretty great.

It is quite a complex topic, so strap in and let's go.

An autocrafting setup consists of 3 things:
- The thing sending the crafting request
- The crafting CPU
- The <ItemLink id="appliedenergistics2:tile.BlockInterface" />.

Here is what happens:

1.  Something creates a crafting request. This can be you in the terminal clicking on something autocraftable,
    or an export bus or interface with a crafting card requesting one of the item they're set to export/stock.

*   (**IMPORTANT:** use whatever you have bound to "pick block" (usually middle-mouse) to request crafts of something you already have in stock, this can conflict with inventory sorting mods),

2.  The ME system calculates the required ingredients and prerequisite crafting steps to fulfill the request, and stores them in the selected crafting CPU

3.  The <ItemLink id="appliedenergistics2:tile.BlockInterface" /> with the relevant [pattern](../items_blocks/patterns.md) pushes the ingredients specified in the pattern to any adjacent inventory.
    In the case of a crafting table recipe (a "crafting pattern") this will be a <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" />.
    In the case of a non-crafting recipe (a "processing pattern") this will be some other block or machine or elaborate redstone-controlled setup.

4.  The result of the craft is returned to the system somehow, be it by import bus, interface, or pushing the result back into a interface.
    **Note that an "item entering system" event must occur, you can't just pipe the result into a chest with a <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> on it.**

5.  If that craft is a prerequisite for another craft in the request, the items are stored in that crafting CPU and then used in that craft.

## Recursive Recipes

One thing the autocrafting algorithm *cannot* handle is recursive recipes. For example, duplication recipes like
"1 redstone dust = 2 redstone dust", from throwing redstone in a Botania manapool. However, there is [a way to handle these recipes.](../tricks_example/recursive_crafting_setup.md)

# Patterns

<ItemImage id="appliedenergistics2:item.ItemEncodedPattern" scale="4" />

Patterns are made in a <ItemLink id="appliedenergistics2:item.ItemMultiPart:340" /> out of blank patterns.

There are several different types of pattern for different things:

*   <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" />s encode recipes made by a crafting table. They can be put directly in a <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> to make it
    craft the result whenever given the ingredients, but their main use is in a <ItemLink id="appliedenergistics2:tile.BlockInterface" /> next to a molecular assembler.
    ME Interfaces have special behavior in this case, and will send the relevant pattern along with the ingredients to adjacent assemblers.
    Since assemblers auto-eject the results of crafts to adjacent inventories, an assembler on a interface is all that is needed to automate crafting patterns.

***

*   <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />s are where a lot of flexibility in autocrafting comes from. They are the most generalized type, simply
    saying "if a interface pushes these ingredients to adjacent inventories, the ME system will receive these items at some point in the
    near or distant future". They are how you will autocraft with almost any modded machine, or furnaces and the like. Because they are so
    general in use and do not care what happens between pushing ingredients and receiving the result, you can do some really funky stuff, like inputting
    the ingredients into an entire complex factory production chain which will sort out stuff, take in other ingredients from infinitely-producing
    farms, print the entirety of the Bee Movie script, the ME system does not care as long as it gets the result the pattern specifies. In fact,
    it doesn't even care if the ingredients are in any way related to the result. You could tell it "1 cherry wood planks = 1 nether star" and have
    your wither farm kill a wither upon receiving a cherry wood planks and it would work.

The source also registers <ItemLink id="appliedenergistics2:item.ItemTunnelPattern" />, a processing-pattern variant used only by tunnel-pattern setups.

Multiple <ItemLink id="appliedenergistics2:tile.BlockInterface" />s with identical patterns are supported and work in parallel. Additionally, you can have a pattern say,
for example, 8 cobblestone = 8 stone instead of 1 cobblestone = 1 stone, and the interface will insert 8 cobblestone into
your smelting setup every operation instead of one at a time.

With a [Pattern Optimization Matrix](../items_blocks/pattern_optimization_matrix.md) connected to the network, the crafting confirmation screen can optimize pattern batch sizes. The interface must also have **Allow pattern optimization** enabled.

## The Most General Form of "Pattern"

There is actually an even more "general" form of "pattern" than a processing pattern. A <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> with a crafting card can be set
to emit a redstone signal in order to craft something. This "pattern" does not define, or even care about ingredients.
All it says is "If you emit redstone from this level emitter, the ME system will receive this item at some point in the
near or distant future". This is usually used to activate and deactivate infinite farms which require no input ingredients,
or to activate a system that handles recursive recipes (which standard autocrafting cannot understand) like, for example, "1 cobblestone = 2 cobblestone"
if you have a machine that duplicates cobblestone.

# The Crafting CPU

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Crafting CPUs manage crafting requests/jobs. They store the intermediate ingredients while crafting jobs with multiple steps are
being carried out, and affect how big jobs can be, and to some degree how fast they are completed. They are multiblocks, and
must be rectangular prisms with at least 1 crafting storage.

Crafting CPUs are made out of:

*   (Required) [Crafting storages](../items_blocks/crafting_cpu.md), available in all the standard cell sizes (1k, 4k, 16k, 64k, 256k). They store the ingredients and
    intermediate ingredients involved in a craft, so larger or more storages are required for the CPU to handle crafting jobs
    with more ingredients.
*   (Optional) <ItemLink id="appliedenergistics2:tile.BlockAdvancedCraftingUnit" />s, they make the system send out ingredient batches from interfaces more often.
    This allows, say, a interface surrounded by 6 molecular assemblers to send ingredients to (and thus use) all 6 at once instead of just one.
*   (Optional) <ItemLink id="appliedenergistics2:tile.BlockCraftingMonitor" />s, they display the job the CPU is handling at the moment. They can be colored via a <ItemLink id="appliedenergistics2:item.ToolColorApplicator" />
*   (Optional) <ItemLink id="appliedenergistics2:tile.BlockCraftingUnit" />s, they simply fill space in order to make the CPU a rectangular prism.

Each crafting CPU handles 1 request or job, so if you want to request both a calculation processor and 256 smooth stone at once, you need 2 CPU multiblocks.

They can be set to handle requests from players, automation (export busses and interfaces), or both.

# ME Interfaces

<Row>
<BlockImage id="appliedenergistics2:tile.BlockInterface" scale="4" />

<BlockImage id="appliedenergistics2:tile.BlockInterface" meta="0" nbt='{LOCK_CRAFTING_MODE:"NONE",orientation_up:"DOWN",BLOCK:"NO",PATTERN_OPTIMIZATION:"YES",waitingToSend:[],priority:0,orientation_forward:"SOUTH",INSERTION_MODE:"DEFAULT",inv:{item0:{},item2:{},item1:{},item8:{},item7:{},item4:{},item3:{},item6:{},item5:{}},proxy:{p:0,g:457L,k:-1L},ADVANCED_BLOCKING_MODE:"DEFAULT",id:"BlockInterface",pointAt:1,SMART_BLOCK:"NO",FUZZY_MODE:"IGNORE_ALL",INTERFACE_TERMINAL:"YES"}' />

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/cable_interface.snbt" />
</GameScene>
</Row>

<ItemLink id="appliedenergistics2:tile.BlockInterface" />s are the primary way in which your autocrafting system interacts with the world. They push the ingredients in
their [patterns](../items_blocks/patterns.md) to adjacent inventories, and items can be inserted into them in order to insert them into the network. Often
a channel can be saved by piping the output of a machine back into a nearby interface (often the one that pushed the ingredients)
instead of using an <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> to pull the output of the machine into the network.

Of note, since they push the ingredients directly from the [crafting storage](../items_blocks/crafting_cpu.md#crafting-storage) in a crafting CPU, they
never actually contain the ingredients in their inventory, so you cannot pipe out from them. You have to have the interface push
to another inventory (like a barrel) then pipe from that.

Also of note, the interface has to push ALL of the ingredients at once, it can't push half-batches. This is useful
to exploit.

ME Interfaces have a special interaction with interfaces on [subnets](subnetworks.md): if the interface is unmodified (nothing in the request slots)
the interface will skip the interface entirely and push directly to that subnet's [storage](../ae2_mechanics/import_export_storage.md),
skipping the interface and not filling it with recipe batches, and more importantly, not inserting the next batch until there's space in storage.

Multiple interfaces with identical patterns are supported and work in parallel.

ME Interfaces will attempt to round-robin their batches to all of their faces, thus using all attached machines in parallel.

## Variants

This branch does not have the normal, directional, and flat interface blocks found in newer AE2. Its interface block connects to the network and imports or exports from its faces; the flat interface is a cable subpart that allows compact placement and does not provide a network connection on its front face. Normal and flat interfaces can be converted in a crafting grid.

## Settings

ME Interfaces have a variety of modes:

*   **Blocking Mode** stops the interface from pushing a new batch of ingredients if there are already
    ingredients in the machine.
*   **Lock Crafting** can lock the interface under various redstone conditions, or until the result of the
    previous craft is inserted into that specific interface.
*   The interface can be shown or hidden on <ItemLink id="appliedenergistics2:item.ItemMultiPart:480" />s.

## Priority

Priorities can be set by clicking the wrench in the top-right of the GUI. In the case of several [patterns](../items_blocks/patterns.md)
for the same item, patterns in interface with higher priority will be used over patterns in interface with lower priority,
unless the network does not have the ingredients for the higher priority pattern.

# Molecular Assemblers

<BlockImage id="appliedenergistics2:tile.BlockMolecularAssembler" scale="4" />

The <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> takes items input into it and carries out the operation defined by an adjacent <ItemLink id="appliedenergistics2:tile.BlockInterface" />,
or the inserted <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" />,
then pushes the result to adjacent inventories.

Their main use is next to a <ItemLink id="appliedenergistics2:tile.BlockInterface" />. ME Interfaces have special behavior in this case,
and will send information about the relevant pattern along with the ingredients to adjacent assemblers. Since assemblers auto-eject the results of
crafts to adjacent inventories (and thus into the return slots of the interface), an assembler on a interface
is all that is needed to automate crafting patterns.

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
