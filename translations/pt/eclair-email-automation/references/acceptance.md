# Plano de validação — Emails transacionais

## Modelo de dados
Template, língua, consentimento, destinatário, domínio, evento, entrega.

## Implementação esperada
Preparar modelos texto/HTML, DKIM/SPF/DMARC e entregabilidade; distinguir transacional e marketing, registo sem segredos, cancelamento da subscrição obrigatório.

## Testes a prever
1. Nominal: Testar erro SMTP, erro de endereço, retoma e expiração de token.
2. Controlo de recusa: Uma falha SMTP não marca um email como entregue nem bloqueia uma conta definitivamente.
3. Invariante: Não enviar token de recuperação por URL não verificado; nunca spam sem consentimento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
