# Public member HTTP routes — Éclair 2.0.0 experimental

El prototipo v1.1 dispone de handlers públicos GET formulario + POST inicio/cierre de sesión + GET espacio privado. Solo son válidos tras la incorporación aprobada del contrato POST. Sesiones de miembros distintas de las de los admins, token opaco, CSRF double-submit y CSRF de sesión en el cierre de sesión; ningún rol admin/editor concedido.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
