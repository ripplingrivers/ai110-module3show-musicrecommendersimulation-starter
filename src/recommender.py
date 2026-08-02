import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
            user_prefs = {
                "genre": user.favorite_genre,
                "mood": user.favorite_mood,
                "energy": user.target_energy,
                "acoustic": user.likes_acoustic
            }
            raw_songs = []
            for s in self.songs:
                raw_songs.append({
                    "id": s.id, "title": s.title, "artist": s.artist,
                    "genre": s.genre, "mood": s.mood, "energy": s.energy,
                    "tempo_bpm": s.tempo_bpm, "valence": s.valence,
                    "danceability": s.danceability, "acousticness": s.acousticness
                })

            # Run the agent recommendation loop
            ranked_tuples = recommend_songs(user_prefs, raw_songs, k=k)

            # Unpacks back to Song objects
            output_songs = []
            for r in ranked_tuples:
                song_dict = r[0]
                match = next((s for s in self.songs if s.id == song_dict["id"]), None)
                if match:
                    output_songs.append(match)
            return output_songs


    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy
        }
        song_dict = {
            "genre": song.genre, "mood": song.mood, "energy": song.energy
        }
        _, reasons = score_song(user_prefs, song_dict)
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                songs.append({
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"].strip().lower(),
                    "mood": row["mood"].strip().lower(),
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"])
                })
    except FileNotFoundError:
        print(f"Warning: File {csv_path} not found.")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    target_genre = user_prefs.get("genre", "").strip().lower()
    if song["genre"] == target_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    target_mood = user_prefs.get("mood", "").strip().lower()
    if song["mood"] == target_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = user_prefs.get("energy", 0.5)
    energy_distance = abs(target_energy - song["energy"])
    energy_points = 3.0 * (1.0 - energy_distance)
    score += energy_points
    reasons.append(f"energy proximity match (+{energy_points:.2f})")

    # A Guardrail system expansion matching the final metrics
    if "acoustic" in user_prefs and user_prefs["acoustic"] and song["acousticness"] > 0.6:
        score += 0.5
        reasons.append("acoustic booster (+0.5)")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    AGENTIC LOOP IMPLEMENTATION:
    Generates suggestions, critiques choices for filter bubble clustering,
    and scales individual rankings dynamically using real-time array tracking.
    """
    scored_list = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_list.append((song, score, list(reasons)))
    
    ranked_list = sorted(scored_list, key=lambda x: x[1], reverse=True)
    
    # --- An Agent Critique Block ---
    # First Pass: Apply penalties dynamically based on what would be selected
    penalized_list = []
    seen_artists = set()
    seen_genres = set()
    
    for song, score, reasons in ranked_list:
        adjusted_score = score
        
        # Injects dynamic evaluation penalties to break filter bubbles (basically, makes the process less mechanical)
        if song["artist"] in seen_artists:
            adjusted_score -= 1.5
            reasons.append("diversity penalty: duplicate artist (-1.5)")
        if song["genre"] in seen_genres:
            adjusted_score -= 0.5
            reasons.append("diversity penalty: genre clustering (-0.5)")
            
        penalized_list.append((song, round(adjusted_score, 2), ", ".join(reasons)))
        
        # Simulating the window: if this song is high enough to be considered,
        # its properties affect downstream variety choices
        seen_artists.add(song["artist"])
        seen_genres.add(song["genre"])
            
    final_playlist = sorted(final_playlist, key=lambda x: x[1], reverse=True)
    return final_playlist[:k]
