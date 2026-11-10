# Plano de validação — Autores e assinaturas

## Modelo de dados
Autor, biografia, função, ligações, conteúdos assinados.

## Implementação esperada
Completar os perfis reais, ligar cada artigo ao seu autor, verificar a página de autor e os dados estruturados produzidos pelo núcleo.

## Testes a prever
1. Nominal: Preencher um perfil e verificar a assinatura, a página de autor e a marcação.
2. Controlo de recusa: Uma conta desativada ou sem conteúdo publicado não expõe nenhuma página de autor.
3. Invariante: Nunca inventar um autor, um diploma ou uma experiência.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
