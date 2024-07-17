from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('my_dag', default_args=default_args, schedule_interval=timedelta(days=1))

# Define tasks
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Hello World"',
    dag=dag,
)

# Define task dependencies
task1
