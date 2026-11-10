---
name: eclair-live-classes
description: "Anunciar e organizar aulas em direto por videoconferência. Use on Éclair CMS 2.x when the user wants to: anunciar e organizar aulas por videoconferência. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Aulas em direto — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **anunciar e organizar aulas por videoconferência**. A **parte pública em leitura é realizável hoje**; as escritas por visitantes exigem mais do que o contrato atual. Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** Integrações Zoom dos LMS. Família: LMS.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Sessão, data, fuso horário, ligação de acesso, inscritos**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Publicar o calendário das sessões em GET, enviar a ligação de acesso pelo serviço de videoconferência ou por e-mail, não numa página pública. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** A leitura pública (GET, colocável em cache) é realizável hoje. Qualquer escrita por um visitante exige uma rota POST pública que o núcleo 2.0 não abre às extensões (PR #19 em rascunho, não fundida): não a simular.
7. **Invariante de segurança:** A ligação de uma sessão paga ou privada nunca é publicada. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Verificar a apresentação das datas em dois fusos horários» e o teste de recusa «Uma sessão passada deixa de ser proposta para inscrição». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote só de leitura (rotas GET) validado, e plano escrito para a parte de escrita, claramente marcada como não entregue.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Verificar a apresentação das datas em dois fusos horários.
- Uma sessão passada deixa de ser proposta para inscrição.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `public-read-only-prototype-possible`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
