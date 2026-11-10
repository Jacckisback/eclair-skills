# Plano de validação — Sincronização CRM

## Modelo de dados
Contacto, empresa, consentimento, mapping, chave externa, proveniência.

## Implementação esperada
Mapear campos estritos, diferenciar atualizações direcionais e fusão, fornecer reconciliação e exportação/eliminação.

## Testes a prever
1. Nominal: Testar fusão, email alterado, conflito, eliminação e retoma.
2. Controlo de recusa: O mesmo contacto ressincronizado não cria vários duplicados no CRM.
3. Invariante: Não exportar contactos sem base legal nem scopes mínimos.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
