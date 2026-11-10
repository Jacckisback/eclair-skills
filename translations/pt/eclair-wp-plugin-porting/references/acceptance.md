# Plano de validação — Portabilidade de extensões WordPress

## Modelo de dados
Extensão de origem, funcionalidades realmente utilizadas, equivalente nativo, desvio.

## Implementação esperada
Listar o que a extensão faz realmente no site, procurar primeiro a funcionalidade nativa, caso contrário o skill do catálogo, caso contrário uma extensão à medida; nunca copiar código PHP WordPress.

## Testes a prever
1. Nominal: Elaborar a tabela de correspondência de um site real e fazê-la validar.
2. Controlo de recusa: Uma funcionalidade sem equivalente é anunciada como em falta, não simulada.
3. Invariante: Nenhum código sob licença incompatível ou dependente da API WordPress é reaproveitado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
