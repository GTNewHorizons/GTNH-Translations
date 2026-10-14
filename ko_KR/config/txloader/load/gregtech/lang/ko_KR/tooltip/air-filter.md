작동하려면 컨트롤러에 {white:Turbine}이 필요합니다.
주변 {green:{var:chunk_size}x{var:chunk_size}} 청크의 오염을 정화합니다.
가동 중에는 고정된 양의 {aqua:{var:eu_usage} EU/t}를 소모합니다.
{gray:{hr}}
각 {white:Muffler Hatch}는 초당 청크 하나에서 다음 양의 오염을 제거합니다.
{green:{var:global_multiplier} * B * turbineEff * FLOOR({var:scaling_factor}^mufflerTier)}
- 이 기계의 티어 보너스(B) = {green:{var:tier_bonus}}
- turbineEff = {white:Turbine} 효율
- 유효한 {white:Muffler Hatch} 티어는 {white:Energy Hatch} 티어에 제한됩니다.
{gray:{hr}}
{white:Input Bus}를 통해 {gold:Absorption Filters}를 공급하면 제거되는 오염량이 두 배가 됩니다(개당 {gold:{var:filter_lifespan}}초).
정비 문제가 하나 발생할 때마다 제거되는 오염량이 {green:{var:maint_penalty}%} 감소합니다.