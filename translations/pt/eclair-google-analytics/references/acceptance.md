# Plano de validação — Google Analytics

## Modelo de dados
Identificador de medição, consentimento, eventos.

## Implementação esperada
Verificar primeiro se uma medição sem cookies é suficiente; caso contrário, consentimento prévio, e constatação de que a política de conteúdo nativa não está aberta às extensões.

## Testes a prever
1. Nominal: Verificar a ausência de pedidos antes do consentimento.
2. Controlo de recusa: Após recusa, nenhum dado é enviado.
3. Invariante: Nenhum script de medição carregado antes do consentimento nem contornando a Content-Security-Policy.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
