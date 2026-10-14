{light_purple:차원은 포함되지 않습니다!}
원시물질을 반물질로 변환합니다
드라이버를 사용하여 렌더링을 비활성화합니다
{var:base_consumption} + ({dark_aqua:반물질} * 1000)^(1.5 - {green:{bold:{underline:M}}}) EU/t를 지속적으로 소모합니다
비어 있을 때는 매 틱마다 소모량이 0.5%씩 감소합니다
반물질을 생성하기 위해 주기마다 ({dark_aqua:반물질} * {var:active_base_mult})^(1.5 - {dark_purple:{bold:{underline:G}}}) EU를 소모합니다
{gray:{hr}}
매초 주기가 진행됩니다
매 주기마다 반물질 해치 16개의 반물질 보유량 중 최저량을 기록합니다
최저량보다 많은 모든 해치는 {red:차이의 절반을 잃습니다!}
{red:주기 중 에너지/원시물질이 바닥나면 반물질의 10%를 소멸시킵니다}
주기마다 해치당 기본 생산량은 반물질 (1/16) * ({dark_aqua:반물질}^(0.5 + {gold:{bold:{underline:C}}}))입니다
각 해치의 해치당 기본 생산량에 다음 정규 분포에서 추출한 난수를 곱합니다
평균은 0.2 + {aqua:{bold:{underline:A}}}이고 분산은 1입니다
반물질 총 획득량이 음수가 될 수도 있습니다!
{gray:{hr}}
안정화 유체를 공급하여 반물질 생성을 개선할 수 있습니다
각 안정화 방식은 한 번에 유체 하나만 사용할 수 있습니다
{green:{bold:{underline:M}}}{green:자기 안정화} (주기마다 유체 {dark_aqua:반물질}^0.5 L를 소모합니다)
1. {fluid:molten.tengampurified} = {green:0.1}
2. {fluid:temporalfluid} = {green:0.2}
3. {fluid:molten.magmatter} = {green:0.3}
{dark_purple:{bold:{underline:G}}}{dark_purple:중력 안정화} (주기마다 유체 {dark_aqua:반물질}^0.5 L를 소모합니다)
1. {fluid:molten.spacetime} = {dark_purple:0.05}
2. {fluid:spatialfluid} = {dark_purple:0.10}
3. {fluid:molten.eternity} = {dark_purple:0.15}
{gold:{bold:{underline:C}}}{gold:구속 안정화} (주기마다 유체 {dark_aqua:반물질}^(2/7) L를 소모합니다)
1. {fluid:molten.shirabon} = {gold:0.05}
2. {fluid:molten.magnetohydrodynamicallyconstrainedstarmatter} = {gold:0.10}
{aqua:{bold:{underline:A}}}{aqua:활성화 안정화} (주기마다 유체 {dark_aqua:반물질}^(1/3) L를 소모합니다)
1. {fluid:naquadah based liquid fuel mkv (depleted)} = {aqua:0.05}
2. {fluid:naquadah based liquid fuel mkvi (depleted)} = {aqua:0.10}