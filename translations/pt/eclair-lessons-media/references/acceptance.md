# Plano de validação — Média pedagógicos

## Modelo de dados
Lição, média, transcrição, ficheiros descarregáveis, direitos e duração.

## Implementação esperada
Preparar média e legendas acessíveis; prever distribuição com autorização do lado do servidor ou URL assinado de curta duração; separar CDN público e conteúdo reservado.

## Testes a prever
1. Nominal: Testar média expirado, acesso sem inscrição e dispositivo móvel.
2. Controlo de recusa: Um URL de documento privado copiado para outro navegador é recusado ou expira.
3. Invariante: Ocultar uma ligação no HTML não é uma proteção; não colocar o média privado em /media público.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
