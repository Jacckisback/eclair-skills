# Plano de validação — Site de profissão liberal

## Modelo de dados
Serviço, profissional, honorários indicativos, contacto.

## Implementação esperada
Apresentar áreas de intervenção e percursos reais, respeitar as regras de comunicação da profissão, propor contacto ou marcação.

## Testes a prever
1. Nominal: Fazer rever os conteúdos pelo profissional.
2. Controlo de recusa: Uma especialidade não reconhecida não é apresentada como título.
3. Invariante: Nenhuma promessa de resultado nem menção proibida pela deontologia da profissão.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
