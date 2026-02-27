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
        if all("https://" in arg for arg in argv[1:]):
            URLs = argv[1:]
        else:
            logging.critical("L'argomento fornito non è un URL valido.")
            return
    else:
        logging.critical(
            "Nessun URL fornito. (E.G. 'Mihoyo Code Scraper.exe' https://game8.co/games/Honkai-Star-Rail/archives/410296)")
        return
    for URL in URLs:
        FILENAME = URL.split("/")[-3].replace("-", " ")
        data = fn.scrape_page(URL)
        fn.save_to_json(data, FILEPATH, FILENAME)

    logging.info("Applicazione terminata in %.2f secondi",
                 time.time() - start_time)


if __name__ == "__main__":
    main()
