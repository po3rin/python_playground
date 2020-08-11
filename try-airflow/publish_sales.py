#!/usr/bin/env python

import datetime
import json
import os
import random
import time

while True:
    data = {
        "sales_number": random.randrange(1, 9999999999),
        "sales_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "sales_category": "sales",
        "department_code": 205,
        "store_code": 26217,
        "customer_code": 2728336234,
        "employee_code": 3540669664,
        "detail": {
            "sales_row_number": 1,
            "item_code": 7118324379,
            "item_name": "item1",
            "sale_unit_price": 1500,
            "sales_quantity": 1,
            "discount_price": 0,
            "consumption_tax_rate": 10,
            "consumption_tax_price": 150,
            "sales_price": 1650,
            "remarks": "sample",
        },
    }

    message = json.dumps(data)
    command = (
        "gcloud --project=pon-playground pubsub topics publish sales --message='%s'"
        % message
    )
    print(command)
    os.system(command)
    time.sleep(random.randrange(1, 5))
