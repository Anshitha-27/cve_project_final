from apscheduler.schedulers.background import BackgroundScheduler
from fetch_cve import store_cve_data

scheduler = BackgroundScheduler()
scheduler.add_job(store_cve_data, "interval", hours=24)  
scheduler.start()
