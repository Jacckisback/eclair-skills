---
name: eclair-extension-builder
description: Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract.
---

# Éclair Extension Builder — construir uma extensão realmente instalável na v2

## Objetivo
Criar um **pacote `eclair-extension/1` conforme ao núcleo v2**. Não utilizar o manifesto `manifest.json` nem os ficheiros `events.php` / `services.php` dos antigos protótipos como se fossem suportados.

## Processo
1. Ler `references/core-map.md`, `docs/EXTENSION-CONTRACT.md`, `docs/schemas/extension.schema.json` e `examples/extensions/bonjour` do checkout.
2. Verificar `ECLAIR_VERSION` e o contrato `eclair-extension/1` através do código e, se acessível, da API das capacidades.
3. Definir `id`, `version`, `requires`, `depends`, `provides`, `entry`, rotas, blocos, campos, assets, `tasks`, migrações; utilizar apenas os campos do esquema.
4. Entregar em `site/extensions/<id>/` **sem escrever em `app/`**; a entrada PHP deve devolver um objeto e não deve produzir nada durante o seu carregamento.
5. Controlar a apresentação com `e()`; ler as definições a partir de `$ctx['settings']`; armazenar via `Eclair\Store` sob `$ctx['data']`. Para os segredos: localização privada e política de não inclusão nas cópias de segurança documentada.
6. Rotas públicas apenas GET. Numa página pública que apresente um dado de sessão ou individual: paragem e pedido de novo contrato de identidade/cache; sem falsas soluções de contorno.
7. Calcular os SHA-256 dos ficheiros e declará-los em `files`, exceto `extension.json`. Gerar um pacote ZIP cuja raiz contenha o manifesto.
8. `php tools/validate.php chemin/extension --json`; corrigir todos os erros antes de propor a importação, depois testar `php tests/run.php` e `php tools/measure.php --check`.
9. Uma pessoa autorizada importa, pré-visualiza/controla, ativa; documentar a desativação, a eliminação de código e a conservação dos dados.

## Entregáveis
`extension.json`, entrada `extension.php`, referências, testes, prova de validação oficial e manual de instalação. Exemplo original em `examples/extensions/skill-sample/`; verificar no núcleo exato antes da implantação.

## V1.0 — Modelo avançado entregue
Consultar `examples/extensions/member-directory`: prova rotas admin GET/POST nativas e uma biblioteca PHP carregada apenas pela extensão. Não transformar o seu GET admin em início de sessão público nem acrescentar um POST a `routes.public` (contrato v2 incompatível).

## Éclair 2.0 — protótipo v1.1 (experimental)
Um protótipo de rota POST pública consta de `examples/extensions/member-directory/`. É rejeitado pelo núcleo 2.0 oficial. Utilizar o manifesto apenas com o patch experimental e o acordo explícito de um mantenedor, nunca em produção. POST exige `cache:false`, TLS, CSRF, redirecionamento relativo.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
