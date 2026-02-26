import functions as fn
import logging
import time

FILEPATH = "output/codes.json"
URL = "https://game8.co/games/Honkai-Star-Rail/archives/410296"
# Funziona anche per ZZZ: https://game8.co/games/Zenless-Zone-Zero/archives/435683
# Funziona anche per Genshin: https://game8.co/games/Genshin-Impact/archives/304759


def main():
    start_time = time.time()
    fn.logconfig()
    logging.info("Applicazione avviata")

    data = fn.scrape_page(URL)
    fn.save_to_json(data, FILEPATH)

    logging.info("Applicazione terminata in %.2f secondi",
                 time.time() - start_time)


if __name__ == "__main__":
    main()
