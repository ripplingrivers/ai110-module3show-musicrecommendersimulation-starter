"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def run_experiment(profile_name: str, user_prefs: dict, songs: list) -> None:
    """Helper function to run and print recommendations for a specific profile."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n==================================================")
    print(f"👤 PROFILE: {profile_name}")
    print(f"   Targets: {user_prefs}")
    print("==================================================")
    
    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{rank}. {song['title']} by {song['artist']} ({song['genre']}/{song['mood']})")
        print(f"   ↳ Final Match Score: {score:.2f} / 6.00")
        print(f"   ↳ Reasons: {explanation}")
        print("-" * 50)


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    profile_a = {"genre": "pop", "mood": "happy", "energy": 0.85}
    
    profile_b = {"genre": "lofi", "mood": "chill", "energy": 0.35}
    
    profile_c = {"genre": "rock", "mood": "moody", "energy": 0.90}

    run_experiment("High-Energy Pop", profile_a, songs)
    run_experiment("Chill Lofi", profile_b, songs)
    run_experiment("Conflicting Edge Case (Intense/Moody Rock)", profile_c, songs)


if __name__ == "__main__":
    main()
