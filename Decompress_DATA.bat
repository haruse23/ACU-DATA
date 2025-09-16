@echo off
for %%F in (%*) do (
    python "%~dp0Decompress_DATA.py" "%%~F"
)
pause
