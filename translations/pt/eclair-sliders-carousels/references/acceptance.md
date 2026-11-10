# Plano de validação — Diaporamas e carrosséis

## Modelo de dados
Diapositivo, imagem, texto, ligação, ordem.

## Implementação esperada
Preferir uma única imagem forte; caso contrário, deslocamento em CSS com comandos de teclado, pausa e nenhuma reprodução automática imposta.

## Testes a prever
1. Nominal: Navegar com o teclado e com o leitor de ecrã, medir o deslocamento da disposição.
2. Controlo de recusa: Sem JavaScript, todo o conteúdo dos diapositivos permanece legível.
3. Invariante: Nenhuma biblioteca de terceiros pesada; respeito por prefers-reduced-motion.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
