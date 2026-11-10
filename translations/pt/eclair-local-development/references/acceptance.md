# Plano de validação — Desenvolvimento local

## Modelo de dados
Versão de PHP, servidor web, cópia do site, dados de teste.

## Implementação esperada
Instalar a mesma versão de PHP e as mesmas regras de servidor, restaurar uma cópia de segurança anonimizada, lançar os testes.

## Testes a prever
1. Nominal: Iniciar o site local e fazer passar a suite de testes.
2. Controlo de recusa: Uma cópia local não envia nenhum e-mail real.
3. Invariante: Os dados reais de clientes não são copiados para o ambiente local sem anonimização.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
