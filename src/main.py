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

    print("\n" + "="*50)
    print(f"👤 PROFILE: {profile_name}")
    print(f"   Targets: {user_prefs}")
    print("="*50)

    artists_seen = set()
    has_duplicates = False
    
    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{rank}. {song['title']} by {song['artist']} ({song['genre']}/{song['mood']})")
        print(f"   ↳ Final Match Score: {score:.2f} / 6.00")
        print(f"   ↳ Reasons: {explanation}")
        print("-" * 50)

        if song['artist'] in artists_seen:
            has_duplicates = True
        artists_seen.add(song['artist'])

    return {
        "profile": profile_name,
        "items_returned": len(recommendations),
        "fails_diversity_guard": has_duplicates
    }



def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded total repository assets: {len(songs)} tracks.")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.85}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.35}),
        ("Adversarial Rock Cluster", {"genre": "synthwave", "mood": "moody", "energy": 0.90})
    ]

    summary_metrics = []
    for name, prefs in profiles:
        metrics = run_experiment(name, prefs, songs)
        summary_metrics.append(metrics)
        
    print("\n📊 SYSTEM RELIABILITY SUMMARY MATRIX:")
    print("Profile Name | Items Count | Diversity Failure Check")
    for sm in summary_metrics:
        print(f"{sm['profile']} | {sm['items_returned']} | {sm['fails_diversity_guard']}")


if __name__ == "__main__":
    main()
