# Public member HTTP routes — Éclair 2.0.0 experimental

O protótipo v1.1 tem uma limitação `RateLimit::attempt` antes do hash, uma separação estrita membros/admin e tokens de sessão de 256 bits. Avaliar a segurança dos `Origin`, de TLS atrás de reverse proxy, CSRF, IDOR, enumeração de contas, fugas de informação e concorrência. Não confundir testes isolados com auditoria em produção.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
