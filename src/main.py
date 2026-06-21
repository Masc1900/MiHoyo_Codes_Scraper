import functions as fn
import logging
import time
from sys import argv

FILEPATH = "output/"
# URL = "https://game8.co/games/Honkai-Star-Rail/archives/410296" # Link di Test
# Funziona anche per ZZZ: https://game8.co/games/Zenless-Zone-Zero/archives/435683
# Funziona anche per Genshin: https://game8.co/games/Genshin-Impact/archives/304759

# TODO Aggiungere un modo per usare più url alla volte tramite args (Mioyo Code Scraper.exe URL1 URL2 URL3...)


def main():
    """
    Funzione principale dell'applicazione.
    Esegue il processo di scraping e salvataggio dei dati per uno o più URL forniti come argomenti.
    """
    start_time = time.time()
    fn.logconfig()
    logging.info("Applicazione avviata")
    if len(argv) > 1:
        allowed_flags = {"-d"}
        args = argv[1:]
        invalid_args = [
            arg for arg in args
            if not (arg.startswith("http://") or arg.startswith("https://") or arg in allowed_flags)
        ]
        if invalid_args:
            logging.critical(
                f"Argomenti non validi: {invalid_args}. Passa solo URL e il flag -d.")
            return

        URLs = [arg for arg in args if arg.startswith("http://") or arg.startswith("https://")]
        if not URLs:
            logging.critical(
                "Nessun URL valido fornito. Inserisci almeno un URL dopo i flag.")
            return
    else:
        logging.critical(
            "Nessun URL fornito. (E.G. 'Mihoyo Code Scraper.exe' https://game8.co/games/Honkai-Star-Rail/archives/410296)")
        return
    for URL in URLs:
        FILENAME = URL.split("/")[-3].replace("-", " ")
        data = fn.scrape_page(URL)
        if not data:
            logging.warning(
                f"Nessun dato estratto da {URL}. Il file non verrà salvato.")
            continue
        fn.save_to_json(data, FILEPATH, FILENAME)

    logging.info("Applicazione terminata in %.2f secondi",
                 time.time() - start_time)


if __name__ == "__main__":
    main()
