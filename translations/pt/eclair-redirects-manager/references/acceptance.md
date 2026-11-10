# Plano de validação — Redirecionamentos

## Modelo de dados
Endereço antigo, endereço novo, tipo, data.

## Implementação esperada
Importar os endereços antigos, criar um redirecionamento direto por endereço, eliminar cadeias e ciclos.

## Testes a prever
1. Nominal: Testar um lote de endereços antigos e registar o estado e o destino.
2. Controlo de recusa: Nenhuma cadeia com mais de um salto nem ciclo.
3. Invariante: Nenhum redirecionamento aberto para um domínio não pretendido.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
