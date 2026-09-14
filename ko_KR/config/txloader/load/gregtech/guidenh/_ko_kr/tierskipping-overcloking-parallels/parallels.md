---
navigation:
  title: "병렬 처리"
  icon: gregtech:gt.blockmachines:31041
  parent: T-O-P-index.md
  position: -3
---

# 병렬 처리


**병렬 처리**는 멀티블록 기계가 동일한 레시피를 같은 시간 간격에 여러 개 처리할 수 있는 기능입니다. 단일 블록 기계에는 이 기능이 없습니다.

기계가 병렬 처리로 작동하면 전력 소모량은 (실제 병렬 수 x 실제 레시피 전력)이 되며, 모든 입력 소비량과 출력 생산량은 실제 병렬 수만큼 증가하고 레시피 시간은 변하지 않습니다.

병렬 처리가 적용된 후 멀티블록은 [정격 전력](T-O-P-index.md#rated-power)이 여전히 충분하다고 가정하고 **[오버클록](overclocking.md)**을 계산하여 시도합니다. 병렬 처리와 배치 모드는 완전히 별개의 기능입니다.

# 최대 병렬 수

멀티블록에는 병렬 설정 창이 있으며, 최대 병렬 수를 수동으로 낮출 수 있습니다.

- 특별한 설명이 없는 기계는 기본적으로 병렬 수가 1이며, 예시는 <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" />입니다.
- <ItemLink id="gregtech:gt.blockmachines:12730" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:12731" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:12738" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:13366" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:13367" showIcon="left" /> 및 <ItemLink id="gregtech:gt.blockmachines:31150" showIcon="left" />은 최대 병렬 수가 256으로 고정되어 있습니다.
- 대부분의 기계는 전압 또는 구조 부품의 티어를 기준으로 최대 병렬 수를 계산합니다. 툴팁에 "각 전압 티어가 $$x$$개의 병렬 처리를 제공합니다"라고 표시되는 경우, 모든 에너지 해치의 전압 입력 합계를 기준으로 계산하며 최대 15(MAX+)로 제한됩니다.

< ItemLink id="gregtech:gt.blockmachines:1003" showIcon="left" />과 <ItemLink id="gregtech:gt.blockmachines:1132" showIcon="left" />만 레시피 간 병렬 처리를 지원하므로, 하나의 병렬 처리 묶음에 서로 다른 여러 레시피가 포함될 수 있습니다.

실제로 실제 병렬 수의 병목은 대개 기계의 최대 병렬 수 제한입니다.

# 1틱 도달 후 오버클록(1tOC)

오버클록으로 인해 실제 레시피 시간이 1틱 미만으로 줄어들 경우, 레시피 시간이 1틱으로 고정되고 초과 오버클록이 추가 병렬 배율로 변환됩니다. 이를 **1tOC**라고 합니다.

$$\text{1tOC 보정 계수} = \left\lceil\frac{1 \text{ 틱}}{\text{실제 시간(부동 소수점)}}\right\rceil$$

이 보정 계수에 해당하는 배율만큼 기계의 최대 병렬 수가 증가합니다. 결과는 올림 처리되므로 항상 플레이어에게 유리합니다.

1tOC를 지원하지 않는 기계:
- 모든 단일 블록 기계
- <ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:15410" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:5001" showIcon="left" />

# 병렬 처리와 완벽한 오버클록의 동등성

**[병렬 처리](parallels.md)**는 완벽한 오버클록과 동등한 것으로 취급할 수 있습니다. 최대 $$n$$개의 병렬 처리가 가능한 기계는 불완전한 오버클록을 완벽한 오버클록으로 변환할 기회를 사실상 $$\log_4{n}$$번 가지며, 그 결과 $$\sqrt{n}$$배 빠르게 작동합니다.