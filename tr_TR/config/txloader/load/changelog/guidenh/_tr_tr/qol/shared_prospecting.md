---
navigation:
  title: Paylaşılan Maden Arama
  parent: qol.md
  icon: gregtech:gt.detrav.metatool.01:100
categories:
    - Yaşam Kalitesi
author: Skorched
date: 2026-05-16
---

# Paylaşılan Maden Arama
Visual Prospecting, çok oyunculu modda nasıl çalıştığını yeniden düzenleyerek devasa bir yaşam kalitesi iyileştirmesi aldı. Yeni bulunan maden keşifleri artık anında aynı takımın tüm üyeleriyle paylaşılacak ([GTNH Team](../misc/gtnh_teams.md) takımından bahsediyorum)! Daha önce <Color id="RED">Paylaşılan Maden Arama</Color>'yı kullanmış oyuncular için işlevsellik etkin biçimde aynı; ancak artık çalışıyor ve optimize edilmiş durumda.

Ayrıca, her sıvıya, daha yüksek Kademedeki maden arayıcı araçlarında bulunan renklerin aynısı kullanılarak renkli katmanlar eklenmesiyle yeraltı sıvı aramalarının ayırt edilmesi kolaylaştırıldı!

Bu kapsamlı yenilemenin bir parçası olarak,

| Komut | İzin Seviyesi | Etki |
| --------------- | --------------- | --------------- |
| `/vp_client_cache_reset` | - | Maden keşiflerinin istemci tarafındaki önbelleğini sıfırlar |
| `/vp team info [detailed]` | 0 | Takımına ilişkin bilgileri gösterir |
| `/vp_team_info <player> [detailed]` | 2 | Hedef oyuncunun takımı hakkında bilgi gösterir |
| `vp_admin team upload <player>` | 2 | Bir oyuncunun önbelleğindeki maden keşiflerini takıma yükler |
| `/vp_admin team clear` | 2 | Takımın maden keşiflerini temizler |
| `/vp_admin servercache rebuild all` | 4 | Sunucu önbelleğini yeniden oluşturur |
| `/vp_admin servercache rebuild spawn` | 4 | Doğma noktası chunk'ları için sunucu önbelleğini yeniden oluşturur |