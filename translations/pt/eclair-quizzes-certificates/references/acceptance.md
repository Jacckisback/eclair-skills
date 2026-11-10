# Plano de validação — Questionários e certificados

## Modelo de dados
Pergunta, opção, correção, tentativa, pontuação, prazo, certificado e verificação.

## Implementação esperada
Versionar banco de perguntas; classificar do lado do servidor; definir tentativas e tempo; gerar certificado assinado/verificável sem PII pública.

## Testes a prever
1. Nominal: Testar fraude, fim de sessão, validação do certificado.
2. Controlo de recusa: Submeter duas vezes uma tentativa não deve gerar dois certificados.
3. Invariante: Nunca enviar a correção ou a resposta certa no HTML de uma prova ativa.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
