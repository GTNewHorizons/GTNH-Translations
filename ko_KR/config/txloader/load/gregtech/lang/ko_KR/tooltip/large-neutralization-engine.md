모든 문제를 (해)결합니다!
{hr}
선택적으로 {aqua:염기}를 공급하여 {color_mechanic:효율}을 높일 수 있습니다:
{aqua:{var:sodium_hydroxide_rate}/분}의 {aqua:수산화 나트륨} : {color_mechanic:{var:sodium_hydroxide_eff}%}
{aqua:{var:potassium_hydroxide_rate}/분}의 {aqua:수산화 칼륨} : {color_mechanic:{var:potassium_hydroxide_eff}%}
{aqua:{var:caesium_hydroxide_rate}/분}의 {aqua:수산화 세슘} : {color_mechanic:{var:caesium_hydroxide_eff}%}
{aqua:{var:francium_hydroxide_rate}/분}의 {aqua:수산화 프랑슘} : {color_mechanic:{var:francium_hydroxide_eff}%}
{hr}
산을 연소시켜 {dark_green:독성 잔여물}을 생산합니다
{dark_green:독성 잔여물}이 {dark_aqua:용량}을 초과하면 기계가 {color_danger:폭발합니다}
매 틱마다 {dark_green:독성 잔여물}이 {green:0.05 * 연료 밀도 ({EU}/{L})^0.8 * 연료 소비량 ({L}) * rand({var:residue_rand_min}, {var:residue_rand_max})}만큼 증가합니다
매 틱마다 {dark_green:독성 잔여물}이 {green:기본 붕괴 * 붕괴 부스트 * 독성 잔여물^0.08}만큼 붕괴합니다
{yellow:멀티블록이 비활성화되면 잔여물은 10배 느리게 붕괴합니다}
{hr}
최대 {blue:{var:robot_arm_amount_for_decay_boost} 로봇 팔}까지 삽입하여 {blue:붕괴 부스트}를 높일 수 있습니다:
{white:붕괴 부스트 =} {green:sqrt(로봇 팔) * N^(로봇 팔 티어 - 1)} 여기서 {green:N={var:robot_arm_bonus_low}} ({tier-color:arm_tier_low:{VN:arm_tier_low}-}) 또는 {green:N={var:robot_arm_bonus_high}} ({tier-color:arm_tier_high:{VN:arm_tier_high}+})
매분 {green:로봇 팔 / (45 * (로봇 팔 티어 + 1))}의 확률로 정확히 {blue:로봇 팔} 하나를 소멸시킵니다
{hr}
구조물은 {color_mode:3개의 티어}를 가지며, 이 티어가 {blue:기본 붕괴}와 {dark_aqua:용량}을 결정합니다:
{color_mode:T1} : {color_mode:강화된 무생물 기계 케이싱} : {blue:{var:tier1_decay}} : {dark_aqua:{var:tier1_capacity}}
{color_mode:T2} : {color_mode:정밀 고정식 기계 케이싱} : {blue:{var:tier2_decay}} : {dark_aqua:{var:tier2_capacity}}
{color_mode:T3} : {color_mode:얼티메이트 정지형 기계 케이싱} : {blue:{var:tier3_decay}} : {dark_aqua:{var:tier3_capacity}}