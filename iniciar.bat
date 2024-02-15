@echo off
timeout /t 3
cd "C:\Users\augus\OneDrive\Área de Trabalho\PESSOAL\Programação_Pessoal\Uminum - Blocos finalizados\venv\Scripts"
timeout /t 3
call activate
timeout /t 3
cd "C:\Users\augus\OneDrive\Área de Trabalho\PESSOAL\Programação_Pessoal\Uminum - Blocos finalizados\UminumBloco"
timeout /t 3
start python manage.py runserver

