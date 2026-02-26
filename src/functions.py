import logging
import os
import requests
import json
from bs4 import BeautifulSoup
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


def scrape_page(url):
    """Scrape le pagine web specificate negli URL e registra i dati estratti.
    Args:
        url (str): URL della pagina web da cui estrarre i dati."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Solleva un'eccezione per status code 4xx/5xx
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all('table')[0].find_all('tr')
        code = None
        link = None
        rewards = None
        dict_list = []

        for row in rows[1:]:  # Salta l'intestazione della tabella
            columns = row.find_all("td")
            column_codes = columns[0]
            column_rewards = columns[1]
            if column_codes:  # Se la colonna dei codici esiste, estrai il codice e il link
                code_row = column_codes.find("input")
                if code_row:
                    code = code_row["value"]
                link_row = column_codes.find("a")
                if link_row:
                    link = link_row["href"]
            if column_rewards:  # Se esiste la colonna delle ricompense esiste, estrai le ricompense
                rewards = str(column_rewards.text).split("\n")
                tmp = []
                for el in rewards:
                    if el != "":  # Rimuove le stringhe vuote dalla lista delle ricompense
                        tmp.append(el)
                rewards = tmp
                reward_names = []
                reward_amounts = []
                for i, el in enumerate(rewards):
                    if i % 2 == 0:
                        reward_names.append(el)
                    else:
                        el = el.replace(",", "")
                        el = int(el.replace("x", ""))
                        reward_amounts.append(el)

                rewards = dict(zip(reward_names, reward_amounts))

            reward_dict = {"Codice": code, "Link": link, "Ricompense": rewards}
            dict_list.append(reward_dict)
        return dict_list

    except requests.exceptions.RequestException as e:
        logging.error(f"Errore durante la richiesta a {url}: {e}")
    except Exception as e:
        logging.error(
            f"Errore durante l'estrazione dei dati da {url}: {e}")


def save_to_json(data, filepath):
    """Salva i dati estratti in un file JSON."""
    with open(filepath, "w") as file:
        json.dump(data, fp=file, indent=4)
    pass
