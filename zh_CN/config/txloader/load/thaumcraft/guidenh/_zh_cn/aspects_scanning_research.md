---
item_ids:
  - Thaumcraft:ItemThaumometer
  - Thaumcraft:ItemInkwell
  - Thaumcraft:ItemResource:9
navigation:
  title: Aspects, Scanning and Research
  parent: ./index.md
  icon: 'Thaumcraft:ItemResearchNotes'
  position: 80
---

# Aspects, Scanning and Research

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

Research in Thaumcraft begins with understanding the world. Scanning reveals the <Color color="#B7A0D6">Aspects</Color> contained in items, creatures, and nodes, granting Research Points and clues;<br>the Research Table then uses these discoveries to combine Aspects and work on Research Notes, ultimately turning them into knowledge in the Thaumonomicon.

The most easily confused parts of research are **discovering Aspects, gaining Research Points, and completing research**. This page explains these requirements and the scanning and research conveniences provided by NH.

## The Aspect System and Composition

**Aspects** describe both the magical properties of objects and the categories used in research. The six Primal Aspects form the foundation of the entire system, while each Compound Aspect consists of two Aspects;<br>these component Aspects can themselves be Compound Aspects, creating a network of relationships that unfolds in layers.

The six Primal Aspects are <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air (Aer), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Earth (Terra), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Fire (Ignis), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Water (Aqua), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Order (Ordo), and <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" />Entropy (Perditio).

| Compound Aspect | Component Aspects |
| --- | --- |
| <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"lux"}' scale="0.75" />Light (Lux) | <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air + <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Fire |
| <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"motus"}' scale="0.75" />Motion (Motus) | <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air + <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Order |
| <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"victus"}' scale="0.75" />Life (Victus) | <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Earth + <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Water |

**An Aspect's composition and an item's Aspect content are two different kinds of information.** "Life consists of Earth and Water" describes a relationship used in research; "an item contains Life" describes that item's properties. The latter affects scanning rewards and the choice of materials for Essentia production, but does not mean that the Research Table directly consumes the item to produce Research Points.

Likewise, combining Earth and Water at the Research Table produces Life Research Points, while processing an item containing Life in an Alchemical Furnace produces Life Essentia. Both use the same Aspect icon, but the resources are stored in different places and serve different purposes.

NH's addons also introduce Aspects. When discovering a new Aspect, consider its name, composition, and actual sources; the Aspect count listed on the original mod's wiki should not be treated as the total for the current modpack.

## What Scanning Provides

<ItemLink id="Thaumcraft:ItemThaumometer" showIcon="left" /> is used to observe the magical properties of items, blocks, creatures, and Aura Nodes. Scanning provides three main types of rewards:

|  |  |
| --- | --- |
| Discovering an object's Aspects | Reveals the Aspects and quantities contained in the object, and may uncover previously unknown Aspects |
| Research Points | Recorded for the player by Aspect, ready to be spent at the Research Table |
| Research clues | Certain specific objects can reveal hidden research, expanding the research available in the Thaumonomicon |

These three rewards are not identical. Scanning a new item whose Aspects you already know can still replenish Research Points; scanning a specific object for hidden research focuses on research clues.

**Scanning does not consume the observed item or break it down into Essentia.** Scanning ordinary items and processing materials in an Alchemical Furnace are ways of acquiring knowledge and producing magical resources, respectively.

Scan records and Research Points are part of the player's research data. Once a type of object has been scanned, repeatedly scanning it cannot provide an unlimited supply of points.

## World, Inventory, and Container Scanning

Blocks, dropped items, and creatures in the world can be observed while holding a Thaumometer. NH also provides inventory and container scanning to make acquiring Research Points more convenient.

 - World scanning | Aim the Thaumometer at a valid object in the world and keep observing it
 - Inventory scanning | Hold the Thaumometer on the cursor and hover over an item slot in an inventory or container
 - Container scanning | Use the Thaumometer on a container after completing the container scanning research

The container scanning research is in the Basic Information category of the Thaumonomicon and requires the Deconstruction Table research; the container scanning research itself must also be completed.<br>
The NH quest "Scanning Made Easy" introduces these two conveniences. Container scanning uses sneak and right-click; scanning the chest block itself and scanning the items inside it should also be understood separately.<br>

Inventory scanning does not work with every slot in every interface. For example, in AE2, scanning storage cells requires another item: <ItemLink id="thaumicenergistics:cell.microscope" showIcon="left" />

## Unknown Aspects and Scanning Requirements

When the Thaumometer says that you cannot understand something, a common reason is that the object contains a Compound Aspect you have not yet discovered.<br>You need to know that Aspect, or both of its component Aspects, to understand the relevant object.<br>Complex objects may involve several Compound Aspects at once, so whether a scan succeeds depends on which Aspects have been discovered.

Combining Aspects at the Research Table is another way to discover new Compound Aspects. A correct combination lets the player discover the new Aspect and gain some Research Points; this also expands the range of objects they can understand and scan.

> [!NOTE]
> Not every pair of Aspects forms a valid combination. Attempting an invalid combination also consumes Research Points, so consult known information about Aspect relationships first to avoid wasting research resources on repeated guesses.

The order in which you scan objects therefore affects your progress. The quest "Just Tell Me What to Scan Already!" provides a set of objects to scan as a reference.

## Item Aspects and NEI Lookups

The Aspects and quantities of scanned items can be viewed in their tooltips. By default, hold the sneak key (usually Shift) to display this information.<br>Unknown icons, discovered Aspects, and specific quantities indicate different discovery states and Aspect amounts.

In GTNH, NEI can display the Aspects of scanned items, Aspect combinations, items containing a particular Aspect, and Arcane, Alchemy, and Infusion recipe lookups. This is useful for finding sources for mass Essentia production.

## Sources and Uses of Research Points

<Color color="#B7A0D6">Research Points</Color> are recorded separately for each Aspect. The numbers at the Research Table show the research resources available to the player.<br>Even if a Compound Aspect has already been discovered, it cannot be placed to form connections once its Research Points have run out.

| Source | What It Provides | Limits and Characteristics |
| --- | --- | --- |
| Scanning a new valid object | Research Points for the Aspects contained in the object; discovering an Aspect for the first time grants additional rewards | A type of object that has already been scanned cannot repeatedly provide points |
| Combining Aspects at the Research Table | Research Points for the corresponding Compound Aspect | Consumes Research Points from both component Aspects; it does not generate resources for free |
| Knowledge Fragments | Adds 1–2 points to each Primal Aspect when used | Difficult to obtain and consumed on use |
| Deconstruction Table | Consumes items in an attempt to obtain Primal Aspect Research Points | Compound Aspects are broken down; output is slow and has a low chance of success |
| Environmental bonuses at the Research Table | Small amounts of bonus Research Points generated by the surroundings | Acquired slowly and cannot replace a steady source of Research Points |

**Knowledge Fragments** can both replenish basic research resources and help discover lost knowledge. These two uses should be understood separately; when seeking special research, consult the Knowledge Fragments entry in the Thaumonomicon.

By default, NH applies a soft cap to Research Points gained from scanning: once the player has 500 Research Points in an Aspect, further scanning yields fewer points for that Aspect.

Research Points are mainly used to place Aspects in notes, combine Compound Aspects, and duplicate research. When using many Compound Aspects, also watch the reserves of their component Aspects to avoid ending up with only one type of Research Point while being unable to replenish the others you need.

## The Research Table, Research Notes, and Scribing Tools

<ItemLink id="Thaumcraft:ItemThaumonomicon" showIcon="left" /> shows the available research paths, the Research Table handles notes and Aspects, and <ItemLink id="Thaumcraft:ItemInkwell" showIcon="left" /> supplies the pen and ink needed for writing.

| Content | Purpose |
| --- | --- |
| Research entries in the Thaumonomicon | View prerequisites, obtain notes for available research, and read unlocked knowledge |
| Unfinished Research Notes | Record the subject of a research project and the Aspects that must be connected |
| Research Table | Combine Aspects, work on notes, and use unlocked research assistance features |
| Scribing Tools | Used to obtain notes and write at the Research Table; ink is consumed |
| Completed research | Reading it adds the corresponding research to the player's knowledge progress |

Both obtaining Research Notes and writing at the Research Table require Scribing Tools. Making two sets is recommended, one for obtaining notes and one for connecting Aspects.<br>
**GTNH locks research to the Hard setting, so ordinary research entries also require notes to complete.**

Thaumcraft Research Tweaks changes the Research Table interface. Aspects can be combined by dragging and dropping, or by using right-click while dragging; the corresponding methods are also used to write Aspects into slots on the notes.<br>
The research instructions in the Thaumonomicon have been updated to cover these interface features. Refer to the current interface when reading them.

## Connection Rules for Research Notes

Notes use a hexagonal grid to represent relationships between Aspects. To complete them, connect all the given Aspects into a single connected whole using valid connections.

A Compound Aspect can connect to its component Aspects, and a component Aspect can also connect to Compound Aspects that contain it. Similar names, similar icon colors, or both tracing back to a Primal Aspect do not automatically create a direct connection.

For example, Earth and Water have no direct relationship simply because they are both basic Aspects, but Life consists of Earth and Water, so "Earth—Life—Water" represents two valid relationships.<br>Another example is Light and Motion, both of which include Air in their composition; "Light—Air—Motion" connects them through their shared component Aspect.

Both composition and position requirements must be met: only adjacent Aspects with a valid relationship can connect to each other.

Placing an Aspect consumes its corresponding Research Points, while writing and making changes also consume ink. Normally, removing a misplaced Aspect does not refund Research Points; Research Expertise and Research Mastery provide a chance to recover them.

Once all parts of the notes are connected, they become completed research. **After completing the connections, you must read the result to unlock the corresponding research.**

## Research Prerequisites and Hidden Knowledge

Connections in the Thaumonomicon show prerequisite relationships between research entries, but a single connection does not necessarily display every requirement.<br>
Some content also requires specific scans, earlier discoveries, Warp-related events, or research progress in other mods.

> [!WARNING]
> Reading research marked as <Color color="#D5B77A">Forbidden Knowledge</Color> adds Warp. The danger level indicates the type and amount of Warp added.

## <ItemLink id="gregtech:gt.blockmachines:13001" showIcon="left" />

**<ItemLink id="gregtech:gt.blockmachines:13001" showIcon="left" />** provides another way to complete Research Notes, allowing a machine to handle the manual work of connecting Aspects.<br>
It is a facility that brings technology and magic together, requiring the corresponding research and materials.<br>
The machine consumes EU and uses the nodes in its structure to complete the Research Notes supplied to it.

> [!WARNING]
> The Research Completer consumes the nodes used for processing.

Research assistance facilities reduce repetitive work, but each has its own costs and requirements.

## Common Questions

| Symptom | What to Check |
| --- | --- |
| The Thaumometer cannot understand an object | Check which of its Aspects have been discovered, especially unknown Compound Aspects and their components |
| Repeatedly scanning the same type of item provides no new points | That type of object may already have been scanned; increasing the number of identical items does not create a new discovery |
| A new scan yields fewer points than the item's Aspect quantities | A high reserve of Research Points in an Aspect triggers the soft cap on scanning rewards |
| Inventory scanning does not respond | Make sure the Thaumometer is held on the cursor, that you hover long enough, and that the target is an ordinary valid inventory slot |
| Individual items can be scanned, but an entire chest cannot | Check that the container scanning research is complete, and distinguish the chest block from the items inside it |
| An Aspect is known but cannot be placed in the notes | Check the remaining Research Points for that Aspect, the Scribing Tools, and the state of the target slot |
| Combining Aspects reduces Primal Research Points | Combining consumes the component Aspects; invalid combinations may also waste points |
| Adjacent icons do not connect | A direct composition relationship is required; names or icons alone are not enough to judge this |
| Research Notes are complete, but the Thaumonomicon entry remains locked | Check whether the completed research has been read |
| NEI does not show a source for an Aspect | Lookups are affected by scanning and discovery progress; the list does not represent every possible source |

</Column>
