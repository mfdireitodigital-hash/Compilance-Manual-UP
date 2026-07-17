# Análise de Reel do Instagram: Técnica "Claude + Arcads" para Vídeos em Papercraft

**Reel analisado:** https://www.instagram.com/reel/Da2oI8YBQe5/
**Autor do reel:** @guivilas.ia (Guilherme Vilas | Inteligência Artificial)
**Data de publicação:** 15/07/2026
**Duração:** 61 segundos
**Engajamento no momento da análise:** 143 curtidas, 104 comentários
**Legenda original:** "Comenta 'PAPEL' que eu te mando as skills e o guia completo #ia #inteligenciaartificial #claude #claudemonet"

**Análise elaborada para:** Universe Pharma Oficial (RZS PHARMA LTDA), como anexo ao Manual de Conformidade e Comunicação Segura no Instagram (v3.0)

---

## 1. Resumo Executivo

O reel é um tutorial de criação de conteúdo com Inteligência Artificial. O criador demonstra como produzir **vídeos animados em estilo papercraft / stop-motion** (recortes de papel que se montam em cena) usando o assistente **Claude** conectado à plataforma **Arcads** (via conector MCP) e ao modelo de vídeo **Seedance 2.0**. O exemplo mostrado é um mini-documentário sobre a história da comunicação humana ("300,000 B.C. — The Stone Age", "The First Schools", "2000s — The Modern City").

O vídeo **não tem relação com produtos farmacêuticos**. Seu valor para a Universe Pharma é **instrumental**: a técnica demonstrada é uma forma de produzir conteúdo visual educativo de alto engajamento — formato que se encaixa diretamente nas Estratégias 1, 2 e 4 do Manual (conteúdo educativo sobre a doença, institucional e de conscientização sobre saúde metabólica), desde que aplicada com as salvaguardas listadas na seção 5 desta análise.

---

## 2. O Que o Reel Mostra (linha do tempo)

| Trecho | Conteúdo |
|---|---|
| 0s–10s | Demonstração do resultado final: vídeo papercraft "história da humanidade" com cartelas de época (Idade da Pedra, primeiras escolas, era das redes sociais, cidade moderna), sob o título "Claude + arcads" |
| 10s–14s | Gancho: "como é que você pode fazer isso" |
| 14s–28s | Passo a passo de configuração no aplicativo Claude: menu lateral, opção "Customize", aba "Connectors", "Add custom connector", cadastro do conector "Arcads" com a URL do servidor MCP remoto |
| 28s–40s | No chat do Claude: anexa imagens de referência ("Pinterest do teu nicho") e envia o prompt de análise de estilo; o conector Arcads executa a ferramenta `arcads_generate_image_gpt` para gerar as imagens-base (geração assíncrona, "checking every 30s") |
| 40s–55s | Segundo prompt usando a skill `/motion-design` com "Arcads + Seedance 2.0" para animar as imagens geradas em stop-motion; exibição dos resultados com botões de download |
| 55s–61s | Chamada para ação: "Comenta 'PAPEL'" para receber as skills e o guia completo por mensagem direta |

## 3. A Técnica Ensinada, Passo a Passo

1. **Conectar a Arcads ao Claude:** no aplicativo Claude, acessar "Customize" → "Connectors" → "Add custom connector"; nomear o conector (Arcads) e informar a URL do servidor MCP remoto da plataforma; clicar em "Add" e autenticar a conta.
2. **Coletar referências visuais:** reunir imagens de referência do estilo desejado (no reel, artes em papercraft coletadas de plataformas como Pinterest) e anexá-las ao chat.
3. **Analisar o estilo e gerar imagens-base.** Prompt exibido no vídeo (em inglês, com o modelo "Sonnet 4.6" selecionado):
   > "Analyze all reference images with GPT-Image to understand the visual style and composition & aesthetic."
   O Claude aciona a ferramenta `arcads_generate_image_gpt` do conector, que gera as cenas estáticas no estilo aprendido (no exemplo, cartelas de épocas históricas).
4. **Animar as imagens com a skill de motion design.** Prompt exibido no vídeo:
   > "Use /motion-design with Arcads + Seedance 2.0. Create a 5-second stop-motion animation from the last 5 images about human stone age to Modern society artificial Inteligence. Start on an empty canvas and have all paper elements assemble themselves piece by piece into the final compositions. Realistic papercraft textures, layered depth, subtle shadows, clean documentary-style motion, 16:9 landscape."
   O resultado são clipes de aproximadamente 5 segundos em que os elementos de papel "se montam" na cena, prontos para download e edição em sequência.

**Ferramentas envolvidas:** Claude (assistente de IA, plano com suporte a conectores/skills), Arcads (plataforma paga de criativos publicitários com IA, conectada via MCP), Seedance 2.0 (modelo de geração de vídeo), GPT-Image (modelo de geração/análise de imagem acionado pela Arcads).

## 4. Por Que Este Formato Interessa à Universe Pharma

- **Compatível com os "Elementos Visuais Seguros" do Manual:** animações em papercraft são, por natureza, infográficos animados — não envolvem corpos reais, fotos de pacientes, embalagens ou dispositivos. Eliminam de saída vários gatilhos visuais de risco máximo (reconhecimento de imagem da Meta para embalagem, caneta injetora, aplicação de injeção).
- **Sem risco de direito de imagem/LGPD de pacientes:** por não usar pessoas reais, o formato evita depoimentos visuais e comparações corporais ("antes e depois", "pessoa obesa vs pessoa magra"), ambos proibidos pelo Manual.
- **Formato de storytelling com alto potencial de engajamento orgânico**, alinhado às estratégias permitidas:
  - **Estratégia 1 (educativo sobre a doença):** ex.: "A jornada da glicose no corpo", "5 sinais de alerta da Diabetes Tipo 2", "Como a resistência à insulina se desenvolve" em papercraft.
  - **Estratégia 2 (institucional):** ex.: linha do tempo "Universe Pharma: inovação em saúde" no mesmo formato documental do reel analisado.
  - **Estratégia 4 (saúde metabólica):** ex.: "O que é saúde metabólica", "Pilares do manejo da obesidade: nutrição, movimento e acompanhamento médico".

## 5. Salvaguardas Obrigatórias ao Adotar a Técnica

A ferramenta muda a forma de produzir; **não muda nenhuma regra do Manual**. Todo vídeo gerado por IA continua sujeito ao Checklist de Conformidade Pré-Publicação (18 critérios) antes de ir ao ar.

1. **Nunca solicitar à IA imagens dos elementos proibidos**, nem mesmo estilizados em papel: embalagem do medicamento, caneta injetora ou dispositivo de aplicação, pessoa aplicando injeção, gráficos de perda de peso, "antes e depois", comparações corporais. A moderação da Meta e a RDC 96/2008 alcançam também representações ilustradas/estilizadas.
2. **Nomenclatura:** os prompts, as cartelas de texto dentro do vídeo, a legenda, o áudio e as hashtags não podem citar Tirzepatida, Mounjaro ou variações ("genérico do Mounjaro"), conforme os Gatilhos Críticos do Glossário.
3. **Não replicar o CTA do reel ("Comenta 'PAPEL' que eu te mando")** em conteúdo da farmacêutica: além de configurar isca de engajamento (formato despriorizado pela Meta), enviar material sobre medicamento tarjado por mensagem direta a leigos caracterizaria publicidade irregular perante a RDC 96/2008. CTAs permitidos permanecem os do Manual: "Fale com seu médico", "Saiba mais sobre a doença".
4. **Rotulagem de conteúdo gerado por IA:** a Meta exige sinalização de mídia realista gerada/alterada por IA e o CONAR tem recomendações no mesmo sentido. Em estilo papercraft (claramente ilustrativo) o risco é menor, mas recomenda-se manter a transparência ativando o rótulo de IA quando aplicável.
5. **Identidade visual:** adaptar paleta e tipografia às diretrizes do Manual (azuis corporativos #0d47a1/#1565c0, verde #2e7d32 para elementos de aprovação; tipografia limpa) para manter consistência institucional.
6. **Vetting de terceiros (LGPD/segurança):** Arcads e Seedance são plataformas externas; não enviar a elas dados pessoais, materiais internos confidenciais ou artes não públicas sem avaliação prévia. Usar apenas referências visuais públicas ou próprias.
7. **Revisão humana obrigatória:** conteúdo gerado por IA pode inserir texto incorreto ou grafias erradas dentro das imagens (o próprio reel exibe "artificial Inteligence" grafado errado no prompt). Revisar cada cartela de texto antes da publicação — informação de saúde incorreta gera risco sanitário e reputacional.

## 6. Veredito

| Critério | Avaliação |
|---|---|
| O reel em si viola regras aplicáveis à Universe Pharma? | Não se aplica — é conteúdo de terceiro, de nicho de IA, sem menção a medicamentos |
| A técnica pode ser adotada pela Universe Pharma? | Sim, com as salvaguardas da seção 5 |
| Melhor uso recomendado | Vídeos educativos e institucionais (Estratégias 1, 2 e 4 do Manual) em papercraft/stop-motion |
| Risco principal | Usar a facilidade de geração por IA para criar justamente os elementos proibidos (embalagem, aplicação, antes/depois) ou textos com gatilhos críticos |
| Próximo passo sugerido | Piloto: 1 vídeo institucional + 1 educativo sobre Diabetes Tipo 2, aprovados pelo checklist e pela equipe de conformidade antes da publicação |

## 7. Metodologia da Análise

Esta análise foi produzida a partir do arquivo de vídeo público do reel (61s), do qual foram extraídos 31 quadros (1 a cada 2 segundos) para leitura das telas, prompts e legendas exibidos, complementados pelos metadados públicos da página (legenda, autor, data, descrições de acessibilidade). O áudio narrado não foi transcrito; as citações de prompts correspondem ao texto visível na tela.

---

**MFDireitoDigital**
Anexo de análise — não substitui nenhuma seção do Manual de Conformidade v3.0.
