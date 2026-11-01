작동하려면 컨트롤러에 {color_name:Turbine}이 필요합니다
{color_range:{var:chunk_size}x{var:chunk_size}} 청크 범위의 오염을 정화합니다
작동 중에는 {color_voltage:{var:eu_usage}} {color_tier:{EU/t}}을 소비합니다
{hr}
각 {color_name:Muffler Hatch}은 다음 계산식에 따라 초당 청크 하나의 오염을 정화합니다
{color_amount:{var:global_multiplier} * B * turbineEff * FLOOR({var:scaling_factor}^mufflerTier)}
- 기계 티어 보너스(B): {color_amount:{var:tier_bonus}}
- turbineEff: {color_name:Turbine} 효율
- 머플러 티어는 {color_name:Energy Hatch} 티어를 초과할 수 없습니다
{hr}
{color_key:Absorption Filters}를 {color_name:Input Bus}에 공급하면 출력이 {color_amount:{var:boost_per_filter}x} 증가합니다
각 필터는 {color_time:{var:filter_lifespan}}초 동안 지속됩니다
정비 문제가 발생할 때마다 정화량이 {color_amount:{var:maint_penalty}%} 감소합니다