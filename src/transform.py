import pandas as pd

def clean_and_transform():
    """Clean and transform the Spotify dataset."""
    # Load datasets
    albums = pd.read_csv("data/spotify-albums_data_2023.csv")
    tracks = pd.read_csv("data/spotify_tracks_data_2023.csv")
    
    # Drop unnecessary columns
    columns_to_drop = ["album_type", "artist_0", "artist_1", "artist_2", "artist_3",
                       "artist_4", "artist_5", "artist_6", "artist_7", "artist_8", "artist_9",
                       "artist_10", "artist_11"]
    albums.drop(columns=columns_to_drop, inplace=True)
    
    # Add 'radio_mix' column
    albums["radio_mix"] = albums["duration_sec"].apply(lambda x: x / 60 <= 3)
    
    # Merge the datasets on track_id and id
    merged = albums.merge(tracks, left_on="track_id", right_on="id")
    
    # Filter data
    filtered = merged[(merged["explicit"] == False) & (merged["track_popularity"] > 50)]
    
    # Save transformed data
    filtered.to_csv("data/transformed_spotify_data.csv", index=False)

if __name__ == "__main__":
    clean_and_transform()
