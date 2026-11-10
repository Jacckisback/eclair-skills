---
name: eclair-storage
description: Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress.
---

# Éclair Storage — escolher a persistência certa

## Decisão de armazenamento
1. Para conteúdo e definições Éclair, utilizar `Eclair\Store` e o prefixo `data/ext/<id>/` obtido via `$ctx['data']`.
2. Verificar `Store::locked`, escritas atómicas e volumes realmente manipulados; não inventar garantias transacionais multificheiro.
3. Para encomendas/pagamentos/stocks e progresso LMS concorrente: especificar SQLite ou MySQL **como dependência opcional do módulo** com as suas migrações, restrições, transações, backup e retoma. O contrato nativo v2 não fornece PDO genérico para as extensões.
4. Declarar dados pessoais, retenção, eliminação e exportação; não conservar chaves nem tokens nas cópias de segurança.
5. Migrações nativas de extensão através do manifesto `migrations[]` e do método `migrate`: aditivas, versionadas, idempotentes. Uma migração de esquema SQL deve ter um plano separado, não ser desencadeada numa página GET.
6. Prever cópia de segurança coerente, restauro a frio e teste de rollback. Se o SQL estiver indisponível em alojamento partilhado, anunciar a funcionalidade como indisponível em vez de recorrer a uma persistência não fiável.
7. Testar as colisões, reinícios, concorrência, duplicados, corrupção, chmod/symlink, backup e reconciliação.

## Regras
O armazenamento nativo sem base de dados deve continuar a ser possível para um site simples. Os protótipos SQL v0.5/v0.8 não são instalados nem reconhecidos pela v2. Não prometer exatamente-uma-vez para os efeitos externos.

## Entregáveis
Esquema, matriz dos invariantes, protocolo de migração/restore, requisitos de alojamento, testes de transação e de integridade.

## V1.0 — Modelo de contas leves
O protótipo `member-directory` respeita `data/ext/<id>/`, escritas atómicas e um bloqueio global. O armazenamento em vários ficheiros **não é uma transação SQL**. A quota de 1 000 contas é um limite de laboratório: qualquer projeto comercial com muitos membros deve primeiro dispor do contrato SQL transacional.

## Éclair 2.0 — protótipo v1.1 (experimental)
O armazenamento do demonstrador utiliza ainda os ficheiros protegidos de `Store` e um bloqueio global. Está limitado a 1000 contas; nenhuma promessa de atomicidade multificheiro, de acesso em grande escala ou de tolerância a falhas transacionais. Um backend SQL é um pré-requisito antes de qualquer exploração de negócio.

## Éclair 2.0 — registo e recuperação (v1.2 experimental)

Ler `references/member-email-v1.2.md` antes de qualquer pedido de criação de contas de clientes/alunos ou de recuperação de palavra-passe. O módulo `member-directory` v0.3 utiliza rotas públicas POST **fora do contrato oficial**; nunca prometer uma instalação direta num Éclair 2.0 não modificado nem ativar os fluxos de e-mail sem URL HTTPS verificado e testes nativos. Preferir o sistema de extensões v2 a qualquer modificação da antiga arquitetura v0.x. Manter separadas as contas públicas e as de administrador, recusar qualquer cache partilhada para as páginas de membros e tratar os e-mails como não entregues enquanto não existir nenhuma confirmação.
