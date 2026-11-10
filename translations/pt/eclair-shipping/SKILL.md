---
name: eclair-shipping
description: "Gerir zonas, tarifas, rastreio e estados de entrega. Use on Éclair CMS 2.x when the user wants to: gerir as zonas, as tarifas, o seguimento e os estados de entrega. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Entrega e transporte — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **gerir as zonas, as tarifas, o seguimento e os estados de entrega**. Esta funcionalidade **exige capacidades ausentes do núcleo 2.0**: o skill entrega conceção, maqueta segura e testes, não uma colocação em produção. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** Zonas e métodos de envio do WooCommerce. Família: Commerce Pro.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Morada validada, zona, transportadora, volume, peso, serviço, custos, tracking**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Modelar zonas e incompatibilidades; calcular a estimativa de custos do lado do servidor; prever split shipments e entrega parcial; anonimizar os dados de expedição nos registos. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** O núcleo já fornece uma loja leve (fichas de produto, variantes, categorias, ligações de pagamento de um prestador, feed de comerciante): utilizá-la primeiro, sem a duplicar. Para além disso, carrinho, encomendas e pagamentos precisam de POST públicos, de um armazenamento transacional fiável, de webhooks autenticados e de idempotência; o Éclair 2.0 oficial não fornece tudo isso. A PR #19 ainda é um rascunho: nunca utilizar uma rota POST não fundida como prova de compatibilidade.
7. **Invariante de segurança:** A morada e o seguimento são privados; nenhum dado pessoal em cache pública, logs detalhados ou URLs. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Testar zona não servida, peso-limite, dois volumes e estado perdido» e o teste de recusa «Um número de seguimento de um cliente não deve ser visível a partir de outra conta». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Dossiê de conceção, maqueta GET segura se for útil, testes bloqueantes e pedido de evolução do núcleo; **sem pacote de produção**.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Testar zona não servida, peso-limite, dois volumes e estado perdido.
- Um número de seguimento de um cliente não deve ser visível a partir de outra conta.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `design-workflow-requires-verified-core-capabilities`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
