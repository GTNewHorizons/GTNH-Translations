---
navigation:
  title: Botania NEI 핸들러 정리
  parent: magic_nei.md
  icon: Botania:lexicon
categories:
    - 마법 NEI
author: koolkrafter5
date: 2026-06-10
---

이번 업데이트에서는 Botania의 다양한 NEI 핸들러가 개선되었습니다:
- 이제 사전 항목은 아이템의 용도뿐만 아니라 레시피를 찾을 때도 표시됩니다.
- 떠다니는 꽃 핸들러는 이제 NEI의 오버레이 버튼을 사용해 아이템을 인벤토리/제작대 그리드로 이동할 수 있습니다.
- 이제 마나 주입, 꽃잎 약제대, 룬 제단 핸들러의 모든 레시피를 실제로 볼 수 있습니다. 예전에는 클릭할 영역을 가로막는 아이템들이 있어서 해당 아이템의 레시피만 볼 수 있었습니다. 이제는 클릭 가능한 영역이 만들어지기 전에 렌더링됩니다.
- 마나 풀(및 그 촉매)과 꽃잎 약제대 같은 제작 설비는 더 이상 북마크/패턴화된 레시피의 재료에 추가되지 않습니다.
- 식물 양조기 핸들러는 왼쪽에 양조를 촉매로 적용할 수 있는 모든 아이템을 포함합니다.
- 꽃잎 약제대와 룬 제단 레시피는 이제 각각 재료에 "아무 씨앗"과 생명의 돌을 포함합니다.

&lt;Recipe id="minecraft:redstone" handlerId="botania.manaPool"/&gt;
&lt;Recipe id="Botania:rune:1" handlerId="botania.runicAltar"/&gt;