# Plano de validação — Variantes e atributos

## Modelo de dados
Produto-pai, variantes com SKU único, combinações de atributos, preço/stock próprios, multimédia e estado.

## Implementação esperada
Definir o número máximo de combinações; garantir a unicidade do SKU; projetar as variantes na apresentação GET; preparar uma seleção validada no servidor no momento do checkout.

## Testes a prever
1. Nominal: Testar variantes ausentes, esgotadas e desativadas.
2. Controlo de recusa: Duas combinações criam o mesmo SKU => recusa explícita antes da publicação.
3. Invariante: Nunca aceitar preço, peso ou stock enviados pelo navegador como dados fiáveis.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
