from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from airflow.utils.helpers import chain, cross_downstream

from random import seed, random

from datetime import timedelta

default_arguments = {'owner': 'VG', 'start_date':days_ago(1)}

with DAG(dag_id = 'Core_concepts', 
        schedule_interval = '@daily',
        catchup = False,
        default_args = default_arguments
        ) as dag:
    bash_task = BashOperator(
        task_id="bash_command",
        bash_command="echo $TODAY",
        env={"TODAY": "2020-05-21"}
    )
    def print_random_number(number):
        seed(number)
        print(random())

    python_task = PythonOperator(
        task_id="python_function", python_callable=print_random_number, op_args=[1]
    )
see
bash_task >> python_task