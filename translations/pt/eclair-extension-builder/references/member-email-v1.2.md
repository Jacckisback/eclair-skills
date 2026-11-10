# Referência técnica — Member Directory v0.3.0 (Éclair v2.0.0, contrato POST experimental)

## Percursos disponíveis (todos cache:false)

| Método | Rota | Função |
|---|---|---|
| GET/POST | `/membres/connexion` | Formulário / início de sessão de uma conta ativa |
| GET | `/membres/espace` | Perfil privado próprio do token de sessão |
| POST | `/membres/deconnexion` | Fim de sessão com CSRF próprio da sessão |
| GET/POST | `/membres/inscription` | E-mail de convite, apenas se `registration_enabled=true` |
| GET/POST | `/membres/verification` | Escolher a palavra-passe com prova de e-mail única |
| GET/POST | `/membres/recuperation` | Pedir um e-mail de recuperação se `recovery_enabled=true` |
| GET/POST | `/membres/reinitialisation` | Substituir a palavra-passe com prova única |

## Mecanismos

- Sem conta CMS/`Auth::can` para os clientes. Os perfis `member` nunca contêm papéis `admin` ou `editor`.
- `MemberAccounts::provision` exige uma palavra-passe provisória aleatória e cria uma conta `pending`. A ligação enviada por e-mail pede à pessoa que escolha a sua própria palavra-passe. O token de verificação expira em 30 minutos e um recibo só se utiliza uma vez.
- `MemberAccounts::issueReset` emite apenas para um membro `active`, depois `confirmReset` efetua a mutação sob bloqueio e incrementa `epoch`. Todos os antigos tokens de sessão ficam inválidos.
- `Mail::send` (serviço Éclair) é utilizado, mas não é um aviso de entrega. Não prometer ao utilizador nenhum êxito de entrega.
- Para enviar um e-mail, o URL canónico configurado deve ser HTTPS e estar verificado. O domínio do pedido HTTP é excluído da ligação de recuperação.
- As páginas GET não efetuam nenhum processamento de negócio; o POST exige HTTPS e `Security::checkFormToken`, verificando o patch do núcleo também essas condições.
- Limitadores por rede / e-mail, mensagens genéricas nos pedidos, provas validadas duas vezes (preflight antes do hash, depois sob bloqueio de armazenamento).
- Nenhum recurso pessoal passa pela cache estática pública. As ligações com token devem ser excluídas dos registos e de qualquer página externa carregada a partir dos formulários de confirmação.

## Limites explícitos

- Uma conta pendente cujo e-mail é aceite pelo transporte mas nunca recebido necessita de um percurso de novo convite/assistência, não fornecido aqui.
- As mensagens genéricas não eliminam totalmente a possibilidade de inferir a existência de uma conta pelo tempo de execução.
- Os tokens de e-mail em URL podem aparecer no histórico do navegador ou em logs: auditoria da infraestrutura obrigatória.
- O protótipo `Store` está limitado a 1 000 membros e não é uma base relacional transacional multificheiro.
- O contrato `eclair-extension/1` oficial **não** autoriza POST público sem patch. Qualquer instalação num site real aguarda a sua validação.
