# Plano de validação — Feeds de redes sociais

## Modelo de dados
Publicação, imagem, ligação, data de recolha.

## Implementação esperada
Recolher as publicações por tarefa agendada do lado do servidor quando a rede o autoriza, apresentá-las em HTML estático; caso contrário, simples ligações para os perfis.

## Testes a prever
1. Nominal: Verificar a apresentação estática e a atualização por tarefa.
2. Controlo de recusa: Se a rede estiver indisponível, a última versão válida continua a ser apresentada.
3. Invariante: Nenhum widget de terceiros é carregado no navegador dos visitantes.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
