Çalışması için kontrolcüde bir {color_name:Türbin} gerektirir
{color_range:{var:chunk_size}x{var:chunk_size}} yığınlık alanda kirliliği temizler
Çalışırken {color_voltage:{var:eu_usage}} {color_tier:EU/t} tüketir
{hr}
Her {color_name:Egzoz Çıkışı} saniyede bir yığının kirliliğini şuna göre temizler
{color_amount:{var:global_multiplier} * B * turbineEff * FLOOR({var:scaling_factor}^mufflerTier)}
- Makine Kademesi Bonusu (B): {color_amount:{var:tier_bonus}}
- turbineEff: {color_name:Türbin} verimliliği
- Egzoz Çıkışı Kademesi {color_name:Enerji Kapağı} Kademesi ile sınırlıdır
{hr}
Çıktıyı {color_amount:{var:boost_per_filter}x} ile çarpmak için bir {color_name:Giriş Yolu}'na {color_key:Soğurma Filtreleri} ver
Her filtre {color_time:{var:filter_lifespan}} saniye dayanır
Her bakım sorunu temizliği {color_amount:{var:maint_penalty}%} azaltır