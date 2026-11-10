# Plano de validação — Contas de cliente

## Modelo de dados
Cliente, credenciais, encomendas, moradas.

## Implementação esperada
Definir registo, início de sessão, recuperação e eliminação de conta; separar estritamente contas de cliente e contas de administração.

## Testes a prever
1. Nominal: Simular registo, início de sessão, consulta e eliminação da conta.
2. Controlo de recusa: Um cliente não consegue ler a encomenda de outro alterando um identificador.
3. Invariante: Um cliente só vê os seus próprios dados; nunca cache partilhada na área de cliente.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
