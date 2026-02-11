import re
from datetime import date


def artist_md_builder():
    print("--- MacheteBath Artist MD Builder ---")
    print("Paste the SoundCloud embed code and press Enter:")
    embed_code = input("> ")

    # 1. Extract the Track ID
    id_match = re.search(r'tracks(?:%253A|/)(?:soundcloud%253Atracks%253A)?(\d+)', embed_code)

    # 2. Extract Artist Name (usually found in the title or link text)
    # This looks for the text between the <a> tags SoundCloud provides
    artist_match = re.search(r'href="https://soundcloud.com/.*?>(.*?)</a>', embed_code)

    # 3. Extract Track Title
    # This looks for the second <a> tag which is usually the track name
    track_match = re.findall(r'href="https://soundcloud.com/.*?>(.*?)</a>', embed_code)

    if id_match:
        track_id = id_match.group(1)
        # Handle cases where the regex might miss the specific names
        artist_name = artist_match.group(1) if artist_match else "Artist Name"
        # track_match[1] is usually the song title in the embed HTML
        track_title = track_match[1] if len(track_match) > 1 else "Track Title"

        today = date.today().strftime("%Y-%m-%d")
        formatted_url = f'\"https%3A//api.soundcloud.com/tracks/{track_id}\"'

        print("\nEnter the artist bio or blurb:")
        blurb = input("> ")

        print(f"\n--- COPY THE BLOCK BELOW INTO YOUR NEW .MD FILE ---")
        print("---")
        print(f'name: "{artist_name}"')
        print(f"date: {today}")
        print(f'track_title: "{track_title}"')
        print(f"sc_url: {formatted_url}")
        print("---")
        print(f"\n{blurb}")
        print(f"\n--- END OF FILE ---")
    else:
        print("\nError: Could not find the required data in the embed code.")


if __name__ == "__main__":
    artist_md_builder()