# Reel: 5 Sinais de Alerta da Diabetes Tipo 2

**Arquivo:** `reel-5-sinais-diabetes.mp4` (1080x1920, 9:16, 24 fps, 30s, H.264, sem áudio)
**Estratégia do Manual:** Estratégia 1 — Conteúdo Educativo sobre a Doença (título retirado dos "Exemplos de Posts Conformes")
**Estilo:** papercraft / stop-motion digital, inspirado na técnica do reel analisado em `ANALISE-REEL-CLAUDE-ARCADS.md`
**Paleta:** azul profundo #0d47a1, azul corporativo #1565c0, verde #2e7d32, branco e tons de papel (conforme "Paleta de Cores Recomendada" do Manual)

---

## Legenda Pronta para Publicação

Sede o tempo todo? Idas frequentes ao banheiro? Cansaço que não passa?

Esses podem ser sinais de alerta da Diabetes Tipo 2 — uma condição que pode passar despercebida por anos.

Neste vídeo, listamos 5 sinais que merecem a sua atenção:

1. Sede excessiva
2. Vontade frequente de urinar
3. Cansaço constante
4. Visão embaçada
5. Cicatrização lenta

Notou algum deles? Fale com seu médico. Somente um profissional de saúde pode avaliar, diagnosticar e orientar o tratamento adequado.

Conteúdo educativo. Não substitui consulta médica.

#saude #bemestar #educacaoemsaude #saudemetabolica #prevencao #diabetestipo2

> Observação sobre hashtags: o Manual classifica #diabetestipo2 como RESTRITA — permitida em contexto educativo (que é o caso), proibida em contexto promocional. Para risco zero de redução de alcance, basta removê-la; as demais são livres. Nenhuma hashtag proibida (#tirzepatida, #mounjaro, #emagrecimento, #perdepesorapido, #medicamentoparaemagrecer) foi utilizada.

## Verificação pelo Checklist de Conformidade Pré-Publicação

| Bloco | Verificação | Resultado |
|---|---|---|
| Nomenclatura | Nenhuma menção a Tirzepatida, Mounjaro ou "genérico do Mounjaro" em vídeo, legenda, hashtags ou áudio | CONFORME |
| Conteúdo | Foco 100% na doença (Diabetes Tipo 2); sem termos de risco ("perca peso", "milagre", "resultado garantido"); sem depoimentos ou antes/depois | CONFORME |
| Visual | Sem embalagem, caneta injetora, dispositivo de aplicação ou pessoa aplicando injeção; sem gráficos de peso; apenas pictogramas de objetos (copo, porta, bateria, olho, curativo) | CONFORME |
| CTA | "Fale com seu médico" (CTA recomendado pelo Manual); sem "compre", "peça o seu", "link na bio" | CONFORME |
| Hashtags | Sem termos proibidos; uma restrita usada em contexto educativo (ver observação acima) | CONFORME (com observação) |
| Anúncios | Vídeo destinado a publicação orgânica; se for impulsionado, revalidar com as Políticas da Meta para anúncios | N/A |
| Disclaimer | "Conteúdo educativo. Não substitui consulta médica." presente no vídeo e na legenda | CONFORME |

## Recomendações de Publicação

1. **Áudio:** o arquivo é entregue sem trilha. Adicionar música da biblioteca do próprio Instagram no momento da publicação (mantém direitos musicais em dia e melhora distribuição).
2. **Rotulagem de IA:** o vídeo é ilustração vetorial animada por código (não é mídia fotorrealista gerada por IA). A rotulagem "Feito com IA" da Meta não é obrigatória neste caso, mas pode ser ativada por transparência, a critério da equipe.
3. **Aprovação interna:** submeter à equipe de conformidade antes de publicar, conforme fluxo do Manual.
4. **Monitoramento:** após publicar, observar os comentários nos primeiros 30 minutos (Dica 3 do Manual).

## Como Regenerar ou Adaptar o Vídeo

A fonte está em `fonte/`:

- `reel.html` — animação completa (HTML/CSS/SVG autocontido). Cada cena, texto e ícone é editável no próprio arquivo; a linha do tempo é determinística (função `__seek(ms)`).
- `render.py` — renderiza os frames com Playwright/Chromium (`python3 render.py 24`) e o MP4 é montado com ffmpeg:

```
python3 -m pip install playwright imageio-ffmpeg
python3 render.py 24
ffmpeg -framerate 24 -i frames/f_%04d.jpg -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -movflags +faststart reel-5-sinais-diabetes.mp4
```

Para novos vídeos da série (ex.: "Fatores de Risco da Obesidade", "O Que é Saúde Metabólica"), duplicar `reel.html` e trocar textos e ícones das cenas — mantendo as salvaguardas da análise (`ANALISE-REEL-CLAUDE-ARCADS.md`, seção 5) e este checklist.

---

**MFDireitoDigital / Universe Pharma** — material produzido em conformidade com o Manual v3.0.
