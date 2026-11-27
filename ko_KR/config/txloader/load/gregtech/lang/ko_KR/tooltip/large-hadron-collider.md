입자를 높은 에너지로 가속한 뒤 충돌시켜 새로운 입자를 생성합니다.
전기적으로 중성인 입자는 영향을 받지 않습니다.
{color_electron_volt:목표 빔 에너지}(최대 {color_electron_volt:{var:max_energy} {TeV}})와 {light_purple:최대 사이클 수}를 설정합니다.
매초 사이클이 진행됩니다.
{hr}
{color_mode:가속기 모드}
더 작은 LHC 고리에서 빔을 가속합니다.
각 사이클은 {color_electron_volt:빔 에너지}를 {color_eu_usage:사이클당 소비되는 {EU}} * {color_electron_volt:{var:ev_per_eu} {eV}} / {gold:빔 레이트}만큼 증가시킵니다.
{color_electron_volt:목표 빔 에너지} 또는 {light_purple:최대 사이클 수}에 도달할 때까지 계속됩니다.
{color_electron_volt:목표 빔 에너지}에 도달하면 현재 {gold:빔 레이트}에 {color_formula:{var:rate_gain}} * {gold:빔 레이트}를 더합니다.
{gold:빔 레이트}가 {color_formula:{var:nerf_cutoff}}를 초과하면 대신 ({color_formula:{var:rate_gain}} * {gold:빔 레이트})^{dark_red:{var:nerf_power}}를 더합니다.
{color_eu_usage:전력} 비용은 {gold:빔 레이트}당 {VNF:tier}의 {color_amperage:1A}에서 시작하며, {light_purple:완료된 사이클 수}에 따라 제곱으로 증가합니다.
{color_eu_usage:P} = ({color_amperage:1A} {VNF:tier}) * {gold:R} * ({light_purple:N}+1)^2
{light_purple:최대 사이클 수}에 도달하면 자동으로 충돌기 모드로 전환합니다.
{hr}
{color_mode:충돌기 모드}
더 큰 LHC 고리에서 반대 방향으로 진행하는 {color_formula:두} 빔으로 빔을 분할하고, 이들이 충돌하여 새로운 입자를 생성합니다.
{color_electron_volt:충돌 에너지}는 {color_electron_volt:빔 에너지}의 {color_formula:{var:collision_multiplier}}배입니다.
{color_electron_volt:충돌 에너지}가 해당 입자의 정지 질량을 초과하면 출력에 입자가 나타납니다.
{color_name:여과된 빔 출력 해치}와 확률 표는 가능한 출력 목록을 보여 주며, 이를 필터링할 수 있게 합니다.
{hr}
{color_mode:부스터 유체}
{color_name:부스터 유체}는 {color_formula:{var:nerf_cutoff}}를 초과하는 {gold:빔 레이트}에 대한 {dark_red:스케일링 지수}를 높입니다.
{color_name:유체 없음}: {dark_red:{var:nerf_power}}
{color_name:{fluid:quarkgluonplasma}}: {dark_red:{var:nerf_power_qgp}}
{color_name:{fluid:molten.magmatter}}: {dark_red:{var:nerf_power_magmatter}}
부스터를 사용하면 {color_electron_volt:빔 에너지}가 즉시 {color_electron_volt:{var:max_energy} {TeV}}로 설정되며, 매 사이클마다 {gold:빔 레이트 {L}}만큼의 유체가 소비됩니다.
공급되는 {color_name:부스터 유체}가 변경되면 빔을 처음부터 다시 가속해야 합니다.
{hr}
LHC 모듈은 네 개이며, 모듈 위쪽의 글자로 구분됩니다:
{aqua:E - 전자기력}: 하전 물질 센서 ({aqua:CMS})
{dark_green:W - 약한 상호작용}: 고급 전체 렙톤 동화 포획기 ({dark_green:ATLAS})
{white:S - 강한 핵력}: 절대 격자 통합 색역학 캡슐화기 ({white:ALICE})
{dark_purple:G - 중력}: 국소 지평선 곡률 결속기 ({dark_purple:LHCb})