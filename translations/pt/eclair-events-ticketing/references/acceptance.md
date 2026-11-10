# Plano de validação — Eventos e bilhetes

## Modelo de dados
Evento, sessão, tipo de lugar, reserva, bilhete, leitura, reembolso.

## Implementação esperada
Separar quotas por sessão; emitir bilhetes únicos após pagamento confirmado; gerir controlo de entrada atómico e transferência.

## Testes a prever
1. Nominal: Testar leitura dupla, cancelamento e último bilhete em simultâneo.
2. Controlo de recusa: Mesmo bilhete apresentado em duas portas => uma única admissão aceite.
3. Invariante: O código QR não contém dados pessoais em claro e não autoriza várias entradas.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
