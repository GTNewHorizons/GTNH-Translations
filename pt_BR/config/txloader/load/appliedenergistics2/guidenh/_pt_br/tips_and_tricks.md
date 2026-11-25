---
navigation:
  title: Tips and Tricks
  position: 20
---

# Dicas e Truques

Um monte de pequenas recomendações aleatórias

* Remova o Optifine.
* Você pode girar e aplicar zoom em cenas do guia que contam com botões de zoom e de ocultar/exibir anotações.
* Mantenha sua rede com uma estrutura em árvore e evite loops.
* Mantenha o bloco completo [dispositivos](ae2_mechanics/devices.md) em grupos de 8 ou menos, a menos que você entenda profundamente como [canais](ae2_mechanics/channels.md) rota através de uma rede.
* Escolha uma madeira e mantenha-se fiel a ela para todos os seus projetos. [padrões](items_blocks/patterns.md). Permitir substituições às vezes funciona, mas usar o mesmo tipo de madeira em toda parte reduz bastante os transtornos.
* Adicione um [célula de energia](items_blocks/energy_cells.md) para que sua rede consiga lidar com picos de energia.
* Você pode usar água no <ItemLink id="appliedenergistics2:tile.BlockCondenser" />.
* A melhor maneira de manter sua rede organizada é não inserir nela itens aleatórios obtidos de criaturas (mobs), como espadas e armaduras. Cada combinação única de encantamento e durabilidade constitui um [tipo] diferente.(ae2_mechanics/bytes_and_types.md).
* Um evento de "entrada de item no sistema" deve ocorrer ao retornar o resultado de um [padrão de processamento].(items_blocks/patterns.md), como por meio de um <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />, <ItemLink id="appliedenergistics2:tile.BlockInterface" />, ou um slot de retorno de interface. Você não pode simplesmente direcionar o resultado para um baú com um <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> nisso.
* O <ItemLink id="appliedenergistics2:tile.BlockInterface" /> Envia lotes completos de receitas para um estoque adjacente. Isso é útil para garantir que as máquinas não recebam lotes parciais, mas às vezes você quer que os ingredientes vão para vários locais. Você pode conseguir isso usando várias interfaces ou um sistema de gerenciamento de receitas. <ItemLink id="appliedenergistics2:tile.BlockInterface" /> como um [pipe subnet](tricks_example/pipe_subnet.md).