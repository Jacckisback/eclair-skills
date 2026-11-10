# Plano de validação — Ofertas de emprego

## Modelo de dados
Oferta, empresa, estado, prazo, candidatura e anexos.

## Implementação esperada
Construir filtros públicos, expiração automática, formulários seguros e ciclo de retenção das candidaturas.

## Testes a prever
1. Nominal: Testar anúncio expirado, spam e exportação do candidato.
2. Controlo de recusa: Um recrutador não consegue ler uma candidatura destinada a outra empresa.
3. Invariante: CV e anexos nunca são colocados num diretório web acessível.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
