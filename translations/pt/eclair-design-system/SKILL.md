---
name: eclair-design-system
description: "Construir uma linguagem visual coerente e sustentável (tokens, componentes). Use on Éclair CMS 2.x when the user wants to: construir uma linguagem visual coerente e fácil de manter. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Sistema de design — Éclair CMS 2.x

## Desencadeador e resultado esperado
Utilizar este skill para **construir uma linguagem visual coerente e fácil de manter**. Esta funcionalidade é **realizável hoje** com o contrato nativo (tema, blocos, rotas GET, páginas de administração, tarefas). Este skill é um **workflow de agente**, não uma extensão PHP funcional nem uma garantia de conformidade.

**Equivalente WordPress:** theme.json e estilos globais. Família: Design e UX.

## Diagnóstico obrigatório antes de qualquer modificação
1. Ler `references/core-map.md` (o que o núcleo já faz) e `references/native-contract.md`; verificar a versão real do CMS e as capacidades em `GET /<admin>/api/capabilities` (se o acesso for autorizado).
2. Ler `references/family-contract.md` e `references/acceptance.md`. Nunca copiar o antigo sistema de packs v0.x nem código PHP do WordPress para o Éclair 2.
3. Identificar o modelo de dados: **Tokens, grelha, espaçamentos, cores, tipografia, componentes e estados**. Documentar o que é público, o que é privado e de onde vem cada dado.

## Procedimento específico
4. **Percurso:** Declarar a escala dos tokens, reutilizar componentes, documentar estados e variantes; compatibilidade com o tema Éclair. Descrever os estados e os erros antes de escrever código.
5. **Localizações:** código próprio do site em `site/extensions/<id>/`, aparência em `site/themes/<id>/`, dados sob `$ctx['data']`, conteúdos e definições através da administração ou do MCP. Nunca editar `app/`, `assets/`, `index.php` nem o updater.
6. **Contrato atual:** O Éclair v2 expõe temas em site/themes e blocos declarativos de extensão. Não modificar app/, nem index.php, nem a CSP, nem a geração da cache; validar os temas através de tools/validate.php.
7. **Invariante de segurança:** Não introduzir uma folha CSS pesada nem uma biblioteca JS sem prova de necessidade. Verificar também as permissões do lado do servidor, o escape com `e()`, a validação dos dados e a ausência de segredos ou de dados pessoais no HTML público ou numa cache partilhada.
8. **Provas:** escrever o teste positivo «Testar o contraste, a coerência e a mudança de tema» e o teste de recusa «Alterar a cor principal não cria nenhuma ilegibilidade das ligações ou dos erros». Medir as regressões de SEO e de desempenho, documentar a reversão.
9. **Validação nativa:** `php tools/validate.php <dossier> --json`, `php tests/run.php` e `php tools/measure.php --check` num checkout oficial para qualquer pacote produzido. Para uma parte não suportada pelo núcleo, fornecer uma nota de lacuna e um teste bloqueante, nunca um êxito fictício.

## Entregáveis obrigatórios
- Miniespecificação: objetivo, utilizadores, percursos, estados, dados, medições.
- Matriz de autorizações e de cache: rota, método, sessão, visibilidade, indexação.
- Pacote `extension.json`/`extension.php` ou pacote de tema validado, apenas se um bloco ou uma definição nativa não for suficiente.
- Testes dos casos positivos e das recusas, procedimento de desativação que conserva os dados, nota de compatibilidade.

## Critérios de aceitação
- Testar o contraste, a coerência e a mudança de tema.
- Alterar a cor principal não cria nenhuma ilegibilidade das ligações ou dos erros.
- Nada é publicado, ativado nem colocado em produção sem uma pessoa autorizada; não é prometida nenhuma pontuação, classificação ou citação por uma IA.
- As partes não suportadas pelo Éclair 2.0 são explicitamente assinaladas como **não entregáveis em produção**.

**Estado de maturidade deste skill:** `native-v2-workflow`. Ver `references/acceptance.md` para os casos de ensaio reproduzíveis.
