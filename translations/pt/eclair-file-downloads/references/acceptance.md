# Plano de validação — Transferências

## Modelo de dados
Ficheiro, título, versão, tamanho, página de suporte.

## Implementação esperada
Arrumar os ficheiros públicos na biblioteca multimédia, apresentar o peso e o formato, versionar os ficheiros substituídos.

## Testes a prever
1. Nominal: Transferir cada ficheiro e verificar o tipo e o tamanho anunciados.
2. Controlo de recusa: Um ficheiro substituído não deixa a versão antiga acessível por engano.
3. Invariante: Nenhum ficheiro privado ou pago é colocado num endereço público adivinhável.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
