# Plano de validação — Integridade dos ficheiros

## Modelo de dados
Ficheiro, impressão digital esperada, desvio.

## Implementação esperada
Lançar o controlo de integridade da página Segurança, explicar cada desvio, restaurar os ficheiros de origem se necessário.

## Testes a prever
1. Nominal: Modificar um ficheiro numa cópia de teste e constatar o alerta.
2. Controlo de recusa: Um ficheiro do núcleo alterado nunca é declarado conforme.
3. Invariante: Um desvio inexplicado é tratado como um incidente, não ignorado.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
