# Éclair CMS 2.0.x — mapa do núcleo verificado

Referência: repositório público `Jacckisback/eclair-cms`, ramo `main` verificado a 9 de novembro de 2026, commit de referência `6567d7642ea2227a598c4988e970d43e2e5e0e4f`. **Um agente deve sempre voltar a verificar o checkout real e `GET /<admin>/api/capabilities`**: esta nota é um instantâneo, não uma garantia de compatibilidade futura.

## 1. Já integrado no núcleo: configurar, não reconstruir

Antes de escrever a mais pequena extensão, verificar se a necessidade está coberta nativamente:

- **Conteúdos**: páginas e artigos em blocos, categorias, menus, autores, rascunhos, planeamento editorial; blocos `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Média**: imagens redimensionadas, recodificadas e convertidas em WebP responsivo, dimensões explícitas, carregamento diferido.
- **Formulário de contacto** e caixa de entrada das mensagens (permissão `messages`).
- **SEO e GEO**: títulos e descrições com análise em direto, JSON-LD (organização ou empresa local, artigo, FAQ, trilho de navegação), sitemap com imagens e `hreflang`, feed RSS, Open Graph com imagem de partilha, redirecionamentos 301 e gestor de redirecionamentos, IndexNow, `llms.txt`, versão Markdown de cada página, política para os robôs de IA.
- **Velocidade**: cache estática de cada página pública, CSS integrado, um único script público, nenhum cookie público.
- **Segurança**: autenticação de dois fatores, limites de tentativas, Content-Security-Policy estrita, conteúdos sanitizados, controlo de integridade, registo de atividade, atualizações assinadas com reversão.
- **Cópias de segurança**: descarregamento e envio agendado para um armazenamento remoto, restauro.
- **Loja leve**: fichas de produto, variantes, categorias, ligações de pagamento de um prestador, feed de comerciante; **sem carrinho, sem encomenda e sem conta de cliente**.
- **Funcionalidades entregues**: afiliação, publicidade, planeamento, importação WordPress, retoma de um site antigo, acompanhamento dos robôs de IA.
- **Assistente de IA e conector MCP**: apenas rascunhos e propostas, nunca publicação nem eliminação.
- **Aparência**: temas e direções artísticas, pré-visualização antes de guardar.

## 2. Onde um skill pode escrever

- Código do núcleo: `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **nunca editar** para entregar uma funcionalidade de site.
- Extensões do site: `site/extensions/<id>/` com `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Temas do site: `site/themes/<id>/` com `theme.json`.
- Dados de uma extensão: `Eclair\Store`, prefixo `$ctx['data']` (`data/ext/<id>/`), segredos em `data/ext/<id>/secrets.php`.
- Conteúdos e definições: apenas através da administração ou do conector MCP.

## 3. Contrato `eclair-extension/1`

- Rotas públicas de uma extensão: **apenas GET**, declaradas no manifesto, colocáveis em cache ou não.
- Administração: GET/POST sob `/<admin>/x/<id>/...`, permissões do núcleo (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) e proteção CSRF.
- Blocos e definições declarativos validados pelo núcleo; tarefas agendadas (no máximo uma vez por hora); migrações idempotentes; recursos publicados.
- O código de uma extensão é **de confiança, sem sandbox**: a importação e a ativação exigem uma pessoa autorizada.
- Validação: `php tools/validate.php <dossier> --json`, depois `php tests/run.php` e `php tools/measure.php --check` num checkout do núcleo.

## 4. Limites conhecidos da 2.0

- Sem rota POST pública para as extensões (PR #19 em rascunho, não fundida), logo sem inscrição, comentário, encomenda ou envio de ficheiros por um visitante fora do formulário de contacto nativo.
- Sem identidade pública (cliente, aluno, membro) no contrato nativo.
- Sem tipo de conteúdo próprio de uma extensão; sem contribuição SEO ou JSON-LD por extensão; sem política de conteúdo (CSP) por extensão; sem filtro geral de renderização.
- Etiquetas, comentários e tipos de conteúdo personalizados do WordPress não são retomados pela importação.
- Os antigos protótipos Éclair Devkit v0.x visavam o núcleo 1.14 e **não se aplicam** à 2.0.

Fontes oficiais:
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
