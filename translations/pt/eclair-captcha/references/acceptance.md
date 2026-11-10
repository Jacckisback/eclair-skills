# Plano de validação — Captcha

## Modelo de dados
Desafio, token, verificação no servidor.

## Implementação esperada
Preferir campo armadilha e limites nativos; um captcha de terceiros exige uma abertura da política de conteúdo que o núcleo não delega nas extensões.

## Testes a prever
1. Nominal: Verificar que a proteção escolhida bloqueia um envio automatizado.
2. Controlo de recusa: Nenhum script de captcha é carregado nas páginas sem formulário.
3. Invariante: Nunca enfraquecer a Content-Security-Policy do site para carregar um script de terceiros.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
