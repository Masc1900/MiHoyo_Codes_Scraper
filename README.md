# Honkai Star Rail Promo Code Scraper

## Descrizione

Questo programma permette di estrarre automaticamente i codici promozionali per il gioco Honkai Star Rail dal sito Game8.
In futuro sarà possibile estendere il programma per altri giochi e altri siti, ma attualmente è focalizzato su Star Rail.

## Input

Il programma estrae i dati da [questa pagina](https://game8.co/games/Honkai-Star-Rail/archives/410296).

Un esempio di pagina è disponibile in [docs/example.html](docs/example.html).

## Output

L'output è un file JSON formattato come segue:

```bash
[
    {
        "Codice": "ALETTERFORYOU",
        "Link": "https://hsr.hoyoverse.com/gift?code=ALETTERFORYOU",
        "Ricompense": [
            {
                "Nome": " Adventure Log",
                "Quantita'": 6,
                "Immagine": "https://img.game8.co/3656095/54eed904294437c7e5e6d92315ca3e02.png/show"
            },
            {
                "Nome": " Dreamlight - Mixed Sweets",
                "Quantita'": 2,
                "Immagine": "https://img.game8.co/3837201/bb231adea728f988f634e82a29586167.png/show"
            }
        ]
    }
]
```

Il file viene salvato in `output/codes.json`.

## Logging

Il programma utilizza il modulo logging di Python, configurato tramite la funzione `logconfig()` in [src/functions.py](src/functions.py).
Tutti i log sono scritti in italiano e vengono salvati nella cartella `logs`.

## Documentazione

Tutta la documentazione, i commenti e i messaggi di log sono in italiano. I nomi delle funzioni, variabili e classi sono in inglese.

## Compilazione

Per compilare il programma in un eseguibile, utilizzare lo script [scripts/buildEXE.bat](scripts/buildEXE.bat).

## Dipendenze

- Python 3.x
- requests
- beautifulsoup4
- auto-py-to-exe

Le dipendenze sono elencate in [requirements.txt](requirements.txt).

## Esecuzione

Per eseguire il programma:

```bash
python src/main.py
```

## Struttura del progetto

```bash
Codes_Scraper
├─ .vscode
│  └─ settings.json
├─ docs
│  └─ example.html
├─ icons
│  └─ Stellar-Jade.ico
├─ output
│  └─ codes.json
├─ README.md
├─ requirements.txt
├─ scripts
│  └─ buildEXE.bat
├─ src
│  ├─ functions.py
│  └─ main.py
└─ tree.md

```
