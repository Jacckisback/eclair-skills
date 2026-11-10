# Plano de validação — GEO e agentes de IA

## Modelo de dados
Conteúdo verificável, proveniência, semântica, llms.txt, Markdown, Schema.org.

## Implementação esperada
Auditar a estrutura, as respostas factuais, as fontes e a coerência do Markdown; controlar os robots de IA sem promessas excessivas.

## Testes a prever
1. Nominal: Testar a versão Markdown, as citações estruturadas e o robots.txt.
2. Controlo de recusa: Os factos apresentados a robots e a humanos permanecem coerentes e atualizados.
3. Invariante: Não confundir pontuação GEO interna, citabilidade e posicionamento garantido.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
