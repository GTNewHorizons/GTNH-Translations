---
navigation:
  title: 작물 교배
  parent: crops.md
  icon: cropsnh:genericSeed
categories:
    - crops
author: Skorched
date: 2026-05-20
---

# 작물 교배
바닐라 씨앗을 작물 막대기에 심는 것만으로 만들 수 있는 씨앗은 그리 많지 않습니다. 다른 씨앗을 생성하는 주요 방법은 세 가지가 있으며, 이번 부분에서 다룹니다. "월드 내"에서 일어나는 교배 방법의 경우, 작물이 [확산](spreading.md)하거나 교배될 확률이 50/50입니다(유효한 교배 설정이라고 가정할 때).

## 확정 교배
<FloatingImage src="../assets/crops/determine.png" displayWidth="128" wrap="square" align="left">
  <ImageAnnotation>
    확정 교배의 예시
  </ImageAnnotation>
</FloatingImage>
확정 교배는 목표 씨앗에 일종의 "레시피"가 있는 교배입니다. 이 경우에는 레시피에 요구되는 대로 성숙한 식물 두 개를 배치하고, 중앙에 목표 작물에 유효한 재배 조건을 갖춘 이중 작물 막대기를 놓으면 됩니다. 유효한 확정 교배 사례가 있다면, 새 식물은 항상 두 부모 중 하나에서 확산된 작물이거나 목표 작물입니다. 풀 변이는 발생하지 않습니다.
<br clear="all">

## 풀 교배
<FloatingImage src="../assets/crops/pools.png" displayWidth="128" wrap="square" align="left">
  <ImageAnnotation>
    작물 변이 풀의 예시
  </ImageAnnotation>
</FloatingImage>

대부분의 작물에서 기본 씨앗을 교배하는 것은 <Color id="GREEN">풀 교배</Color>를 통해 이루어집니다. 스캔한 작물의 사용처를 검색하면 여기에 표시된 페이지를 찾을 수 있으며, 이 페이지에는 해당 씨앗이 속한 모든 "풀"이 표시됩니다. 이 방식으로 목표 작물을 생성하려면 목표 작물과 같은 풀에 속한 성숙한 부모 두 개를 양쪽에 두고, 확정 교배와 동일한 기본 설정 단계를 따라야 합니다. 이는 흔히 훨씬 덜 "정확한" 방법입니다. 올바른 계획 없이는 "출력" 작물의 유효 풀이 원하는 작물 하나보다 더 커지기 때문입니다.
<br clear="all">

## 작물 교배기
더 고급 작물의 경우에는 <Color id="BLUE">작물 교배기</Color> <ItemImage id="gregtech:gt.blockmachines:28025" />를 사용해야 합니다. 이 기계는 출력이 완전히 확정적이지만, 사용한 기계의 전압 티어에 따라 출력을 소멸시킬 확률이 있습니다. LV에서는 성공률 40%부터 시작하며, ZPM+에서는 100%입니다.

작물 교배기의 모든 레시피는 일련의 입력(흔히 씨앗 두 개지만 더 많을 수 있습니다)과 일정량의 <Color id="GREEN">농축 비료</Color>를 필요로 합니다. 이 레시피는 출력 씨앗의 티어와 스탯 모두에 따라 달라지므로 다소 오해의 소지가 있을 수 있습니다.

예를 들어, <Color id="RED">보크시아 씨앗</Color>을 생산하려고 한다고 가정해 보겠습니다. NEI에 표시된 레시피는 갈바니아 씨앗 + 니켈백 씨앗 + 보크사이트 광석 + <Color id="GREEN">7560L 농축 비료</Color>입니다.

실제 비료량은 아래와 같이 입력의 스탯에 따라 크게 달라질 수 있습니다:
- 1/1/1 입력: <Latex formula="\text{Fertilizer} = 6 \times 144 + (1 + 1 + 1) \times 72 = 1080L" />
- 31/31/31 입력: <Latex formula="\text{Fertilizer} = 6 \times 144 + (31 + 31 + 31) \times 72 = 7560L" />

예를 들어 MV 작물 교배기는 입력 유체 슬롯에 6,400L만 저장할 수 있다는 점을 고려하면 이는 특히 중요합니다.

따라서 이 특정 목적을 위해 씨앗의 스탯을 "하향"할 필요가 있을 수 있습니다.