# Plano de validação — Mapas e planos de acesso

## Modelo de dados
Morada, coordenadas, imagem de mapa, ligação de itinerário.

## Implementação esperada
Preferir uma imagem de mapa estática com ligação para o itinerário; um mapa interativo de terceiros depende da política de conteúdo nativa.

## Testes a prever
1. Nominal: Verificar imagem, texto alternativo e ligação de itinerário em dispositivo móvel.
2. Controlo de recusa: Nenhum pedido a um serviço de mapas no carregamento da página.
3. Invariante: Nenhum mapa de terceiros carregado antes de uma ação do visitante.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
