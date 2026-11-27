24시간마다 총 용량의 1%에 해당하는 에너지를 잃습니다
{VNF:minWirelessCapacitorTier} 축전기당 수동 손실량은 {red:{var:maxPassiveDrain}} {EU/t}로 제한됩니다
수동 손실량은 상위 축전기 티어마다 {color_danger:{var:wirelessCapPassiveDrainTierMultiplier}}배 증가합니다
수동 손실량은 현재 발생한 유지보수 문제의 수만큼 곱해집니다
{hr}
유리 외벽은 가장 높은 축전기 티어보다 {var:glassTiersBelowCellAllowed}티어 낮아야 합니다
더 많거나 더 좋은 축전기를 추가하여 용량을 늘리십시오
{hr}
드라이버를 들고 우클릭하면 무선 모드를 활성화할 수 있습니다
이 모드는 멀티블록에 {TC:minWirelessCapacitorTier:{VN:minWirelessCapacitorTier}+} 축전기가 있어야만 활성화할 수 있습니다.
활성화되면 {blue:{var:rebalanceTicks}}틱마다 LSC가
무선 {EU} 네트워크와 균형을 맞추려고 시도합니다.
LSC에 {red:{var:wirelessEuCap}} ({VNF:minWirelessCapacitorTier}) {EU}보다 적으면
네트워크에서 가져와 LSC에 추가합니다.
더 많으면 {dark_red:{bold:{underline:모든 초과분}}} {EU}를 네트워크에 추가하고 LSC에서 제거합니다
기지를 망가뜨릴 수 있으니 주의하십시오
임계값은 상위 축전기 티어마다 {color_danger:{var:wirelessCapTierMultiplier}}배 증가합니다