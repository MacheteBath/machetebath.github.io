import re
import os
from datetime import date


def artist_md_builder():
    print("--- MacheteBath Artist MD Builder ---")
    print("Paste the SoundCloud embed code and press Enter:")
    embed_code = input("> ")

    # 1. Extract the Track ID
    id_match = re.search(r'tracks(?:%253A|/)(?:soundcloud%253Atracks%253A)?(\d+)', embed_code)

    # 2. Extract Artist Name and Track Title
    artist_match = re.search(r'href="https://soundcloud.com/.*?>(.*?)</a>', embed_code)
    track_matches = re.findall(r'href="https://soundcloud.com/.*?>(.*?)</a>', embed_code)

    if id_match:
        track_id = id_match.group(1)
        artist_name = artist_match.group(1) if artist_match else "Unknown Artist"
        track_title = track_matches[1] if len(track_matches) > 1 else "Unknown Track"

        today = date.today().strftime("%Y-%m-%d")
        formatted_url = f'\"https%3A//api.soundcloud.com/tracks/{track_id}\"'

        print(f"\nEnter the bio/blurb for {artist_name}:")
        blurb = input("> ")

        # Create the Front Matter content
        content = f"""---
name: "{artist_name}"
date: {today}
track_title: "{track_title}"
sc_url: {formatted_url}
---

{blurb}
"""
        # 3. Generate a safe filename
        # Removes spaces/special chars and makes it lowercase
        clean_name = re.sub(r'[^a-zA-Z0-9]', '-', artist_name.lower().strip()).strip('-')
        filename = f"{today}-{clean_name}.md"

        # 4. Save to the _artists folder
        # We use '../_artists/' because the script is inside the 'tools/' folder
        filepath = os.path.join("..", "_artists", filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"\nSUCCESS: Created {filepath}")
        except Exception as e:
            print(f"\nERROR saving file: {e}")
            # Fallback: Print it anyway so you don't lose the work
            print(content)

    else:
        print("\nError: Could not find the required data in the embed code.")


if __name__ == "__main__":
    artist_md_builder()