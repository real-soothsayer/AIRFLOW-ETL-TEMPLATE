
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from etl import CONFIG
from etl.common.deduplicate import deduplicate

## DAG documentation
"""
This DAG is used to deduplicate rows from a csv file

- Task 1 : deduplicate rows from a csv file
"""

## DAG DEFINITION
with DAG(
        'dedup_flow',
        default_args={
            'depends_on_past': False,
            'email': CONFIG['notif'],
            'email_on_failure': True,
            'email_on_retry': False,
            'max_active_run': 1,
            'retries': 0,
            'retry_delay': timedelta(minutes=2)  #  20 minutes
        },
        description='Deduplicate rows from a csv file',
        schedule_interval="5 * * * *",
        start_date=datetime(2023, 5, 1, 0, 0, 0),
        catchup=False,
        tags=['DEDUP']
) as dag:
    deduplicate = PythonOperator(
        task_id='dedup_task',
        provide_context=True,
        python_callable=deduplicate,
        on_failure_callback=deduplicate, # Replace with the failure callback function
        dag=dag
    )

    deduplicate

if __name__ == "__main__":
    dag.clear()
    dag.run()
