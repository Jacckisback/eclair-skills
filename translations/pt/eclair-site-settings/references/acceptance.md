# Plano de validação — Definições do site

## Modelo de dados
Nome, descrição, logótipo, contactos, língua, tema, direção artística.

## Implementação esperada
Ler as capacidades do site, preencher as definições pela administração, pré-visualizar antes de guardar.

## Testes a prever
1. Nominal: Configurar um site novo e verificar a apresentação pública.
2. Controlo de recusa: Uma conta sem o direito Definições não modifica nenhuma definição.
3. Invariante: Nenhuma proteção nativa é desativada para ganhar tempo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
