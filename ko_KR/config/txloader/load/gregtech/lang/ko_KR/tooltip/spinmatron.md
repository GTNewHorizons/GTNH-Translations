3가지 모드: {light_purple:경량} | {blue:표준} | {dark_green:중량}
{gray:{hr}}
{white:총 터빈} 티어당 {gold:{var:parallels} 병렬 처리 수}
{green:{var:speed}% 속도}
{aqua:{var:eu_eff}% EU 사용량}
{white:초대형이 아닌 터빈}은 효율이 감소합니다...
{white:구조물} 티어당 {var:slots_per_tier}개의 {white:터빈 슬롯}을 얻습니다
작동하려면 {gold:등유}가 {aqua:(레시피 티어 * {var:fluid_per_tier} {var:fluid_unit}/s)} 필요합니다
대신 {gold:생촉매 추진 유체}를 공급하면 병렬 처리 수가 {gold:{var:tier2_mult}x} 증가합니다
{yellow:오버클럭은 해치 티어 + 1로 제한됩니다}
{gray:{hr}}
{light_purple:경량 모드}:
- {green:+{var:light_speed}% 속도 보너스}
- 최대 레시피 티어: {aqua:(전압 티어 - {var:light_offset})}
{blue:표준 모드}: 일반 처리
{dark_green:중량 모드}: {gold:생촉매 추진 유체}가 필요합니다
- {gold:병렬 처리 수}를 {gold:{var:heavy_div}}로 나눕니다
- {red:EU 비용}에 {red:{var:heavy_eu}}를 곱합니다
- {light_purple:오버클럭 제한 없음}
- 일부 레시피는 {dark_green:중량 모드}가 {dark_red:필요합니다}