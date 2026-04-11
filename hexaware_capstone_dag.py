from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

# 1. Configuration for the Hexaware Data Pipeline
default_args = {
    'owner': 'lakshya',
    'depends_on_past': False,
    'email_on_failure': False,
    # If Databricks cluster is cold, retry after 2 minutes
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

# 2. Define the Workflow
with DAG(
    dag_id='hexaware_retail_pipeline',
    default_args=default_args,
    description='Triggers the Medallion (Bronze-Silver-Gold) Job in Azure Databricks',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['retail_analytics', 'databricks'],
) as dag:

    
    run_medallion_job = DatabricksRunNowOperator(
        task_id='trigger_medallion_workflow',
        databricks_conn_id='databricks_default',
        job_id=129772944750961 
    )

    run_medallion_job
