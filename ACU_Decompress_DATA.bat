@echo off
for %%F in (%*) do (
    python "%~dp0ACU_Decompress_DATA.py" "%%~F"
)
pause

