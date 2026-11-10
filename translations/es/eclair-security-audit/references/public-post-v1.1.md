# Public member HTTP routes — Éclair 2.0.0 experimental

El prototipo v1.1 tiene una limitación `RateLimit::attempt` antes del hash, una separación estricta miembros/admin y tokens de sesión de 256 bits. Evaluar la seguridad de los `Origin`, de TLS detrás de un reverse proxy, CSRF, IDOR, enumeración de cuentas, fugas de información y concurrencia. No confundir tests aislados con una auditoría en producción.

El patch fuente se encuentra en `core-patch/` de la distribución completa, no incluido en una copia autónoma del skill. No considerar nunca este patch como una API oficial antes de su fusión upstream.
