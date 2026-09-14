---
navigation:
  title: 공유 탐광
  parent: qol.md
  icon: gregtech:gt.detrav.metatool.01:100
categories:
    - 편의성
author: Skorched
date: 2026-05-16
---

# 공유 탐광
Visual Prospecting은 멀티플레이에서 작동하는 방식을 개편하여 엄청난 편의성 향상을 얻었습니다. 새로 발견된 탐광 정보는 이제 같은 팀, 정확히는 [GTNH Team](../misc/gtnh_teams.md)의 모든 구성원에게 즉시 공유됩니다! 과거에 <Color id="RED">공유 탐광</Color>을 사용했던 플레이어라면, 기능은 사실상 동일하지만 이제 제대로 작동하며 최적화되었습니다.

또한, 지하 유체 탐사는 각 유체에 색상 오버레이를 추가하여 구분하기 쉬워졌으며, 이는 상위 티어 탐광 도구에서 볼 수 있는 것과 동일한 색상을 사용합니다!

이번 개편의 일환으로,

| 명령어 | 권한 레벨 | 효과 |
| --------------- | --------------- | --------------- |
| `/vp_client_cache_reset` | - | 클라이언트 측 탐광 정보 캐시를 초기화합니다 |
| `/vp team info [detailed]` | 0 | 자신의 팀에 대한 정보를 표시합니다 |
| `/vp_team_info <player> [detailed]` | 2 | 대상 플레이어의 팀에 대한 정보를 표시합니다 |
| `vp_admin team upload <player>` | 2 | 한 플레이어의 캐시에 있는 탐광 정보를 팀에 업로드합니다 |
| `/vp_admin team clear` | 2 | 팀 탐광 정보를 지웁니다 |
| `/vp_admin servercache rebuild all` | 4 | 서버의 캐시를 재구축합니다 |
| `/vp_admin servercache rebuild spawn` | 4 | 스폰 청크에 대해 서버의 캐시를 재구축합니다 |