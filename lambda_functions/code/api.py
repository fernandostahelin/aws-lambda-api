import requests
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MercadoBTCapi:
    def __init__(self, coin: str) -> None:
        self.coin = coin
        self.base_endpoint = "https://www.mercadobitcoin.net/api"

    def _get_endpoint(self, date: datetime.date) -> str:
        return f"{self.base_endpoint}/{self.coin}/day-summary/{date.year}/{date.month}/{date.day}"
    
    def get_data(self, date: datetime.date) -> dict:
        endpoint = self._get_endpoint(date=date)
        logger.info(f"getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        return response.json()

resultado = MercadoBTCapi(coin="BTC").get_data(datetime(2024,8,20))
print(resultado)