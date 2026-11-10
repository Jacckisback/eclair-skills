# Plano de validação — Arquitetura LMS

## Modelo de dados
Cursos, secções, lições, pré-requisitos, inscrições, progresso, direitos e eventuais vendas.

## Implementação esperada
Definir catálogos públicos vs lições privadas; escolher um armazenamento de progresso transacional; ligar o acesso à identidade de membro validada; compor módulos independentes.

## Testes a prever
1. Nominal: Testar estudante, professor, administrador e visitante.
2. Controlo de recusa: Um aluno inscrito não consegue ler o conteúdo privado de outro curso.
3. Invariante: Nenhuma promessa de acesso privado através de um simples URL secreto ou de um bloco oculto.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
