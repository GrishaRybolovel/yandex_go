from django.core.management.base import BaseCommand
from api.models import Price
import requests
import json


def main():
    url = 'https://ya-authproxy.taxi.yandex.ru/3.0/routestats'

    payload = {
        "extended_description": True,
        "format_currency": True,
        "payment": {
            "type": "card",
        },
        "route": [
            [55.780336, 49.133755],
            [55.823903, 49.154357]
        ],
        "selected_class": "econom",
        "supports_paid_options": True,
        "supported_markup": "tml-0.1",
        "summary_version": 2
    }

    res = requests.post(url=url, json=payload)
    response = json.loads(res.content)    
    try:
        pr = int(response['service_levels'][0]['price'][:3])
        coef = response['service_levels'][0]['paid_options']['value']
        price = int(coef * int(pr))

        try:
            obj = Price.objects.create(price=price, point_from_x=55.780336, point_from_y=49.133755,
                                       point_to_x=55.823903, point_to_y=49.154357)
            obj.save()
        except Exception as e:
            print(str(e))
    except:
        pass


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        main()
