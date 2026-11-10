# Éclair Member Directory — v1.0 reference

Um demonstrador nativo Éclair 2.0 é fornecido em `examples/extensions/member-directory/` na raiz da distribuição de origem; não é incluído na cópia autónoma do skill.

- `schema`: `eclair-extension/1`; `requires.eclair`: `>=2.0.0`.
- Rotas `admin`: GET raiz, POST `/create`, POST `/disable`; permissão `users`.
- Nenhuma rota pública. Nenhum login público e nenhum e-mail de validação é enviado.
- `Store`: chaves `ext/member-directory/...`, escrita sob bloqueio, limite de 1 000 membros a título experimental.
- Sessão de membro distinta das sessões da administração, token opaco de 256 bits com hash em repouso, revogação por epoch.
- Ativação após prova de e-mail: não fornecida pela superfície HTTP. Um papel de membro não pode ser `admin` ou `editor`.
- Instalador: copiar a extensão para `site/extensions/member-directory`, passar o `tools/validate.php` do núcleo 2.0, importar e ativar manualmente apenas em laboratório.
- Para contas ativas destinadas ao público: RFC para POST público seguro, validação de e-mail, rate limiting, fluxo de reset e testes nativos. Nenhuma rota GET deve criar/modificar uma conta ou uma sessão.
