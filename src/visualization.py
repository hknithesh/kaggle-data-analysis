import pandas as pd
import sqlite3

def visualize_data():
    db_name='spotify_data.db'
    conn = sqlite3.connect(db_name) # Re-using the same db_name for querying
    cursor = conn.cursor()
    
    # Top 20 labels with track counts
    query_labels = """
    SELECT label, COUNT(*) as track_count
    FROM spotify_data
    GROUP BY label
    ORDER BY track_count DESC
    LIMIT 20;
    """
    top_labels = pd.read_sql_query(query_labels, conn)
    print("Top 20 Labels by Track Count:\n", top_labels)
    
    print("----------------------------------------------------------------------------------------------------------")
    
    # Top 25 popular tracks (2020-2023)
    query_tracks = """
    SELECT track_name, track_popularity, release_date
    FROM spotify_data
    WHERE release_date BETWEEN '2020-01-01' AND '2023-12-31'
    ORDER BY track_popularity DESC
    LIMIT 25;
    """
    top_tracks = pd.read_sql_query(query_tracks, conn)
    print("Top 25 Popular Tracks (2020-2023):\n", top_tracks)
    
    conn.close()

if __name__ == "__main__":
    visualize_data()