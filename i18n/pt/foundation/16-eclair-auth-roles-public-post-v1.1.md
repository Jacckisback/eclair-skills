# Public member HTTP routes — Éclair 2.0.0 experimental

O protótipo v1.1 possui handlers públicos GET formulário + POST início/fim de sessão + GET área privada. Só são válidos após a adição aprovada do contrato POST. Sessões de membros distintas das dos admins, token opaco, CSRF double-submit e CSRF de sessão no fim de sessão; nenhum papel admin/editor concedido.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
