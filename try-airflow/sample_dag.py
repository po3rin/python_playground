# -*- coding: utf-8 -*-

from airflow.models import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import timedelta, datetime
import pendulum

local_tz = pendulum.timezone("Asia/Tokyo")

default_args = {
    "owner": "Airflow",
    "start_date": datetime(2019, 1, 1, tzinfo=pendulum.timezone("Asia/Tokyo")),
    "depends_on_past": True,
    "retries": 1,
    "retry_deray": timedelta(minutes=5),
}


dag = DAG(dag_id="sample_dag", default_args=default_args, schedule_interval="@once")

op1 = BashOperator(
    task_id="op1", bash_command="echo {}".format(datetime.now()), dag=dag,
)

op2 = DummyOperator(task_id="op2", trigger_rule="all_success", dag=dag,)
op3 = DummyOperator(task_id="op3", trigger_rule="all_success", dag=dag,)
op4 = DummyOperator(task_id="op4", trigger_rule="all_success", dag=dag,)

op5 = BashOperator(
    task_id="op5", bash_command="echo {}".format(datetime.now()), dag=dag
)

op1 >> op2 >> [op3, op4] >> op5
