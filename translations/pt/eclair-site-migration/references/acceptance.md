# Plano de validação — Mudança de alojamento ou de domínio

## Modelo de dados
Cópia de segurança, novo alojamento, DNS, redirecionamentos de domínio.

## Implementação esperada
Fazer cópia de segurança, restaurar no novo fornecedor de alojamento, verificar, comutar o DNS, redirecionar o domínio antigo página a página.

## Testes a prever
1. Nominal: Ensaiar a mudança num domínio de teste.
2. Controlo de recusa: Nenhum endereço antigo responde com 404 após a comutação.
3. Invariante: Os segredos do site nunca viajam por e-mail ou serviço de mensagens.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
