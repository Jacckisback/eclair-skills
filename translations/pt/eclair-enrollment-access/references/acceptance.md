# Plano de validação — Inscrições nos cursos

## Modelo de dados
Membro, curso, inscrição, estado, origem, data e revogação.

## Implementação esperada
Criar inscrição idempotente; tratar direitos por objeto; distinguir inscrição gratuita/paga; revogar após reembolso segundo regra explícita.

## Testes a prever
1. Nominal: Testar compra duplicada, reembolso, suspensão da conta.
2. Controlo de recusa: Um membro excluído já não consegue aceder às lições anteriormente autorizadas.
3. Invariante: Nunca inscrição automática com base num simples URL de retorno do prestador de pagamento.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
