---
item_ids:
  - gregtech:gt.blockmachines:15563
navigation:
  title: 전기식 내파 압축기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15563
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 전기식 내파 압축기
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15563"/>
</GameScene>
<Color id="GREEN">전기식 내파 압축기(EIC)</Color>는 전기를 사용해 플레이트와 분진을 압축하는 UHV 티어 멀티블록입니다. <Color id="GREEN">EIC</Color>는 폭발물을 소모하지 않고, 레시피 소요 시간을 1초에서 1틱으로 줄이며, 최대 256 병렬 처리를 제공하기 때문에 내파 압축기 <ItemImage id="gregtech:gt.blockmachines:1001"/> 및 밀도^2 <ItemImage id="gregtech:gt.blockmachines:15547"/>의 직접적인 상위 버전입니다. <Color id="GREEN">EIC</Color>는 또한 자기유체역학적으로 구속된 항성 물질(MHDCSM) 부품을 제작할 수 있는 유일한 기계이므로 UXV로 진행하는 데 필수적이지만, 가능한 한 빨리 건설하는 것을 강력히 권장합니다.

<br clear="all"/>

> [!NOTE]
> 다음 변경 사항이 멀티블록에 적용되었습니다(구조 제외):
> - 유리: 이제 구조에 유리가 포함되므로, 유리도 또 하나의 티어 구성 요소입니다. UMV 유리는 제한을 제거합니다.

## 건설
<Color id="GREEN">EIC</Color>에는 두 가지 티어 구성 요소가 있습니다. 구속 블록은 병렬 처리 수를 결정하고, 유리는 에너지 해치의 최대 티어를 결정합니다. UMV 티어 유리는 모든 제한을 제거합니다. 버스/해치는 구조 어디에서나 나콰다 강화 블록을 대체할 수 있습니다. 본격적인 오버클럭킹을 위해 <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>를 지원하지만, <Color id="GREEN">EIC</Color>는 한 티어만 건너뛸 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용해 하위 채널 "piston_block"과 "glass"로 각각 구속 블록과 유리의 티어를 지정하여 구조를 시각화/건설하십시오.

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15563"/><ItemImage id="gregtech:gt.blockmachines:15563"/>
- 230-247 <ItemLink id="gregtech:gt.blockreinforced:10"/><ItemImage id="gregtech:gt.blockreinforced:10"/>
- 36 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 24 구속 블록(티어형) <ItemImage id="gregtech:gt.blockmetal5:2"/>
- 22 티어형 유리 <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 10 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 2 <ItemLink id="gregtech:gt.blockframes:324"/><ItemImage id="gregtech:gt.blockframes:324"/>
- 1개 이상 에너지 해치(모든 강화 블록 가능) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1개 유지보수 해치(모든 강화 블록 가능) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0개 이상 입력 버스(모든 강화 블록 가능) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치(모든 강화 블록 가능) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스(모든 강화 블록 가능) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0개 이상 출력 해치(모든 강화 블록 가능) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">EIC</Color>는 케이싱과 버스/해치를 절약하기 위해 각 측면을 서로 벽 공유할 수 있습니다. 여기에는 구조의 왼쪽과 오른쪽에 있는 날개 세 층이 모두 포함됩니다. 구속 블록은 위치 제한 때문에 포함되지 않습니다.

## 사용법
대부분의 <Color id="GREEN">EIC</Color> 레시피는 UEV 전압으로 책정되며 길이는 단 1틱입니다. 즉, <Color id="GREEN">EIC</Color>는 폭발물을 전혀 사용하지 않으면서도 믿을 수 없을 만큼 빠르고 놀랍도록 에너지 효율적입니다. 더 높은 티어는 다음 표에서 볼 수 있듯 상당한 수의 병렬 처리를 추가합니다.

| 티어 | 구속 블록 | 병렬 처리 |
| --------------- | --------------- | --------------- |
| 1 | 뉴트로늄 블록 | 1 |
| 2 | 인피니티 블록 | 4 |
| 3 | 초월 금속 블록 | 16 |
| 4 | 시공간 블록 | 64 |
| 5 | 유니버시움 블록 | 256 |

하지만 <Color id="GREEN">EIC</Color>는 한 티어만 건너뛸 수 있습니다. 예를 들어 레시피가 MAX 전압으로 책정되어 있다면, <Color id="GREEN">EIC</Color>는 이를 실행하기 위해 최소 4A UXV 에너지 해치가 필요합니다. 아무리 많은 UMV 앰프도 결코 충분하지 않습니다. 이 제한은 이터니티 나나이트로 용융 MHDCSM을 제작하려 할 때 가장 분명하게 드러납니다.
<RecipeFor id="gregtech:gt.metaitem.99:583" input="gregtech:gt.metaitem.03:4141"/>