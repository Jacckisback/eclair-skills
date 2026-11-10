# Plano de validação — SEO local

## Modelo de dados
Nome, morada, telefone, horários, zona servida.

## Implementação esperada
Preencher os contactos exatos nas definições, verificar a marcação de empresa local produzida pelo núcleo, alinhar a ficha do estabelecimento com o site.

## Testes a prever
1. Nominal: Comparar os contactos do site, da marcação e da ficha do estabelecimento.
2. Controlo de recusa: Horários não confirmados não são publicados.
3. Invariante: Nenhuma morada, avaliação ou zona de intervenção inventadas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
