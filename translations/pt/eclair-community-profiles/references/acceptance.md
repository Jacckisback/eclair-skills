# Plano de validação — Perfis de comunidade

## Modelo de dados
Pseudónimo único, avatar, preferências de visibilidade, reputação e papéis.

## Implementação esperada
Distinguir ID interno e pseudónimo; impor limites e moderação do avatar; expor unicamente campos consentidos; gerir mudanças de nome e redirecionamentos seguros.

## Testes a prever
1. Nominal: Testar colisão de pseudónimos e eliminação de conta.
2. Controlo de recusa: Um visitante não consegue inferir um email através de uma mensagem de erro ou de uma API de perfil.
3. Invariante: Email, sessão, IP, morada e informações de recuperação permanecem privados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
