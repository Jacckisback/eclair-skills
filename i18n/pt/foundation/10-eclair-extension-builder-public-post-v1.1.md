# Public member HTTP routes — Éclair 2.0.0 experimental

Um protótipo de rota POST pública consta de `examples/extensions/member-directory/`. É rejeitado pelo núcleo 2.0 oficial. Utilizar o manifesto apenas com o patch experimental e o acordo explícito de um mantenedor, nunca em produção. POST exige `cache:false`, TLS, CSRF, redirecionamento relativo.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
