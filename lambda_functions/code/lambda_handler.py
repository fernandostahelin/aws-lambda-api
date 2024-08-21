import datetime
from api import MercadoBTCapi
from writer import S3Writer


def handler(event, context):
    coin = "BTC"
    date = (datetime.datetime.now() - datetime.timedelta.days(2)).date()
    api = MercadoBTCapi(coin=coin)
    data = api.get_data(date=date)

    writer = S3Writer(coin=coin)
    writer.write(data)
