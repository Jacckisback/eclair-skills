# Public member HTTP routes — Éclair 2.0.0 experimental

O armazenamento do demonstrador utiliza ainda os ficheiros protegidos de `Store` e um bloqueio global. Está limitado a 1000 contas; nenhuma promessa de atomicidade multificheiro, de acesso em grande escala ou de tolerância a falhas transacionais. Um backend SQL é um pré-requisito antes de qualquer exploração de negócio.

O patch de origem encontra-se em `core-patch/` da distribuição completa, não incluído numa cópia autónoma do skill. Nunca considerar este patch como uma API oficial antes da sua fusão upstream.
