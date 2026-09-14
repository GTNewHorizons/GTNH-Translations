---
navigation:
  title: Angelica 변경 사항
  parent: misc.md
  icon: eternalsingularity:combined_singularity:14
categories:
    - 기타 변경 사항
author: Skorched
date: 2026-05-30
---

# Angelica 변경 사항
모르시는 분들을 위해 말씀드리면, <Color id="GREEN">Angelica</Color>는 GTNH의 Optifine 대체 모드로, 전반적인 렌더링을 개선하고 셰이더에 대한 내장 호환성을 제공합니다!

이 모드는 새로운 모드가 아니지만, 2.9를 위한 몇 가지 변경 사항이 있습니다! 여기에는 렌더링을 전반적으로 최적화하려는 막대한 노력이나 버그 수정은 포함되지 않습니다.

## 간소화 CTM
이 항목은 텍스처 개발자들을 위한 것입니다! 알고 계실 수도 있고 아닐 수도 있지만, 예전에는 유리를 예쁘게 보이게 만드는 데만 <Color id="RED">47</Color>개의 고유 텍스처가 필요했습니다! Angelica는 <Color id="GREEN">간소화 CTM</Color>에 대한 내장 지원으로 이 문제를 바꾸었습니다. 이제 블록당 5개의 파일만 만들면 되므로 작업량은 9분의 1로 줄고, 차지하는 파일 공간은 거의 10분의 1로 줄어들며, 시각적 품질 저하도 전혀 없습니다.

## 고급 색상 추적
> [!WARNING]
> 이것은 아직 팩에 완전히 구현되지 않았으며, 작업이 계속 진행 중입니다. 하지만, 다음 버전을 위한 시기상조의 예고 없이 무슨 업데이트이겠습니까!
GTNH에서 <Color id="GREEN">고급 색상 추적</Color>을 기본으로 제공하기 위해 백그라운드에서 많은 작업이 진행되고 있습니다. Euphoria Patches 같은 것을 사용하시는 분들은 이미 익숙하시겠지만, $$\text{soon}^{TM}$$ 모든 셰이더에 대한 완전한 지원이 제공될 것입니다(어쩌면 셰이더 없이도 가능할지도 모릅니다!)
<FloatingImage src="../assets/misc/lava.png" displayWidth="384">
  <ImageAnnotation>
    용암이 생성하는 색상 조명
  </ImageAnnotation>
</FloatingImage>