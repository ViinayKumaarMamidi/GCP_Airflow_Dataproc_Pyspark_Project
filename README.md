# GCP_Airflow_Dataproc_Pyspark_Project

This repo contains details about leveraging the Airflow in the GCP Composer and running the Ephemeral Dataproc Cluster to run Pyspark Job and Orchestrate within the Airflow, Thanks

**Project Goal:**

The main aim of this project is to understand how best we can utilize Apache Airflow inside GCP Cloud Composer to run a Pyspark Job by leveraging Ephemeral Dataproc Cluster for data processing. Thanks


**End to End Project Details:**

1. Department and Employee CSV files are placed in to the GCS bucket as the source and as Destination of this project is the GCS bucket with CSV file format, Please create a buckets for source files and output files as needed
2. In the GCP Composer, Airflow 3 has been spin up and necessary permissions to the corresponding service account has been provided to make sure it connects to GCS bucket, Dataproc cluster, BQ services
3. Once Airflow is up and running, In the Airflow DAGs folder, place the airflow_spark_job.py file
4. Place the emp_batch_job.py in to the required GCS bucket
5. Spark Processing Python File Details: python file: emp_batch_job.py does contain spark code to read the csv datasets from both files and perform join operation and write the final joined datasets into the GCS bucket with filtered datasets
6. Please note for end to end proecssing, I have limited the datasets for few records only
7. Airflow Spark Job Details: This airflow_spark_job.py contains details about creation of the Dataproc Cluster, Execution of the Python script (emp_batch_job.py) and Deletion of the Dataproc Cluster once the Spark job is ran to sucess. For testing purpose I have limited the cluster configurations to minimum to avoid cost. Please make sure you include/import required Airflow operators which supports Dataproc i.e,  DataprocCreateClusterOperator, DataprocSubmitJobOperator and DataprocDeleteClusterOperator
8. Once the Sources files are placed in the source GCS bucket, and corresponding Python file is placed in the mentioned location, upload the DAG into the DAGs folder and wait for 5-10 miniutes to see the DAG in the Airflow DAGs section and once DAG is available, Please trigger the DAG, If there are any errors found, please check the errors and resolved as needed
9. After triggering the DAG, your DAG first step which is creation of the Ephemeral Dataproc Cluster will take 5-10 minutes of the time, while the rest of the tasks with take less amount of the time
10. During Dataproc cluster creation, you can go to Dataproc service and verifiy whether your cluster is creating or not and check the logs as needed
11. Once all the tasks in the DAG is completed, you should see CSV file in the output folder mentioned in the code, Please verify and compare the datasets with source datasets to see proper filter of the data has occured or not
12. In this whole process, We are leveraging concepts of utilizing a Ephemeral Dataproc Cluster to process our Pyspark Job leveraging Airflow as Orchestorator Tool and Terminating the Dataproc Cluster once DAG/Pyspark Job completed to success.


**Required Permissions grants for Default Service Account in GCP:**

Please make sure to include below roles in the GCP default service account you are using in the Airflow setup to avoid any access issues during the DAG execution process and Dataproc Cluster creation process


<img width="885" height="552" alt="image" src="https://github.com/user-attachments/assets/3417c3c2-1c6d-4239-8c49-1ce16c1036a5" />


**Spark code Python File URL:**

https://github.com/ViinayKumaarMamidi/GCP_Airflow_Dataproc_Pyspark_Project/blob/main/emp_batch_job.py

**Airflow DAG File URL:**

https://github.com/ViinayKumaarMamidi/GCP_Airflow_Dataproc_Pyspark_Project/blob/main/airflow_spark_job.py


**End to End Airflow Dag:**

<img width="1421" height="629" alt="image" src="https://github.com/user-attachments/assets/d6618579-1ac7-4865-bff9-ffd5e7a5a044" />


**GCS Bucket Structure:**

<img width="1412" height="392" alt="image" src="https://github.com/user-attachments/assets/0f8bd70f-bc28-418e-b947-a0e8fcddf079" />




