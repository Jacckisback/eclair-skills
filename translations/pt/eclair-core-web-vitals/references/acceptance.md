# Plano de validação — Sinais web essenciais

## Modelo de dados
Apresentação do maior elemento, estabilidade, reatividade, por modelo de página.

## Implementação esperada
Medir em laboratório e com dados reais quando existirem, tratar a causa principal por modelo de página, voltar a medir.

## Testes a prever
1. Nominal: Medir três modelos de página em dispositivo móvel antes e depois da correção.
2. Controlo de recusa: Uma melhoria não medida não é anunciada como adquirida.
3. Invariante: Nenhuma pontuação é prometida; apenas os resultados medidos são reportados.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
