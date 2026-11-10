# Plano de validação — Páginas de erro

## Modelo de dados
Página de erro, ligações úteis, registo dos endereços não encontrados.

## Implementação esperada
Compor uma página 404 útil no tema do site, propor a página inicial e páginas-chave, tratar os 404 frequentes por redirecionamento.

## Testes a prever
1. Nominal: Pedir um endereço inexistente e verificar estado 404 e conteúdo.
2. Controlo de recusa: Uma página não encontrada nunca responde com um estado 200.
3. Invariante: A página de erro não apresenta nenhum rasto técnico.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
