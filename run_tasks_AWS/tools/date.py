import datetime
import dateutil.relativedelta


class Date:
    def __init__(self):
        self.date_today = datetime.datetime.now()
        self.date_one_month_before = self.date_today + dateutil.relativedelta.relativedelta(months=-1)
        self.dates_facebook = {'until': str(self.date_today).split(' ')[0],
                               'since':  str(self.date_one_month_before).split(' ')[0]}
        self.date_youtube = f'{str(self.date_today + dateutil.relativedelta.relativedelta(months=-3)).split(" ")[0]}T01:00:00-00:00'

