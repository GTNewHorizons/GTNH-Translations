---
navigation:
  title: 물질 조작기 개선 사항
  parent: qol.md
  icon: matter-manipulator:itemMatterManipulator3
categories:
    - 편의성
author: Skorched
date: 2026-05-16
---

# 물질 조작기 개선 사항
<Color id="GREEN">물질 조작기</Color> <ItemImage id="matter-manipulator:itemMatterManipulator3" />가 작동하는 방식에 몇 가지 좋은 변경 사항이 적용되었습니다! 아래에 설명합니다.

# 고급 복사 옵션 (스마트 복사)
복사/붙여넣기 방사형 메뉴에 이제 세 가지 새로운 토글이 있는 <Color id="BLUE">__고급 옵션__</Color> 하위 메뉴가 제공됩니다:
- __외부 허브에 연결 (MKII+)__: 복사되는 영역 _바깥_의 허브에 연결된 무선 커넥터를 복사할 때, 붙여넣은 커넥터는 해당 허브에 계속 연결된 상태로 유지됩니다!
- __자동 P2P 인터페이스 (MKII+)__: ME 인터페이스를 P2P ME 인터페이스 터널로 대체합니다. 원본은 "입력측" 터널을 받고, 붙여넣은 버전은 "출력측" 터널을 받으며, 주파수는 자동으로 일치합니다. 패턴은 원본에 남으므로, 모두 그 단일 패턴 세트로 라우팅되는 처리 설비를 복제할 수 있습니다! (유체 P2P 인터페이스 터널에서도 작동합니다)
- __조합 입력 버스 자동 프록시 (MKIII)__: 복사된 구조물의 <Color id="RED">조합 입력 버스</Color>를 원래 버스에 다시 연결된 <Color id="BLUE">조합 입력 프록시</Color>로 대체합니다! 다시 말해 연결은 자동입니다!

<FloatingImage src="../assets/qol/mm_smart.png" wrap="square" align="left" displayWidth="256">
  <ImageAnnotation>
    새로운 스마트 복사 메뉴
  </ImageAnnotation>
</FloatingImage>
<br clear="all"/>
# 장식 블록 지원
Carpenter's Blocks, Project Red 또는 Forge Microblocks에 푹 빠진 분들을 위해, <Color id="GREEN">물질 조작기</Color>가 이제 이를 완전히 지원합니다!

이 블록들을 복사하고 붙여넣는 일은 역사적으로 제대로 구현하기 불가능했지만, 이제는 방향을 저장할 뿐만 아니라 장식용 커버도 보존합니다!

## OpenComputers 케이블 지원
케이블 모드가 이제 OpenComputers 케이블과 함께 작동합니다. 케이블을 마우스 오른쪽 버튼으로 클릭해 선택한 다음, GregTech/Applied Energistics 케이블에서처럼 선을 그리기 시작하십시오!