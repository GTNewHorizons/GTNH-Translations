---
navigation:
  parent: /items_blocks_index.md
  title: Crafting CPU Multiblock (Storage, Coprocessor, Monitor, Unit)
  icon: appliedenergistics2:tile.BlockSingularityCraftingStorage
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockCraftingUnit
- appliedenergistics2:tile.BlockCraftingMonitor
- appliedenergistics2:tile.BlockCraftingUnit:1
- appliedenergistics2:tile.BlockCraftingUnit:2
- appliedenergistics2:tile.BlockCraftingUnit:3
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:0
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:1
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:2
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:3
- appliedenergistics2:tile.BlockCraftingStorage
- appliedenergistics2:tile.BlockCraftingStorage:1
- appliedenergistics2:tile.BlockCraftingStorage:2
- appliedenergistics2:tile.BlockCraftingStorage:3
- appliedenergistics2:tile.BlockAdvancedCraftingStorage
- appliedenergistics2:tile.BlockAdvancedCraftingStorage:1
- appliedenergistics2:tile.BlockAdvancedCraftingStorage:2
- appliedenergistics2:tile.BlockAdvancedCraftingStorage:3
- appliedenergistics2:tile.BlockSingularityCraftingStorage
---

# Crafting CPU

<GameScene width="350" height="220" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingUnit:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingMonitor" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingUnit:0" scale="4" />
</Row>

Crafting CPUs manage crafting requests and jobs. They store intermediate products while multi-step crafting jobs are in progress, and affect the maximum size of jobs and, to some degree, how quickly they complete. See [autocrafting](../ae2_mechanics/autocrafting.md) for more details.

Right-click a Crafting CPU to open the crafting status UI and check the progress of its active job.

## Settings

*   A Crafting CPU can accept requests from players only, automation only (such as an <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> with an <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />), or both.

## Construction

Crafting CPUs are multiblocks and must be solid rectangular prisms with no gaps. They are made from several components.

Each CPU must contain at least one Crafting Storage block; the smallest valid CPU is a single 1k Crafting Storage block.

# Crafting Unit

<BlockImage id="appliedenergistics2:tile.BlockCraftingUnit" scale="4" />

(Optional) Crafting Units fill space in a CPU so that it remains a solid rectangular prism when there are not enough other components. They are also an ingredient in the other components.

<RecipeFor id="appliedenergistics2:tile.BlockCraftingUnit" />

# Crafting Storage

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:0" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:2" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:3" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:0" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:2" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:3" scale="4" />
</Row>

(Required) Crafting Storage is available in all standard cell sizes: 1k, 4k, 16k, 64k, and 256k. It stores the ingredients and intermediate products of a crafting job, so jobs with more ingredients require larger or additional storage blocks.

<Column>
  <Row>
    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:0" />

    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:1" />

    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:2" />

    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:3" />
  </Row>

  <Row>
    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage" />

    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:1" />

    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:2" />

    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:3" />
  </Row>
</Column>

# Crafting Coprocessing Unit

<BlockImage id="appliedenergistics2:tile.BlockCraftingUnit:1" scale="4" />

(Optional) Crafting Coprocessing Units increase the CPU's operating rate, allowing the system to send ingredient batches from an <ItemLink id="appliedenergistics2:tile.BlockInterface" /> more frequently and keep up with fast machines. For example, when an interface surrounded by <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" />s can send batches faster than one assembler can process them, it distributes batches among the assemblers.

Some complex recipes have multiple steps that can run in parallel, such as making planks and books at the same time for bookshelves. In the crafting status UI, opened by right-clicking a CPU or using the hammer icon in a [terminal](terminals.md), these steps appear as “scheduled”. Each Coprocessing Unit allows one additional such step to run in parallel, where it appears as “crafting”. In practice, Coprocessing Units are usually added for batch insertion speed rather than for the number of parallel recipe steps.

<RecipeFor id="appliedenergistics2:tile.BlockCraftingUnit:1" />

# Crafting Monitor

<BlockImage id="appliedenergistics2:tile.BlockCraftingMonitor" scale="4" />

(Optional) A Crafting Monitor displays the job currently handled by its CPU. Its screen can be dyed with an <ItemLink id="appliedenergistics2:item.ToolColorApplicator" />.

<RecipeFor id="appliedenergistics2:tile.BlockCraftingMonitor" />
