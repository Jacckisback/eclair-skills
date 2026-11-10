# Plano de validação — Observabilidade e alertas

## Modelo de dados
Logs estruturados, erros, correlações, métricas, traces, retenção.

## Implementação esperada
Definir alertas úteis, anonimizar dados, vigiar tarefas e cache, distinguir incidente do site e do módulo, fornecer runbook.

## Testes a prever
1. Nominal: Testar aumento de erros 5xx, atraso das tarefas e disco cheio.
2. Controlo de recusa: Um módulo desativado não continua a enviar dados nem a executar tarefas.
3. Invariante: Nenhuma palavra-passe, token, pagamento ou PII em bruto nos logs; nenhuma telemetria oculta.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
