# Public member HTTP routes — Éclair 2.0.0 experimental

El almacenamiento del demostrador sigue utilizando los archivos protegidos de `Store` y un bloqueo global. Está limitado a 1000 cuentas; ninguna promesa de atomicidad multiarchivo, de acceso a gran escala ni de tolerancia a fallos transaccionales. Un backend SQL es un requisito previo antes de cualquier explotación de negocio.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
