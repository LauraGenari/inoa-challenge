# dashboard/cron.py

from django_cron import CronJobBase, Schedule

from .views import check_prices

class CheckPricesCronJob(CronJobBase):      
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'dashboard.check_prices_cron_job'  # Identificador único

    def do(self):
        check_prices()
