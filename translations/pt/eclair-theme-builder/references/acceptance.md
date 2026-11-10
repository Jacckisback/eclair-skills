# Plano de validação — Criação de tema

## Modelo de dados
theme.json, estilos, assets, templates declarados, licença e proveniência.

## Implementação esperada
Partir do tema de exemplo oficial, usar as variáveis e os modelos suportados, testar a preview e depois o ZIP, verificar a compatibilidade de versão.

## Testes a prever
1. Nominal: Testar o validador de tema, a ativação, a pré-visualização e a reversão.
2. Controlo de recusa: Um template defeituoso não torna o site inacessível, graças ao recurso previsto.
3. Invariante: Nunca refazer o SEO head e o canonical nem tocar nos ficheiros do núcleo.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
