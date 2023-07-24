import os
import db
import temp_service
from logger import logger as log

def main():
    time_on = db.get_minutes_on()
    
    if time_on is None:
        log.info("no info about time_on")
        return

    if time_on < int(os.environ["MAX_MINUTES_ON"]):
        log.info("no max minutes reached")
        return

    last_setted = db.get_last_setted()
    last_mode = db.get_last_mode()

    log.info("setting " + str(last_setted - 1))
    result = temp_service.set_temp(last_setted - 1, last_mode)
    log.info(result, result.text)


if __name__ == "__main__":
    main()
