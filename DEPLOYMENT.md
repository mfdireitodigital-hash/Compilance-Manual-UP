# Guia de Implantação Permanente

## Informações do Projeto

**Nome do Projeto:** Manual de Conformidade - Universe Pharma  
**Versão:** 3.0  
**Data de Criação:** Novembro de 2025  
**Elaborado por:** MFDireitoDigital  
**Tipo:** Site Estático (HTML5 + CSS3 + JavaScript)

---

## Requisitos de Servidor

- Servidor Web (Apache, Nginx, IIS ou similar)
- Suporte a HTTP/HTTPS
- Sem requisitos de backend ou banco de dados
- Sem requisitos de linguagens de programação

## Instruções de Implantação

### Opção 1: Hospedagem em Servidor Web Tradicional

1. **Copiar arquivos para o servidor:**
   ```bash
   scp -r /home/ubuntu/universe_pharma_compliance_manual/* usuario@seu-servidor.com:/var/www/html/compliance-manual/
   ```

2. **Configurar permissões:**
   ```bash
   chmod -R 755 /var/www/html/compliance-manual/
   chmod -R 644 /var/www/html/compliance-manual/*
   ```

3. **Acessar via navegador:**
   ```
   https://seu-dominio.com/compliance-manual/
   ```

### Opção 2: Hospedagem em GitHub Pages

1. **Criar repositório no GitHub:**
   ```bash
   git remote add origin https://github.com/universepharma/compliance-manual.git
   git branch -M main
   git push -u origin main
   ```

2. **Ativar GitHub Pages:**
   - Ir para Settings > Pages
   - Selecionar "main" como branch
   - Salvar

3. **Acessar via navegador:**
   ```
   https://universepharma.github.io/compliance-manual/
   ```

### Opção 3: Hospedagem em Serviço de CDN (Recomendado)

1. **Fazer upload para Cloudflare Pages, Vercel ou Netlify**
2. **Configurar domínio customizado**
3. **Ativar HTTPS automático**

---

## Estrutura de Arquivos

```
compliance-manual/
├── index.html              (Página principal - 50KB)
├── images/                 (Diretório de imagens)
│   ├── *.jpg              (Imagens em JPEG)
│   ├── *.png              (Imagens em PNG)
│   └── *.webp             (Imagens em WebP)
├── README.md              (Documentação do projeto)
├── DEPLOYMENT.md          (Este arquivo)
├── .htaccess              (Configuração Apache)
└── .git/                  (Repositório Git)
```

## Tamanho Total

- **HTML:** ~50 KB
- **Imagens:** ~3.3 MB
- **Total:** ~3.4 MB

## Performance

- Tempo de carregamento: < 2 segundos (com cache)
- Compatibilidade: Todos os navegadores modernos
- Responsividade: Desktop, Tablet, Mobile

## Segurança

- Sem vulnerabilidades de injeção SQL (sem banco de dados)
- Sem vulnerabilidades de XSS (conteúdo estático)
- HTTPS recomendado para transmissão segura
- Sem dados sensíveis armazenados no cliente

## Manutenção

### Atualizar o Manual

1. **Editar index.html** localmente
2. **Testar em navegador**
3. **Fazer commit:**
   ```bash
   git add -A
   git commit -m "Descrição da atualização"
   git push origin main
   ```
4. **Site será atualizado automaticamente** (se usando GitHub Pages ou CDN)

### Adicionar Novas Imagens

1. **Colocar imagens em `/images/`**
2. **Referenciar no HTML:**
   ```html
   <img src="images/nome-da-imagem.jpg" alt="Descrição">
   ```
3. **Fazer commit e push**

## Monitoramento

- Verificar acesso regularmente
- Monitorar tempo de carregamento
- Revisar logs de erro (se disponível)
- Atualizar conteúdo conforme novas políticas da Meta/ANVISA

## Backup

O repositório Git serve como backup automático. Para backup adicional:

```bash
# Fazer backup local
tar -czf compliance-manual-backup-$(date +%Y%m%d).tar.gz /home/ubuntu/universe_pharma_compliance_manual/

# Fazer backup em nuvem
aws s3 cp compliance-manual-backup-*.tar.gz s3://seu-bucket/backups/
```

## Suporte

Para dúvidas sobre implantação, contate:
- **Equipe de TI:** ti@universepharma.com.br
- **Equipe de Conformidade:** conformidade@universepharma.com.br
- **MFDireitoDigital:** mfdireitodigital@universepharma.com.br

---

**Última Atualização:** Novembro de 2025  
**Status:** Pronto para Implantação Permanente
