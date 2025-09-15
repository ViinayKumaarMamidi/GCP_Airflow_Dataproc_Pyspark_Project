from pyspark.sql import SparkSession

def process_data():
    spark = SparkSession.builder.appName("GCPDataprocJob").getOrCreate()

    # Define your GCS bucket and paths
    # GCP Project Name: XXXXXXX
    # Bucket Name: XXXXX

    bucket = "XXXXX"
           
    # Defining Variabls for emp, dept and output files paths: 
    
    emp_data_path = f"gs://{bucket}/data/employee.csv"
    dept_data_path = f"gs://{bucket}/data/department.csv"
    output_path = f"gs://{bucket}/output"


    # Read Employee datasets using Spark 
    
    employee = spark.read.csv(emp_data_path, header=True, inferSchema=True)
    
    # Read Deparment datasets using Spark 
    
    department = spark.read.csv(dept_data_path, header=True, inferSchema=True)


    # Filter employee data
    
    filtered_employee = employee.filter(employee.salary > 50000) # Adjust the salary threshold as needed

    # Joining emp and dept datasets based on the key "dept_id"
    
    joined_data = filtered_employee.join(department, "dept_id", "inner")


    # Writing the final joined_data data frame into CSV file into the output folder location: 
    
    joined_data.write.csv(output_path, mode="overwrite", header=True)
    
    print(f"Final data has been uploaded in to the GCS Bucket folder: {output_path}" )

    
    spark.stop()

if __name__ == "__main__":
    process_data()