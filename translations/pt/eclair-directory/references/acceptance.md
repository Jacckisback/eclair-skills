# Plano de validação — Diretório profissional

## Modelo de dados
Ficha, categoria, localização, contacto público, estado de verificação.

## Implementação esperada
Separar dados profissionais públicos e privados; criar páginas de categoria, canonical, moderação e filtros limitados.

## Testes a prever
1. Nominal: Testar fichas falsas, duplicados, eliminação e pesquisa vazia.
2. Controlo de recusa: Uma ficha pendente não aparece nem no sitemap nem nos dados estruturados.
3. Invariante: Não publicar morada pessoal, telefone ou contactos sensíveis sem autorização.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
