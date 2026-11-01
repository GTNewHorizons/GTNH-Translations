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
바닐라 씨앗을 작물 막대에 심기만 해서 얻을 수 있는 씨앗에는 한계가 있습니다. 다른 씨앗을 얻는 방법은 크게 세 가지이며, 이 절에서 다룹니다. "인게임"에서 이루어지는 교배 방식에서는 작물이 [퍼지거나](spreading.md) 교배될 확률이 각각 50%입니다(올바른 교배 환경을 갖춘 경우).

## 결정론적 교배
<FloatingImage src="../assets/crops/determine.png" displayWidth="128" wrap="square" align="left">
  <ImageAnnotation>
    결정론적 교배의 예시
  </ImageAnnotation>
</FloatingImage>
결정론적 교배는 대상 씨앗에 일종의 "조합법"이 있는 경우를 말합니다. 이 경우 조합법에 필요한 성숙한 식물 두 개를 배치하고, 가운데에 작물 막대를 두 개 겹쳐 설치한 뒤 대상 작물에 필요한 재배 조건을 갖추기만 하면 됩니다. 유효한 결정론적 교배 조합이라면 새 식물은 항상 부모 중 한쪽에서 퍼진 작물이거나 대상 작물입니다. 풀 돌연변이는 발생하지 않습니다.
<br clear="all">

## 풀 교배
<FloatingImage src="../assets/crops/pools.png" displayWidth="128" wrap="square" align="left">
  <ImageAnnotation>
    작물 돌연변이 풀의 예시
  </ImageAnnotation>
</FloatingImage>

대부분의 작물에서 기본 씨앗은 <Color id="GREEN">풀 교배</Color>를 통해 얻습니다. 스캔한 작물의 용도를 검색하면 여기에 표시된 페이지를 찾을 수 있으며, 해당 씨앗이 속한 모든 "풀"을 확인할 수 있습니다. 이 방법으로 대상 작물을 얻으려면 대상 작물과 같은 풀에 속한 성숙한 부모 식물 두 개를 양쪽에 배치하고, 결정론적 교배와 동일한 기본 설치 단계를 따라야 합니다. 올바르게 계획하지 않으면 유효한 "결과" 작물 풀이 원하는 작물뿐 아니라 더 많은 작물을 포함할 수 있으므로, 이 방법은 원하는 작물을 얻는 데 정확도가 훨씬 낮을 수 있습니다.
<br clear="all">

## 작물 교배기
더 고급 작물을 얻으려면 <Color id="BLUE">작물 교배기</Color> <ItemImage id="gregtech:gt.blockmachines:28025" />를 사용해야 합니다. 이 기계의 결과물은 완전히 결정론적이지만, 사용하는 기계의 전압 티어에 따라 결과물이 소멸할 확률이 있습니다. LV에서는 성공률이 40%이며, ZPM 이상에서는 100%입니다.

작물 교배기의 모든 조합법에는 몇 가지 입력 재료(대개 씨앗 두 개지만 더 많을 수도 있습니다)와 일정량의 <Color id="GREEN">농축 비료</Color>가 필요합니다. 조합법에 표시된 양은 티어와 결과 씨앗의 능력치에 따라 달라지므로 다소 오해를 부를 수 있습니다.

예를 들어 <Color id="RED">보크시아 씨앗</Color>을 생산한다고 가정해 보겠습니다. NEI에 표시된 조합법은 갈바니아 씨앗 + 니켈백 씨앗 + 보크사이트 광석 + <Color id="GREEN">7560L 농축 비료</Color>입니다.

실제 비료 필요량은 아래와 같이 입력 씨앗의 능력치에 따라 크게 달라질 수 있습니다.
- 1/1/1 입력: <Latex formula="\text{Fertilizer} = 6 \times 144 + (1 + 1 + 1) \times 72 = 1080L" />
- 31/31/31 입력: <Latex formula="\text{Fertilizer} = 6 \times 144 + (31 + 31 + 31) \times 72 = 7560L" />

예를 들어 MV 작물 교배기의 입력 유체 슬롯에는 6,400L만 저장할 수 있다는 점을 고려하면 이는 특히 중요합니다.

따라서 이 용도로 씨앗의 능력치를 낮춰야 할 수도 있습니다.