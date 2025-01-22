import unittest
import pandas as pd

class TestCleanAndTransform(unittest.TestCase):
    def test_radio_mix_column(self):
        """Test the 'radio_mix' column calculation."""
        
        # Sample input data for the albums DataFrame
        albums_data = {
            'track_id': [1, 2],
            'duration_sec': [180, 300]  # First one <= 3 minutes, second one > 3 minutes
        }
        
        # Create a DataFrame for albums
        albums_df = pd.DataFrame(albums_data)
        
        # Apply the 'radio_mix' column transformation
        albums_df['radio_mix'] = albums_df['duration_sec'].apply(lambda x: x / 60 <= 3)
        
        # Check the expected results
        self.assertTrue(albums_df.loc[0, 'radio_mix'])  # First row should be True
        self.assertFalse(albums_df.loc[1, 'radio_mix'])  # Second row should be False

if __name__ == '__main__':
    unittest.main()
