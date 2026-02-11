import re
from datetime import date


def extract_soundcloud_id():
    print("Paste the SoundCloud embed code and press Enter:")
    embed_code = input("> ")

    # Matches the ID number from the embed code
    match = re.search(r'tracks(?:%253A|/)(?:soundcloud%253Atracks%253A)?(\d+)', embed_code)

    if match:
        track_id = match.group(1)
        today = date.today().strftime("%Y-%m-%d")
        # Formats exactly as your .md expects with quotes
        formatted_url = f'\"https%3A//api.soundcloud.com/tracks/{track_id}\"'

        print(f"\n--- Copy these lines into your .md Front Matter ---")
        print(f"date: {today}")
        print(f"sc_url: {formatted_url}")
    else:
        print("\nError: Could not find the track ID.")


if __name__ == "__main__":
    extract_soundcloud_id()