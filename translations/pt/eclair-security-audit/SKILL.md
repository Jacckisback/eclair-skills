---
name: eclair-security-audit
description: Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security.
---

# Éclair Security Audit — revisão antes da ativação

## Perímetro
1. Estabelecer a versão do núcleo, a proveniência da extensão, os ficheiros executáveis e as permissões reclamadas.
2. Exigir o contrato `extension.json` conforme e hashes SHA-256 para os ficheiros; verificar symlinks, caminhos com travessia de diretórios, scripts imprevistos, ZIP bombs, tamanhos, métodos e rotas reservadas.
3. Controlar separadamente o `right` nativo de rota admin e as autorizações de negócio sobre os objetos; uma permissão `content` não autoriza a ler a encomenda de outro cliente.
4. Testar CSRF, rate limiting, session fixation, acesso direto aos ficheiros, XSS no HTML devolvido, injeção SQL, SSRF dos URL externos e gestão dos segredos.
5. Páginas públicas com `cache:true`: ausência de dados pessoais e de variantes por utilizador. Páginas admin: headers, autenticação e recusa por omissão.
6. Para um checkout: webhook assinado com verificação de servidor, idempotência, montantes, moeda, IVA e transições de estado transacionais antes da entrega.
7. Para eventos de negócio: recordar que a v2 não integra bus/outbox padrão; projeto separado com testes de falha e nenhuma promessa de exactly-once para efeitos remotos.
8. Nunca executar módulos não auditados com a confiança do processo PHP.

## Provas mínimas
`php tools/validate.php chemin/extension --json`, `php tests/run.php`, `php tools/measure.php --check` e cenários negativos HTTP numa instalação de teste. Nenhum relatório de segurança é uma certificação automática.

## Entregáveis
Lista de riscos classificados, demonstrações reproduzíveis, correções, limites restantes e decisão explícita Go/No-Go.

## V1.0 — Testes da identidade
Auditar o protótipo `member-directory`: nenhuma conta de membro em `data/users.php`, palavra-passe nunca restituída, estado `pending` por omissão, papéis `admin/editor` proibidos, epoch de revogação, controlo de objeto próprio/alheio, cookie `__Host-` HTTPS. Os testes locais não valem como auditoria em produção.

## Éclair 2.0 — protótipo v1.1 (experimental)
O protótipo v1.1 tem uma limitação `RateLimit::attempt` antes do hash, uma separação estrita membros/admin e tokens de sessão de 256 bits. Avaliar a segurança dos `Origin`, de TLS atrás de reverse proxy, CSRF, IDOR, enumeração de contas, fugas de informação e concorrência. Não confundir testes isolados com auditoria em produção.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
