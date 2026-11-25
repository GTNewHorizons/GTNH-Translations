---
item_ids:
  - Thaumcraft:ItemThaumonomicon
navigation:
  title: Thaumcraft
  icon: 'Thaumcraft:ItemThaumonomicon'
  position: 40
---

# Thaumcraft

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

<GameScene interactive={true} wrap="square" align="right" width="240" height="220" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/infusion_altar.snbt" />
</GameScene>

**Thaumcraft 4** (TC4) é um dos principais mods de magia do GTNH e o primeiro mod de magia com o qual você se depara.

Começando pela análise e pela pesquisa, você aprende gradualmente sobre os aspectos contidos em itens e criaturas. Por meio da alquimia e da infusão, é possível criar varinhas, ferramentas mágicas, equipamentos e sistemas de automação.

No NH, o Thaumcraft está intimamente ligado a materiais tecnológicos, ao Twilight Forest e a outros mods de magia. À medida que suas pesquisas avançam, você pode explorar o Botania e o Blood Magic, conectar sistemas mágicos ao AE ou utilizar a magia para manter as máquinas do GT em funcionamento.

Esta página oferece uma visão geral do mundo de Thaumcraft, conceitos básicos e alterações específicas de New Horizons, com foco no uso de instalações mágicas e nas diferenças entre elas. <Color color="#B7A0D6">pontos de pesquisa, Vis e essencial</Color>.

<br clear="all" />

## O Mundo de Thaumcraft

- **Tudo tem aspectos.** Em Thaumcraft, os objetos têm mais do que uma aparência e uma função: eles também contêm <Color color="#B7A0D6">aspects</Color> que você pode observar e estudar. Fogo, água, ordem, vida e metal podem, todos, ser descritos por meio de aspectos. A combinação de aspectos gera propriedades mais complexas; compreender essas relações é fundamental para a pesquisa e a alquimia.

- **O conhecimento torna-se infraestrutura.** O mundo também contém <Color color="#B7A0D6">aura nodes</Color> que coletam energia mágica. Varinhas podem extrair Vis de nodos para uso em criação arcana e como focos para varinhas. A Essentia extraída de itens é utilizada em alquimia, infusão e em alguns dispositivos mágicos. À medida que seu conhecimento e suas instalações evoluem, você passa da pesquisa e criação manuais para o armazenamento de Essentia, logística e produção automatizada.

- **A exploração tem consequências.** O processamento de materiais mágicos pode poluir o ambiente ao redor, enquanto o aprendizado de conhecimentos proibidos pode conferir ao jogador "Warp". Ao pesquisar uma nova habilidade, informe-se sobre seus usos, custos e efeitos.

## O Thaumonomicon

O <ItemLink id="Thaumcraft:ItemThaumonomicon" showIcon="left" /> É a sua principal fonte de conhecimento sobre o Thaumcraft, contendo explicações de pesquisas, anotações de pesquisa e receitas desbloqueadas. Seus registros de pesquisa fornecem instruções de operação para dispositivos específicos.

O livro possui abas separadas para diferentes tópicos e complementos. As pesquisas possuem pré-requisitos, e algumas entradas só aparecem após análises específicas ou o cumprimento de outras condições. **A ausência de uma entrada não significa, necessariamente, que ela não exista.**

| Conteúdo do livro | Informações fornecidas |
| --- | --- |
| Pesquise ícones e conexões | Pré-requisitos entre entradas de pesquisa e dicas sobre como desbloqueá-las |
| <Color color="#B7A0D6">Research notes</Color> | Pesquisa realizada em uma Mesa de Pesquisa, principalmente por meio de conexões de aspectos. |
| Pesquisa que consome pontos de pesquisa | Os tipos de aspecto e os pontos de pesquisa necessários para desbloqueá-lo |
| Pesquisa concluída | Usos do aparelho, instruções de operação e receitas |
| <Color color="#D5B77A">Forbidden knowledge markers</Color> | Os efeitos roxos e os avisos associados indicam que aprender sobre esta pesquisa pode causar distorção. |

Pesquisas concluídas precisam ser lidas para que seu conteúdo seja desbloqueado. **O desbloqueio de pesquisas e os requisitos de materiais são independentes:** visualizar uma receita no livro não significa que sua tecnologia e suas instalações mágicas já sejam capazes de produzi-la.

## Aspectos, Pontos de Pesquisa, Vis e Essentia

Esses conceitos frequentemente utilizam os mesmos ícones de aspecto, mas servem a propósitos diferentes. Ao encontrar um ícone, verifique primeiro se ele aparece em uma Mesa de Pesquisa, em uma varinha ou em um recipiente de essência.

| Conceito | Significado | Principais usos |
| --- | --- | --- |
| <Color color="#B7A0D6">Aspects</Color> | Propriedades que descrevem itens, criaturas e fenômenos mágicos | Compreender as combinações de pesquisa e identificar quais essências um item pode fornecer |
| <Color color="#B7A0D6">Research points</Color> | Recursos de pesquisa acumulados pelo jogador, rastreados separadamente para cada aspecto | Conectando anotações de pesquisa, combinando aspectos e desbloqueando pesquisas |
| <Color color="#B7A0D6">Vis</Color> | Energia mágica armazenada em uma varinha, monitorada separadamente para cada aspecto primordial | Fabricação em uma Bancada de Trabalho Arcano, utilizando focos de varinha e operações semelhantes |
| <Color color="#B7A0D6">Essentia</Color> |Aspectos extraídos de itens que podem ser armazenados e transportados | Alquimia, infusão e alguns dispositivos mágicos |

## Aspectos e Pontos de Pesquisa

Os seis <Color color="#B7A0D6">primal aspects</Color> são <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Air (Aer), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Earth (Terra), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Fire (Ignis), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Water (Aqua), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Order (Ordo) e <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" />Entropy (Perditio). Aspectos compostos são formados a partir de dois outros aspectos; os complementos do NH também expandem o sistema de aspectos.

Escanear itens, criaturas e outros alvos pode revelar aspectos e conceder pontos de pesquisa. Alguns alvos exigem que você conheça seus aspectos constituintes antes de poderem ser escaneados. Combinar aspectos em uma Mesa de Pesquisa também pode ajudar você a descobrir novos aspectos compostos. Se lhe faltarem pontos de pesquisa, você precisará reabastecer seus recursos de pesquisa; recarregar uma varinha não resolverá esse problema.

## Vis e Essentia

O *Vis* em uma varinha é contabilizado separadamente para os seis aspectos primordiais. Verifique a quantidade armazenada de cada aspecto exigida por uma receita arcana; ter um aspecto totalmente carregado não compensa a falta de outro.

A essência é, geralmente, extraída de itens por meio de um Forno Alquímico ou instalações similares, sendo então coletada em frascos ou outros recipientes. Uma receita que exija aspectos compostos, como "metal" ou "vida", frequentemente solicita a essência correspondente, em vez de Vis contido em uma varinha..

Aer Vis required by an Arcane Worktable and Metallum essentia required by infusion come from a wand and an essentia supply system, respectively. **Research points, wand Vis and essentia in jars cannot replace each other.**

## Nodes and Sources of Magical Energy

**Aura nodes** are concentrations of magical energy in the world. Observation tools reveal their aspects, and wands can draw Vis from them. Most nodes gradually regenerate their energy, so finding and managing nodes is an important part of early magical power supply.

Nodes have different types, qualities and aspect compositions. Once you understand them, you can research ways to move, preserve and modify them, using what you find while exploring to supply your base's magical facilities.

> [!WARNING]
> When drawing energy from a node with an early wand, avoid casually draining an aspect to zero. <Color color="#D5B77A">Draining a node completely</Color> can damage it and affect its ability to provide energy later. First learn what protections your wand and completed research offer.

Later, you will also encounter <Color color="#B7A0D6">Centi-Vis</Color>: modified nodes can supply compatible devices with this form of energy. Storing Vis in a wand and building a Centi-Vis supply network are two forms of power supply that you need to understand separately.

## Vis Costs and Discounts

<Color color="#B7A0D6">Wand capacity</Color> determines how much Vis of each primal aspect the wand can store, while <Color color="#B7A0D6">Vis discounts</Color> reduce the energy actually consumed by an operation. Wand caps and some equipment provide discounts. For more demanding recipes, consider both wand capacity and the discounts available to you.

For example, suppose an arcane recipe has a base requirement of 100 Vis of one aspect, with a total applicable discount of 20%. The actual requirement becomes 80 Vis of that aspect. This allows a wand with a capacity of 80 to satisfy a recipe that originally required 100, but the wand's capacity remains 80.

| Problem | What to Check |
| --- | --- |
| The wand has enough capacity but lacks stored energy | Replenish every type of Vis required by the recipe |
| A fully charged wand still cannot meet the recipe's requirements | Upgrade the wand or increase the discounts applicable to that craft |
| You have equipment with discounts but still cannot craft | Check the actual requirements, whether the equipment is worn and the stored amount of each aspect |
| Infusion lacks essentia | Prepare an essentia supply; Vis discounts cannot replace essentia ingredients |

## Flux, Taint and Warp

Environmental problems and effects on the player need to be understood separately.

| Concept | Main Target | What to Know |
| --- | --- | --- |
| <Color color="#D5B77A">Flux</Color> | The surrounding environment | Improper magical processing can release pollution; watch your alchemy facilities and their surroundings |
| <Color color="#D5B77A">Taint</Color> | Terrain, blocks and creatures | An environmental hazard that needs dedicated treatment; investigate its source and control methods when you find it |
| <Color color="#D5B77A">Warp</Color> | The player | Forbidden research and some actions cause Warp, which can trigger related events |

Cleaning up environmental pollution does not remove the player's Warp, and dealing with Warp does not replace treating a tainted area. Look for forbidden knowledge warnings when reading new research, and consider pollution control when preparing new alchemy facilities.

> [!WARNING]
> Warp Theory adds more Warp events in NH. <Color color="#D5B77A">High Warp</Color> can trigger dangerous events that damage your base. Before pursuing forbidden research, learn about these events and how to respond, and make suitable arrangements for valuable facilities and items.

## NH-Specific Changes and Mod Integration

NH makes many changes to Thaumcraft's material progression, research and user experience, mainly in the following areas.

| Topic | What to Watch For in NH |
| --- | --- |
| Wand materials | The usual wand progression involves Twilight Forest boss materials; check current recipes and material sources before crafting |
| Wand upgrades | Capacity and Vis discounts need to develop together; after completing the relevant research, you can also replace wand rods and caps |
| Recipe lookup | Use the Thaumonomicon for research and operating instructions, and NEI to check current recipes; the quest book explicitly directs you to NEI for some wand recipes |
| Scanning conveniences | You can scan items in your inventory; scanning an entire chest still requires the corresponding research |
| Research and aspect assistance | Aspect Recipe Index and similar features help you find aspect sources, combinations and related recipes |
| Magical automation | Golems, Automagy and related content provide logistics and automation facilities; Thaumic Energistics connects essentia storage and supply to AE |
| Technology and magic integration | Addons such as EMT provide tools and devices; GT also has facilities such as the Research Completer and Vis Maintenance Hatch |
| Other magic paths | Botania and Blood Magic also have connections to Thaumcraft research and materials |

Magic offers movement and building tools, equipment and enchantments, durability repair, material processing, and item and essentia automation. Choose a research direction based on your current needs, then follow its prerequisites to develop the facilities you need.

## Topics

This category organizes guides by topic, with each topic page directly under Thaumcraft. The guides focus on an overview of mechanics, facility uses, resource relationships and NH-specific changes. The Thaumonomicon and NEI provide detailed operating instructions and recipes.

| Chapter | Main Content |
| --- | --- |
| [Thaumcraft Basics](./thaumcraft_basics.md) | The Thaumonomicon, aspects, nodes, Warp, Vis, Vis discounts and an overview of the world |
| [Aspects, Scanning and Research](./aspects_scanning_research.md) | The aspect system, scanning conditions, research points, research notes and prerequisites |
| [Wands, Vis and Nodes](./wands_vis_nodes.md) | Wand crafting and discounts, Vis sources, node types and cultivation, and Centi-Vis supply |
| [Alchemy and Essentia](./alchemy_essentia.md) | Crucibles and alchemy devices, essentia production and distribution, pollution control |
| [Infusion Crafting](./infusion_crafting.md) | Altar components, recipe resources, stability and integration with other devices |
| [Magic Automation](./magic_automation.md) | Item logistics, inventory control, fluid devices, production support and golem uses |
| [Warp and Eldritch Knowledge](./warp_eldritch.md) | Warp management, Eldritch research, Opening the Eye, and exploration of the Outer Lands |
| [Thaumic Tinkerer](./thaumic_tinkerer.md) | Custom enchanting, durability repair, infused crops, elemental fire, and KAMI devices |
| Addons and GT Integration | Thaumic Energistics, other addon facilities, and GT's magical devices and material connections |

</Column>