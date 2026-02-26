@echo off
pyinstaller --noconfirm --onefile --console --name "Mihoyo Code Scraper" --icon "..\icons\Stellar-Jade.ico" --add-data "..\src\functions.py;." --distpath "..\dist" --workpath "..\build" --specpath "..\specs" "..\src\main.py"
pause
