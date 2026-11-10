# Plano de validação — Pré-produção e colocação online

## Modelo de dados
Cópia de teste, diferenças, lista de verificação de colocação online.

## Implementação esperada
Restaurar uma cópia de segurança num subdomínio protegido e não indexável, validar aí tema e funcionalidades, depois reproduzir em produção.

## Testes a prever
1. Nominal: Percorrer uma mudança de tema da cópia até à produção.
2. Controlo de recusa: A cópia de teste não é indexada nem acessível sem autenticação.
3. Invariante: A cópia de teste está protegida por palavra-passe e bloqueada aos robôs.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
