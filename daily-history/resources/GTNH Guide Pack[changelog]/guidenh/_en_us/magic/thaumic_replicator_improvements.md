---
navigation:
  title: Thaumic Replicator Improvements
  parent: magic.md
  icon: ThaumicExploration:replicator
categories:
    - Magic Changes
author: koolkrafter5
date: 2026-06-09
---

The <ItemLink id="ThaumicExploration:replicator"/> <ItemImage id="ThaumicExploration:replicator"/> has received a large number of improvements:
- It now <Color id="GREEN">remembers</Color> the jars it is pulling essentia from. It will now only search for new jars when the current one it is pulling that aspect from is <Color id="RED">empty</Color>, resulting in a lot less lag.
- The glyphs on its sides are now <Color id="GREEN">pixel-accurate</Color> and <Color id="GREEN">glow in the dark</Color>.
- Some side glyphs will no longer be empty for blocks with fewer than 4 essentia types by rendering the same aspect on multiple sides.
- It now shows the essentia bubble effect when working, like infusion.
- An empty hand is now required to clear the template to prevent accidentally voiding crafts.
- It can now replicate a few <Color id="GREEN">new types of blocks</Color> like stained glass, stained hardened clay, and netherrack.
- The block above the replicator can now be any block that is <Color id="GREEN">fully transparent</Color> (like glass) if you want to make a fancy display case.
- It has been given a [new NEI handler](magic_nei/thaumic_replicator_nei.md).
- Many bugs and crashes have been fixed.