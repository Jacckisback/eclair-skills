# Public member HTTP routes — Éclair 2.0.0 experimental

Los formularios públicos GET utilizan `Security::formField()` y deben declararse `cache:false`. Sus respuestas no deben alcanzar el fast path del núcleo. POST queda excluido del fast path y forzado a no-store. Probar la purga en la activación del módulo y comprobar la ausencia de cookies/identidades en el HTML de la caché compartida.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
