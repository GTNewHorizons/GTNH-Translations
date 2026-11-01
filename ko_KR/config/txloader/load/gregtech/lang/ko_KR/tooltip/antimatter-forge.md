{light_purple:차원은 포함되지 않습니다!}
원시물질을 반물질로 변환합니다
렌더링을 비활성화하려면 드라이버를 사용하십시오
수동으로 {var:base_consumption} + ({dark_aqua:반물질} * 1000)^(1.5 - {green:{bold:{underline:M}}}) {EU/t}를 소비합니다
비어 있을 때 소비량이 매 틱 1%씩 감소합니다
반물질을 생산하기 위해 매 주기마다 ({dark_aqua:반물질} * {var:active_base_mult})^(1.5 - {dark_purple:{bold:{underline:G}}}) {EU}를 능동적으로 사용합니다
{hr}
매초 주기가 진행됩니다
매 주기마다 16개의 반물질 해치 중 반물질이 가장 적은 양을 기록합니다
최저량보다 많은 반물질을 보유한 모든 해치는 {red:차이의 절반을 잃습니다!}
주기 도중 에너지/원시물질이 고갈되면 {red:반물질의 10%가 소멸합니다}
해치당 기본 생산량은 매 주기 반물질 (1/16) * ({dark_aqua:반물질}^(0.5 + {gold:{bold:{underline:C}}}))입니다
각 해치는 해치당 기본 생산량에 다음과 같은 정규분포에서 추출한 난수를 곱합니다
평균은 0.2 + {aqua:{bold:{underline:A}}}이고 분산은 1입니다
반물질의 총 획득량이 음수일 수도 있습니다!
{hr}
반물질 생성을 향상하기 위해 안정화 유체를 공급할 수 있습니다
각 안정화는 한 번에 유체 하나만 사용할 수 있습니다
{green:{bold:{underline:M}}}{green:자기 안정화} (주기당 유체 {dark_aqua:반물질}^0.5 {L} 소비)
1. {fluid:molten.tengampurified} = {green:0.1}
2. {fluid:temporalfluid} = {green:0.2}
3. {fluid:molten.magmatter} = {green:0.3}
{dark_purple:{bold:{underline:G}}}{dark_purple:중력 안정화} (주기당 유체 {dark_aqua:반물질}^0.5 {L} 소비)
1. {fluid:molten.spacetime} = {dark_purple:0.05}
2. {fluid:spatialfluid} = {dark_purple:0.10}
3. {fluid:molten.eternity} = {dark_purple:0.15}
{gold:{bold:{underline:C}}}{gold:구속 안정화} (주기당 유체 {dark_aqua:반물질}^(2/7) {L} 소비)
1. {fluid:molten.shirabon} = {gold:0.05}
2. {fluid:molten.magnetohydrodynamicallyconstrainedstarmatter} = {gold:0.10}
{aqua:{bold:{underline:A}}}{aqua:활성화 안정화} (주기당 유체 {dark_aqua:반물질}^(1/3) {L} 소비)
1. {fluid:naquadah based liquid fuel mkv (depleted)} = {aqua:0.05}
2. {fluid:naquadah based liquid fuel mkvi (depleted)} = {aqua:0.10}