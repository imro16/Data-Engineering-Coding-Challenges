# CSV Data Anonymization Project

## Overview
This project demonstrates how to generate a CSV file containing personal data, anonymize specific columns, and scale the anonymization process to handle large datasets using a distributed computing platform like Apache Spark.

## Files in the Repository

### 1. `generate_csv.py`
This script generates a CSV file with the columns `first_name`, `last_name`, `address`, and `date_of_birth`. The file is saved as `data.csv`.

### 2. `anonymize_csv.py`
This script anonymizes the `first_name`, `last_name`, and `address` columns of the `data.csv` file using SHA-256 hashing. The output is saved as `anonymized_data.csv`.

### 3. `anonymize_csv_spark.py`
This script performs the same anonymization as `anonymize_csv.py` but is optimized for large datasets using Apache Spark. The output is saved as `anonymized_data_spark.csv`.

## How to Run

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `faker` (for generating fake data)
  - `pyspark` (for distributed processing using Spark)
- Apache Spark (if running the Spark version)

### Installation
To install the necessary Python libraries, you can use pip:

```sh
pip install faker pyspark
```

### Step 1: Generate the CSV File

To generate a CSV file with sample data:

```sh
python generate_csv.py
```

This will create a file named `data.csv` with the specified number of rows.

### Step 2: Anonymize the CSV File

#### Option 1: Anonymize on a Single Machine

For small to medium-sized datasets, you can anonymize the data using the following command:

```sh
python anonymize_csv.py
```

This will create a file named `anonymized_data.csv` with the `first_name`, `last_name`, and `address` columns anonymized.

#### Option 2: Anonymize Using PySpark

For large datasets (e.g., >2GB), it is recommended to use Apache Spark for distributed processing:

```sh
python anonymize_csv_spark.py
```

This will create a directory named `anonymized_data_spark.csv` containing the anonymized CSV files.

## Scaling the Solution

For datasets larger than what can comfortably fit into a single machine’s memory, use the PySpark version (`anonymize_csv_spark.py`). Apache Spark distributes the data processing across multiple nodes, making it suitable for handling large-scale data efficiently.

## Project Structure

```
csv-anonymization-project/
│
├── generate_csv.py              # Script to generate the initial CSV file
├── anonymize_csv.py             # Script to anonymize the CSV file on a single machine
├── anonymize_csv_spark.py       # Script to anonymize the CSV file using PySpark
├── README.md                    # Project documentation
└── data/                        # Folder for generated CSV files (optional)
    ├── data.csv                 # Generated CSV file with sample data
    ├── anonymized_data.csv       # Anonymized CSV file (single machine version)
    └── anonymized_data_spark.csv # Anonymized CSV file (Spark version)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can customize the README as per your specific requirements, especially if you include sample files or additional documentation. This file should give a clear understanding of the project and instructions on how to use the provided scripts.
