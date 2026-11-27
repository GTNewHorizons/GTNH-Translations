{color_key:로켓 연료}를 연소하여 전력을 생산합니다 (최소 {var:min_fuel} {L}/s)
{white:다이나모 해치}의 크기를 제외하면 출력에는 상한이 없습니다
다만 {color_eu_usage:{var:cap1} {EU/t}}와 {color_eu_usage:{var:cap2} {EU/t}}(부스트 미적용)의 소프트 캡이 있어 연료 효율이 감소합니다
{color_danger:비활성 상태에서 로켓 연료를 넣지 마십시오 - 가동 시 소멸됩니다!}
{hr}
연소 과정에는 다음과 같은 추가 투입물이 필요합니다:
시간당 {white:{var:lubricant}} {color_amount:{var:lubricant_amount} {L}} (부스트 시 x{var:boost})
틱당 현재 {EU/t}의 {color_amount:{var:air_percent}%}에 해당하는 {white:공기} (에어 인테이크 해치를 통해서만)
부스트 시 틱당 현재 {EU/t}의 {color_amount:{var:coolant_percent}%}에 해당하는 {white:{var:coolant}} (선택 사항)
{hr}
공기가 고갈되면 기계가 정지하며 수동으로 재시작해야 합니다
부스트를 적용하면 소프트 캡이 {aqua:{var:cap1_boosted} {EU/t}}와 {aqua:{var:cap2_boosted} {EU/t}}로 증가합니다
현재 출력에 따라 예열하는 데 {var:warmup_min}-{var:warmup_max}초가 걸립니다
{hr}
{aqua:{var:pollution_unit} {EU/t}}당 {dark_purple:{var:pollution}}의 오염을 발생시킵니다