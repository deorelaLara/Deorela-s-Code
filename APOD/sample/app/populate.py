from peewee import EXCEPTIONS
from apod import APOD
from models import Pictures
from datetime import timedelta, date
import json

def main():
    api = APOD()
    def daterange(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    start_dt = date(2000, 1, 1)
    end_dt = date(2020, 12, 31)
    for dt in daterange(start_dt, end_dt):
        #print(dt.strftime("%Y-%m-%d"))
        data=(json.dumps(api.getPicture(dt.strftime("%Y-%m-%d")), indent=2))

    for n in data:
        try:
            raw = n
            if raw:
                pic, created = Pictures.get_or_create(**raw)
                print(f"Picture {'created' if created else 'existing'}: {pic.name}")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
    myDB.close()