---
navigation:
  title: Shared Prospecting
  parent: qol.md
  icon: gregtech:gt.detrav.metatool.01:100
categories:
    - Quality Of Life
author: Skorched
date: 2026-05-16
---

# Shared Prospecting
Visual Prospecting has received a huge quality of life improvement by overhauling how it works in multiplayer. New prospects found will instantly now be shared to all members of a same team ([GTNH Team](../misc/gtnh_teams.md)to be specific)! Those players who have used <Color id="RED">Shared Prospecting</Color> in the past, the functionality is effectively the same, but working and optimised.

Additionally, underground fluid prospecting has been made easier to distinguish by adding colored overlays to each fluid, using the same colors as is found in the higher tier prospector's tools!

As part of this overhaul,

| Command | Permission Level | Effect |
| --------------- | --------------- | --------------- |
| `/vp_client_cache_reset` | - | Resets the clientside cache of prospects |
| `/vp team info [detailed]` | 0 | Shows info regarding your team |
| `/vp_team_info <player> [detailed]` | 2 | Shows info regarding a target player's team |
| `vp_admin team upload <player>` | 2 | Uploads the prospects of one players cache to the team |
| `/vp_admin team clear` | 2 | Clears the team prospects |
| `/vp_admin servercache rebuild all` | 4 | Rebuilds the cache to the server |
| `/vp_admin servercache rebuild spawn` | 4 | Rebuilds the cache to the server for the spawn chunks |

