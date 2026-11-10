# Plano de validação — Cópias de segurança e restauro

## Modelo de dados
Arquivo de cópia de segurança, data, destino, teste de restauro.

## Implementação esperada
Ativar a cópia de segurança descarregável ou para o armazenamento remoto previsto pelo núcleo, fixar a frequência, restaurar numa cópia para verificar.

## Testes a prever
1. Nominal: Restaurar a última cópia de segurança numa instalação de teste e comparar.
2. Controlo de recusa: Um arquivo modificado ou armadilhado é recusado no restauro.
3. Invariante: Uma cópia de segurança contém dados pessoais: é armazenada cifrada ou em local seguro, nunca numa pasta pública.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
