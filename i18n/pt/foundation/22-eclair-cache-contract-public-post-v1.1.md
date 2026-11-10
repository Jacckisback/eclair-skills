# Public member HTTP routes — Éclair 2.0.0 experimental

Os formulários públicos GET utilizam `Security::formField()` e devem ser declarados `cache:false`. As suas respostas não devem atingir o fast path do núcleo. POST é excluído do fast path e forçado a no-store. Testar a purga na ativação do módulo e verificar a ausência de cookies/identidades no HTML de cache partilhada.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
