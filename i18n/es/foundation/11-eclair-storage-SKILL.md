---
name: eclair-storage
description: Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress.
---

# Éclair Storage — elegir la persistencia adecuada

## Decisión de almacenamiento
1. Para contenido y ajustes de Éclair, utilizar `Eclair\Store` y el prefijo `data/ext/<id>/` obtenido mediante `$ctx['data']`.
2. Comprobar `Store::locked`, las escrituras atómicas y los volúmenes realmente manejados; no inventar ninguna garantía multiarchivo transaccional.
3. Para pedidos/pagos/existencias y progreso LMS concurrente: especificar SQLite o MySQL **como dependencia opcional del módulo** con sus migraciones, restricciones, transacciones, backup y recuperación. El contrato nativo v2 no proporciona un PDO genérico para las extensiones.
4. Declarar datos personales, retención, eliminación y exportación; no conservar claves ni tokens en las copias de seguridad.
5. Migraciones nativas de extensión mediante el manifiesto `migrations[]` y el método `migrate`: aditivas, versionadas, idempotentes. Una migración de esquema SQL debe tener un plan aparte, no desencadenarse en una página GET.
6. Prever una copia de seguridad coherente, una restauración en frío y un test de rollback. Si SQL no está disponible en un alojamiento compartido, anunciar la funcionalidad como no disponible en lugar de recurrir a una persistencia no fiable.
7. Probar las colisiones, los reinicios, la concurrencia, los duplicados, la corrupción, chmod/symlink, el backup y la reconciliación.

## Reglas
El almacenamiento nativo sin base de datos debe seguir siendo posible para un sitio sencillo. Los prototipos SQL v0.5/v0.8 no están instalados ni reconocidos por v2. No prometer «exactamente una vez» para los efectos externos.

## Entregables
Esquema, matriz de invariantes, protocolo de migración/restore, requisitos de alojamiento, tests de transacción y de integridad.

## V1.0 — Modelo de cuentas ligeras
El prototipo `member-directory` respeta `data/ext/<id>/`, escrituras atómicas y un bloqueo global. El almacenamiento en varios archivos **no es una transacción SQL**. La cuota de 1 000 cuentas es un límite de laboratorio: todo proyecto comercial con muchos miembros debe disponer primero del contrato SQL transaccional.

## Éclair 2.0 — prototipo v1.1 (experimental)
El almacenamiento del demostrador sigue utilizando los archivos protegidos de `Store` y un bloqueo global. Está limitado a 1000 cuentas; ninguna promesa de atomicidad multiarchivo, de acceso a gran escala ni de tolerancia a fallos transaccionales. Un backend SQL es un requisito previo antes de cualquier explotación de negocio.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
