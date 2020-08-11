# -*- coding: utf-8 -*-

from airflow.models import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from datetime import timedelta, datetime
import pendulum
import random

local_tz = pendulum.timezone("Asia/Tokyo")

default_args = {
    "owner": "Airflow",
    "start_date": datetime(2019, 1, 1, tzinfo=pendulum.timezone("Asia/Tokyo")),
    "depends_on_past": True,
    "retries": 1,
    "retry_deray": timedelta(minutes=5),
}


dag = DAG(
    dag_id="python_operator", default_args=default_args, schedule_interval="@once"
)

op1 = BashOperator(
    task_id="op1", bash_command="echo {}".format(datetime.now()), dag=dag,
)


def print_random(rnd):
    print(rand)
    return "この戻り値はlogに出力されます。:" + rnd


rnd = random.random()

op2 = PythonOperator(task_id="op2", python_callable=print_random, dag=dag)

op1 >> op2
