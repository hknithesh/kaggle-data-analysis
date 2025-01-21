import sqlite3
import pandas as pd

def load_to_sqlite():
    """Load the transformed data into SQLite."""
    # Read the transformed data
    df = pd.read_csv("data/transformed_spotify_data.csv")
    db_name='spotify_data.db' # Changed to use spotify_data.db instead of spotify.db
    
    # Connect to SQLite database, using the same db_name 
    conn = sqlite3.connect(db_name)  
    cursor = conn.cursor()
    
    # Insert data
    df.to_sql("spotify_data", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_to_sqlite()
