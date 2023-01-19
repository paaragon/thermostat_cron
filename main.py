import os
import db
import temp_service


def main():
    time_on = db.get_minutes_on()
    if time_on > int(os.environ["MAX_MINUTES_ON"]):
        print("no max minutes reached")
        return

    last_setted = db.get_last_setted()
    last_mode = db.get_last_mode()

    print("setting " + str(last_setted - 1))
    result = temp_service.set_temp(last_setted - 1, last_mode)
    print(result, result.text)


if __name__ == "__main__":
    main()
