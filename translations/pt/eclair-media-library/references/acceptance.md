# Plano de validação — Biblioteca multimédia

## Modelo de dados
Ficheiro, texto alternativo, dimensões, utilizações.

## Implementação esperada
Importar os ficheiros multimédia, preencher os textos alternativos, identificar os ficheiros não utilizados e os duplicados.

## Testes a prever
1. Nominal: Enviar vários formatos e verificar a conversão, as dimensões e os textos alternativos.
2. Controlo de recusa: Um ficheiro em formato proibido ou armadilhado é recusado no envio.
3. Invariante: Só são enviados os formatos aceites pelo núcleo; nenhum ficheiro executável.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
