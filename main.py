from src.extract import download_data
from src.transform import clean_and_transform
from src.load import load_to_sqlite
from src.visualization import visualize_data

def main():
    """Run the ETL pipeline locally."""
    print("Starting ETL pipeline...")
    download_data()
    print("Data downloaded.")
    
    clean_and_transform()
    print("Data cleaned and transformed.")
    
    load_to_sqlite()
    print("Data loaded into SQLite.")
    
    visualize_data()
    print("Query Results Completed.")

if __name__ == "__main__":
    main()
