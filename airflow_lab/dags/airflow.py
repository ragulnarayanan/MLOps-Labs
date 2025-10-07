from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Import functions from functions.py
from functions import load_data, split_data, fit_model, predict_data

# Define default_args
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 10, 5),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'cancer_classification',
    default_args=default_args,
    description='Breast Cancer classification with Random Forest',
    schedule=None,
    catchup=False,
)

# Define tasks
load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

split_data_task = PythonOperator(
    task_id='split_data',
    python_callable=split_data,
    op_args=['{{ task_instance.xcom_pull(task_ids="load_data")[0] }}',  # X data from load_data
             '{{ task_instance.xcom_pull(task_ids="load_data")[1] }}'],  # y data from load_data
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=fit_model,
    op_args=['{{ task_instance.xcom_pull(task_ids="split_data")[0] }}',  # X_train
             '{{ task_instance.xcom_pull(task_ids="split_data")[2] }}'],  # y_train
    dag=dag,
)

predict_model_task = PythonOperator(
    task_id='predict_model',
    python_callable=predict_data,
    op_args=['{{ task_instance.xcom_pull(task_ids="split_data")[1] }}'],  # X_test
    dag=dag,
)

# Set task dependencies
load_data_task >> split_data_task >> train_model_task >> predict_model_task
