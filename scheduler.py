import schedule
import time
import os

def run_etl():
    print("ETL en cours...")
    os.system("python load_mongodb.py")

schedule.every(1).minutes.do(run_etl)

print("Scheduler démarré...")

while True:
    schedule.run_pending()
    time.sleep(1)