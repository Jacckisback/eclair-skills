---
name: eclair-email-campaigns
description: "Conceber campanhas de email a partir dos conteúdos do site. Use on Éclair CMS 2.x when the user wants to: conceber o envio de campanhas de e-mail a partir dos conteúdos do site. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Campanhas de e-mail — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **conceber o envio de campanhas de e-mail a partir dos conteúdos do site**. Esta funcionalidade **exige capacidades ausentes do núcleo 2.0**: o skill entrega conceção, maqueta segura e testes, não uma colocação em produção. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** MailPoet, Newsletter, FluentCRM. Família: Marketing e audiência.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Lista, segmento, campanha, envio, cancelamento da subscrição**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Confiar o envio a um serviço especializado, preparar os conteúdos a partir do site, definir segmentos, frequência e cancelamento da subscrição. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** Esta funcionalidade requer escritas de visitantes, contas públicas, transações ou eventos assinados que `eclair-extension/1` não fornece na 2.0. Entregar a conceção, uma maqueta GET segura e testes bloqueantes; nunca anunciar uma colocação em produção.
7. **Invariante de segurança:** Cada e-mail contém uma ligação funcional de cancelamento da subscrição; nenhuma lista comprada. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Enviar uma campanha de teste para uma lista interna» e o teste de recusa «Um endereço que cancelou a subscrição não recebe mais nada». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Dossiê de conceção, maqueta GET segura se for útil, testes bloqueantes e pedido de evolução do núcleo; **sem pacote de produção**.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Enviar uma campanha de teste para uma lista interna.
- Um endereço que cancelou a subscrição não recebe mais nada.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `design-workflow-requires-verified-core-capabilities`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
