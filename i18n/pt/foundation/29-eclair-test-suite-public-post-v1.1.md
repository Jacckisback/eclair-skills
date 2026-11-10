# Public member HTTP routes — Éclair 2.0.0 experimental

Testar `php tests/member-directory.php` + `php tests/member-public.php` e os testes Python. Num clone real do Éclair 2.0.0, aplicar o patch a uma feature branch limpa, executar `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check` e ensaios HTTP/TLS. Nenhuma fusão sem estes critérios.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
