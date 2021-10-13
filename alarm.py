from playsound import playsound
import schedule
import time

def ring():
  playsound('./sounds/bell.mp3')

schedule.every().day.at("03:00").do(ring) # wake up, iron, vc, cook breakfast (45 min)
schedule.every().day.at("03:45").do(ring) # quiet time (30 min)
schedule.every().day.at("04:15").do(ring) # pray (20 min)
schedule.every().day.at("04:35").do(ring) # brush, floss, trays (20 min)
schedule.every().day.at("04:55").do(ring) # panda daily (10 min)
schedule.every().day.at("05:05").do(ring) # L1 (45 min)
schedule.every().day.at("05:50").do(ring) # break (10 min)
schedule.every().day.at("06:00").do(ring) # L2 (45 min)
schedule.every().day.at("06:45").do(ring) # break (10 min)
schedule.every().day.at("06:55").do(ring) # L3 (45 min)
schedule.every().day.at("07:40").do(ring) # break (10 min)
schedule.every().day.at("07:50").do(ring) # L4 (45 min)
schedule.every().day.at("08:35").do(ring) # cook, lunch, brush, floss, trays, dishes (1 hr)
schedule.every().day.at("09:35").do(ring) # nap, Bible (45 min)
schedule.every().day.at("10:20").do(ring) # wake up, shower (20 min)
schedule.every().day.at("10:40").do(ring) # L5 (45 min)
schedule.every().day.at("11:25").do(ring) # break (10 min)
schedule.every().day.at("11:35").do(ring) # L6 (45 min)
schedule.every().day.at("12:20").do(ring) # break (10 min)
schedule.every().day.at("12:30").do(ring) # L7 (45 min)
schedule.every().day.at("13:15").do(ring) # dinner, dishes, brush, floss, trays, meal prep (1 hr)
schedule.every().day.at("14:15").do(ring) # L8 (45 min)
schedule.every().day.at("15:00").do(ring) # break (10 min)
schedule.every().day.at("15:10").do(ring) # L9 (45 min)
schedule.every().day.at("15:55").do(ring) # walk (1 hr)
schedule.every().day.at("16:55").do(ring) # shower, cream (45 min)
schedule.every().day.at("17:40").do(ring) # L10 (45 min)
schedule.every().day.at("18:25").do(ring) # break (5 min)
schedule.every().day.at("18:30").do(ring) # read (30 min)
schedule.every().day.at("19:00").do(ring) # sleep, Bible (8 hr)

while True:
  schedule.run_pending()
  time.sleep(1)
