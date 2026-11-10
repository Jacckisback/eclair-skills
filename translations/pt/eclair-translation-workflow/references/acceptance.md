# Plano de validação — Fluxo de tradução

## Modelo de dados
Conteúdo de origem, versão de destino, tradutor, estado, data de atualização.

## Implementação esperada
Manter um quadro dos conteúdos a traduzir, produzir as traduções em rascunho, pedir a revisão por um falante da língua, assinalar as versões desatualizadas.

## Testes a prever
1. Nominal: Traduzir uma página, pedir a sua revisão, publicar e, depois, modificar a origem e verificar a sinalização.
2. Controlo de recusa: Uma tradução não revista permanece em rascunho.
3. Invariante: Nenhuma tradução jurídica ou médica é publicada sem validação qualificada.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
