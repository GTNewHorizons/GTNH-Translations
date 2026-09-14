---
item_ids:
  - appliedenergistics2:tile.BlockSpatialPylon
navigation:
  title: 공간 IO 변경 사항
  parent: ae2.md
  icon: appliedenergistics2:tile.BlockSpatialPylon
categories:
    - Applied Energistics 2
author: Skorched
date: 2026-05-27
---

# 공간 IO 변경 사항
공간 IO 시스템에 몇 가지 개선 사항이 있습니다! 변경 사항은 아래에서 확인할 수 있습니다:
- __공간 링크 챔버__: 공간 셀 <ItemImage id="appliedenergistics2:item.ItemSpatialStorageCell.16Cubed"/>을 중첩할 수 있으며, ME 네트워크를 해당 포켓 차원에 연결할 수 있습니다!
- __공간 네트워크 릴레이__: 공간 셀 차원에 배치하면, 이 특정 셀이 내부에 있는 링크 챔버에 연결됩니다
- __새로운 제작법__: 공간 부품의 새로운 제작법이 추가되어, 조립기에서 제작할 때 더 저렴해지고 재귀 제작이 필요하지 않습니다!
- __매트릭스 블록__: 포켓 차원의 경계를 구성하는 매트릭스 블록을 이제 상호작용할 수 있으며, 셀이 공간 링크 챔버 안에 있는 한 우클릭으로 포켓 차원에서 나갈 수 있습니다!

> [!NOTE]
> 공간 링크 챔버는 자체 용도로 1채널을 사용하며, 포켓 차원 내부에서 31채널을 전송할 수 있습니다


> [!WARNING]
> 이것은 기계의 다차원 전송을 __절대__ 수정하지 않습니다. 공간 시스템으로 기계나 타일 엔티티를 차원 간에 이동시키려고 하면, 반드시 손상됩니다!