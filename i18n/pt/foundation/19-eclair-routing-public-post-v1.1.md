# Public member HTTP routes — Éclair 2.0.0 experimental

As rotas públicas POST **não** estão presentes no Éclair 2.0 oficial. O patch proposto v1.1 faz uma exceção controlada: método POST explícito, `cache:false`, HTTPS, `Security::checkFormToken()`, resposta `private,no-store`, redirecionamento 303 relativo. Fazer sempre ensaios HTTP com o CMS completo antes da fusão.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
