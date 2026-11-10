# Plano de validação — Equipa

## Modelo de dados
Pessoa, função, fotografia, biografia curta.

## Implementação esperada
Utilizar o bloco de equipa nativo com fotografias homogéneas e textos fornecidos pelas próprias pessoas.

## Testes a prever
1. Nominal: Apresentar a equipa num dispositivo móvel com textos alternativos corretos.
2. Controlo de recusa: Uma pessoa retirada desaparece também das páginas em cache.
3. Invariante: Nenhuma fotografia ou informação é publicada sem o consentimento da pessoa.
4. GET/HEAD: cache pública apenas sem estado de sessão nem dados sensíveis; canonical, estado HTTP, SEO e GEO inalterados ou melhorados.
5. POST: nunca cache partilhada; CSRF, TLS, permissões, limitação das tentativas, idempotência. Não executar se o núcleo não o suportar oficialmente.
6. Ativação e desativação: os conteúdos são conservados e as rotas públicas retiradas sem fugas.
7. Controlos: validador nativo, testes PHP e HTTP, orçamentos; registar os comandos lançados, os seus resultados e o que não foi testado.

## Prova de disponibilidade
Estado da funcionalidade ou da extensão, registos de CI, matriz dos testes, procedimento de reversão e recusa de qualquer promessa não verificada.
