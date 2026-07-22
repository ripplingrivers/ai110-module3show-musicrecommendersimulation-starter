# 🎵 Music Recommender Simulation

## Project Summary

For this project, I am working on building a relatively straightforward, content-based music recommendation simulator. I believe the main goal here is to try and connect a user's personal taste profile with digital audio metadata from a song catalog. From what I understand, it seems to mimic some of the basic ideas behind commercial streaming algorithms—mostly by looking at the "distance" between what a user might be in the mood for and what a song actually offers, while hopefully providing a decent explanation for why each song was picked.


---

## How The System Works

I've been researching how major streaming platforms handle recommendations, and it seems like they usually rely on a mix of looking at what other people listen to (collaborative filtering) and looking closely at the traits of the songs themselves (content-based filtering). For my version, I decided to focus mostly on the content-based side of things, trying to score individual tracks against what a user explicitly says they want. 

### Feature Architecture
I decided to map out the connections between the user data and the song data using a weighted system, though I'm still adjusting how much weight each feature should get. Here is what I am considering:

*   **`Song` Data Points**: I'm looking at things like `genre` and `mood` (which seem to be clear categories), alongside numeric values like `energy` and `tempo_bpm` to capture the overall intensity.
*   **`UserProfile` Targets**: These store the user's general preferences, like `favorite_genre`, `favorite_mood`, `target_energy`, and whether they might like acoustic sounds.

### Finalized Algorithm Recipe (Max: 6.0 Points)
To evaluate how well a song matches, I've settled on a weighted point system that gives a slight edge to the overall kinetic energy of the music:
*   **Genre Match (+2.0 points)**: Gives a solid baseline bonus if the song belongs to the user's preferred genre category.
*   **Mood Match (+1.0 point)**: Adds a smaller bonus if the emotional text label aligns perfectly.
*   **Energy Proximity (Up to 3.0 points)**: This is calculated using a distance formula: `3.0 * (1.0 - abs(User_Target - Song_Energy))`. I wanted energy to hold the most weight because I think the physical intensity of a track dictates a "vibe" much more than a genre label does.

### Ranking Rule Mechanics
Once the loop evaluates every single song in our file and assigns it a final score out of 6.0, the ranking rule takes over. It gathers all those individual scores, orders the tracks from the absolute highest score to the lowest, and then extracts the top `k` recommendations to print out for the user.

### Potential Biases and System Blind Spots
I think there are a few interesting biases built into this design that are worth keeping an eye on:
1.  **Genre Dominance over Hidden Vibes**: Because a genre match gives a flat 2.0 points, an average lofi song might score significantly higher than an absolutely perfect, beautiful ambient song, simply because the ambient song lost out on the exact genre string match.
2.  **The "Middle-of-the-Road" Soft Bias**: Because our energy calculation scales based on distance, songs with moderate energy levels (around 0.50) might accidentally show up as safe, mediocre recommendations for a wide variety of users, whereas extreme songs (very high or very low energy) will only ever show up if specifically looked for.



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

==================================================
👤 PROFILE: High-Energy Pop
   Targets: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85}
==================================================
1. Sunrise City by Neon Echo (pop/happy)
   ↳ Final Match Score: 5.91 / 6.00
   ↳ Reasons: genre match (+2.0), mood match (+1.0), energy proximity match (+2.91)
--------------------------------------------------
2. Gym Hero by Max Pulse (pop/intense)
   ↳ Final Match Score: 4.76 / 6.00
   ↳ Reasons: genre match (+2.0), energy proximity match (+2.76)
--------------------------------------------------
3. Festival Fire by Glow Sticks (edm/happy)
   ↳ Final Match Score: 3.88 / 6.00
   ↳ Reasons: mood match (+1.0), energy proximity match (+2.88)
--------------------------------------------------
4. Neon Skyline by CyberPulse (synthwave/happy)
   ↳ Final Match Score: 3.79 / 6.00
   ↳ Reasons: mood match (+1.0), energy proximity match (+2.79)
--------------------------------------------------
5. Rooftop Lights by Indigo Parade (indie pop/happy)
   ↳ Final Match Score: 3.73 / 6.00
   ↳ Reasons: mood match (+1.0), energy proximity match (+2.73)
--------------------------------------------------

==================================================
👤 PROFILE: Chill Lofi
   Targets: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35}
==================================================
1. Library Rain by Paper Lanterns (lofi/chill)
   ↳ Final Match Score: 6.00 / 6.00
   ↳ Reasons: genre match (+2.0), mood match (+1.0), energy proximity match (+3.00)
--------------------------------------------------
2. Midnight Coding by LoRoom (lofi/chill)
   ↳ Final Match Score: 5.79 / 6.00
   ↳ Reasons: genre match (+2.0), mood match (+1.0), energy proximity match (+2.79)
--------------------------------------------------
3. Focus Flow by LoRoom (lofi/focused)
   ↳ Final Match Score: 4.85 / 6.00
   ↳ Reasons: genre match (+2.0), energy proximity match (+2.85)
--------------------------------------------------
4. Campfire Embers by Oak & Ivy (folk/chill)
   ↳ Final Match Score: 3.85 / 6.00
   ↳ Reasons: mood match (+1.0), energy proximity match (+2.85)
--------------------------------------------------
5. Spacewalk Thoughts by Orbit Bloom (ambient/chill)
   ↳ Final Match Score: 3.79 / 6.00
   ↳ Reasons: mood match (+1.0), energy proximity match (+2.79)
--------------------------------------------------

==================================================
👤 PROFILE: Conflicting Edge Case (Intense/Moody Rock)
   Targets: {'genre': 'rock', 'mood': 'moody', 'energy': 0.9}
==================================================
1. Storm Runner by Voltline (rock/intense)
   ↳ Final Match Score: 4.97 / 6.00
   ↳ Reasons: genre match (+2.0), energy proximity match (+2.97)
--------------------------------------------------
2. Night Drive Loop by Neon Echo (synthwave/moody)
   ↳ Final Match Score: 3.55 / 6.00
   ↳ Reasons: mood match (+1.0), energy proximity match (+2.55)
--------------------------------------------------
3. Festival Fire by Glow Sticks (edm/happy)
   ↳ Final Match Score: 2.97 / 6.00
   ↳ Reasons: energy proximity match (+2.97)
--------------------------------------------------
4. Gym Hero by Max Pulse (pop/intense)
   ↳ Final Match Score: 2.91 / 6.00
   ↳ Reasons: energy proximity match (+2.91)
--------------------------------------------------
5. Concrete Jungle by MC Cipher (hip-hop/intense)
   ↳ Final Match Score: 2.85 / 6.00
   ↳ Reasons: energy proximity match (+2.85)
--------------------------------------------------


---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



