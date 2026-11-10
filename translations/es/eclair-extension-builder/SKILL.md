---
name: eclair-extension-builder
description: Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract.
---

# Éclair Extension Builder — construir una extensión realmente instalable en v2

## Objetivo
Crear un **paquete `eclair-extension/1` conforme al núcleo v2**. No utilizar el manifiesto `manifest.json` ni los archivos `events.php` / `services.php` de los antiguos prototipos como si estuvieran soportados.

## Proceso
1. Leer `references/core-map.md`, `docs/EXTENSION-CONTRACT.md`, `docs/schemas/extension.schema.json` y `examples/extensions/bonjour` del checkout.
2. Comprobar `ECLAIR_VERSION` y el contrato `eclair-extension/1` mediante el código y, si es accesible, la API de capacidades.
3. Definir `id`, `version`, `requires`, `depends`, `provides`, `entry`, rutas, bloques, campos, assets, `tasks`, migraciones; utilizar únicamente los campos del esquema.
4. Entregar en `site/extensions/<id>/` **sin escribir en `app/`**; la entrada PHP debe devolver un objeto y no debe producir ninguna salida durante su carga.
5. Controlar la salida con `e()`; leer los ajustes desde `$ctx['settings']`; almacenar mediante `Eclair\Store` bajo `$ctx['data']`. Para los secretos: ubicación privada y política de exclusión de las copias de seguridad documentada.
6. Rutas públicas solo GET. En una página pública que muestre un dato de sesión o individual: detenerse y solicitar un nuevo contrato de identidad/caché; nada de falsos rodeos.
7. Calcular los SHA-256 de los archivos y declararlos en `files`, salvo `extension.json`. Generar un paquete ZIP cuya raíz contenga el manifiesto.
8. `php tools/validate.php chemin/extension --json`; corregir todos los errores antes de proponer la importación, después probar `php tests/run.php` y `php tools/measure.php --check`.
9. Una persona autorizada importa, previsualiza/controla, activa; documentar la desactivación, la eliminación del código y la conservación de los datos.

## Entregables
`extension.json`, entrada `extension.php`, referencias, tests, prueba de validación oficial y manual de instalación. Ejemplo original en `examples/extensions/skill-sample/`; comprobar sobre el núcleo exacto antes del despliegue.

## V1.0 — Modelo avanzado entregado
Consultar `examples/extensions/member-directory`: demuestra rutas admin GET/POST nativas y una biblioteca PHP cargada únicamente por la extensión. No transformar su GET admin en un inicio de sesión público ni añadir un POST a `routes.public` (contrato v2 incompatible).

## Éclair 2.0 — prototipo v1.1 (experimental)
Un prototipo de ruta POST pública figura en `examples/extensions/member-directory/`. El núcleo 2.0 oficial lo rechaza. Utilizar el manifiesto únicamente con el patch experimental y el acuerdo explícito de un mantenedor, nunca en producción. POST exige `cache:false`, TLS, CSRF, redirección relativa.

## Éclair 2.0 — registro y recuperación (v1.2 experimental)

Leer `references/member-email-v1.2.md` antes de cualquier petición de creación de cuentas de clientes/alumnos o de recuperación de contraseña. El módulo `member-directory` v0.3 utiliza rutas públicas POST **fuera del contrato oficial**; no prometer nunca una instalación directa en un Éclair 2.0 sin modificar ni activar los flujos de email sin una URL HTTPS verificada y tests nativos. Preferir el sistema de extensiones v2 a cualquier modificación de la antigua arquitectura v0.x. Mantener separadas las cuentas públicas y las de administración, rechazar toda caché compartida para las páginas de miembros y tratar los emails como no entregados mientras no exista ninguna confirmación.
