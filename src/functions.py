import logging
import os
from sys import argv
from time import strftime


def logconfig():
    """
    Configura il sistema di logging per l'applicazione.

    Inizializza il logging con handler per file e console e
    opzionalmente per un widget GUI.
    Crea la cartella 'logs' se non esiste.
    Il livello di logging può essere DEBUG (con flag -d)
    o INFO (default).

    Args:
        log_widget (tkinter.Text, optional):
        Widget di testo Tkinter dove visualizzare i log in GUI.
        Se None (default), i log vengono scritti solo su file e console.

    Returns:
        None

    Behavior:
        - Crea la cartella 'logs' nella directory corrente se non esiste.
        - Imposta il livello di logging a DEBUG se il flag '-d' è presente in sys.argv.
        - Imposta il livello di logging a INFO altrimenti.
        - Configura tre handler:
            1. FileHandler: scrive i log in un file con timestamp nel nome.
            2. StreamHandler: scrive i log su console/stdout.
            3. TextWidgetHandler:
            (opzionale) scrive i log nel widget GUI fornito.
        - Formato log: "{asctime} - {levelname} - {message}" con data/ora in formato ISO.

    Logs:
        Registra tramite il sistema di logging appena configurato.
    """

    if not (os.path.exists(os.path.join(os.getcwd(), "logs"))):
        os.mkdir("logs")

    if "-d" in argv:
        level = logging.DEBUG
    else:
        level = logging.INFO

    handlers = [
        logging.FileHandler(
            filename=f"logs/{strftime("%Y-%m-%d_%H-%M-%S")}.log",
            encoding="utf-8",
            mode="a",
        ),
        logging.StreamHandler(),
    ]

    # Add GUI text widget handler if provided

    logging.basicConfig(
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level,
        handlers=handlers,
    )
