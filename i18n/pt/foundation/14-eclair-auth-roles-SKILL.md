---
name: eclair-auth-roles
description: Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles.
---

# Éclair Auth & Roles — distinguir admin e membros

## Realidade v2
`Eclair\Auth` e `Users` controlam **a administração** com as suas permissões (`content`, `settings`, `security`, etc.). Não são um diretório de clientes, alunos ou membros, e não devem ser desviados para papéis `customer/student`.

## Procedimento
1. Consultar `Users`, `Auth`, `Admin`, `Security`, `Session`, `RateLimit` e a permissão pedida por cada rota admin `eclair-extension/1`.
2. Para uma funcionalidade de administração, declarar `routes.admin[]` com `right` exato e apoiar-se na verificação CSRF do núcleo. Verificar o acesso segundo cada papel existente.
3. Para uma área pública de clientes/alunos: produzir uma RFC de fornecedor de identidade ou um componente de servidor dedicado e auditado com armazenamento adequado; **não** expor as rotas sensíveis via GET público.
4. Definir a sessão de membro independente, os cookies `Secure/HttpOnly/SameSite`, as autenticações progressivas, rate limiting, recuperação e verificação de e-mail.
5. Permissões: identificar sistematicamente o sujeito através de uma sessão de servidor verificada, depois controlar o objeto e o âmbito (IDOR/BOLA) em cada pedido.
6. Testar ausência de privilégios herdados do admin, mudança de papel, revogação, reset, corridas de sessões, acesso entre contas, CSRF e recusa por omissão.

## Demonstrador nativo v1.0
A extensão `examples/extensions/member-directory/` fornece um exemplo **apenas admin** para o Éclair 2.0:
- `routes.admin`: GET + POST (`users`) com controlos reforçados nos handlers; `routes.public`: array vazio.
- `MemberAccounts` e `MemberSessions` permanecem independentes de `Eclair\Users/Auth/Session`; conta `pending` obrigatória no provisionamento.
- Os dados residem exclusivamente sob `data/ext/member-directory/` via `Store`. Nunca em `data/users.php`.
- `MemberPermissions::allows` recebe um token de sessão verificado, não uma identidade fornecida pelo chamador.
- Nem registo público, nem e-mail enviado, nem recuperação de palavra-passe, nem gestão real das sessões HTTP está ativada.
- A API POST pública necessita de uma RFC/novo contrato do núcleo e de uma validação de ponta a ponta antes da implantação.
Ler `references/member-directory-v1.md` antes de construir um LMS, fórum ou comércio.

## Entregáveis
Matriz de permissões e recursos, modelo de ameaças, plano de identidade, conjuntos de testes e indicação «native / RFC necessária».

## Éclair 2.0 — protótipo v1.1 (experimental)
O protótipo v1.1 possui handlers públicos GET formulário + POST início/fim de sessão + GET área privada. Só são válidos após a adição aprovada do contrato POST. Sessões de membros distintas das dos admins, token opaco, CSRF double-submit e CSRF de sessão no fim de sessão; nenhum papel admin/editor concedido.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
