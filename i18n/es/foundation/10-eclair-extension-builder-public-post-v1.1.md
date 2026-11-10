# Public member HTTP routes — Éclair 2.0.0 experimental

Un prototipo de ruta POST pública figura en `examples/extensions/member-directory/`. El núcleo 2.0 oficial lo rechaza. Utilizar el manifiesto únicamente con el patch experimental y el acuerdo explícito de un mantenedor, nunca en producción. POST exige `cache:false`, TLS, CSRF, redirección relativa.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
