# Public member HTTP routes — Éclair 2.0.0 experimental

Las rutas públicas POST **no** están presentes en Éclair 2.0 oficial. El patch propuesto v1.1 hace una excepción controlada: método POST explícito, `cache:false`, HTTPS, `Security::checkFormToken()`, respuesta `private,no-store`, redirección 303 relativa. Realizar siempre pruebas HTTP con el CMS completo antes de la fusión.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
