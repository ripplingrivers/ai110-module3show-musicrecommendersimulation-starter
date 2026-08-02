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

Loaded total repository assets: 87 tracks.

==================================================
👤 PROFILE: High-Energy Pop
   Targets: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85}
==================================================
1. Rock Me by One Direction (pop/happy)
   ↳ Adjusted Match Score: 6.00 / 6.00
   ↳ System Ledger Trace: genre match (+2.0), mood match (+1.0), energy proximity match (+3.00)
--------------------------------------------------
2. Timber by Pitbull & Kesha (pop/happy)
   ↳ Adjusted Match Score: 5.47 / 6.00
   ↳ System Ledger Trace: genre match (+2.0), mood match (+1.0), energy proximity match (+2.97), diversity penalty: genre clustering (-0.5)
--------------------------------------------------
3. Finesse by Bruno Mars & Cardi B (pop/happy)
   ↳ Adjusted Match Score: 5.47 / 6.00
   ↳ System Ledger Trace: genre match (+2.0), mood match (+1.0), energy proximity match (+2.97), diversity penalty: genre clustering (-0.5)
--------------------------------------------------
4. Bad Habits by Ed Sheeran (pop/happy)
   ↳ Adjusted Match Score: 5.38 / 6.00
   ↳ System Ledger Trace: genre match (+2.0), mood match (+1.0), energy proximity match (+2.88), diversity penalty: genre clustering (-0.5)
--------------------------------------------------
5. Run by OneRepublic (pop/happy)
   ↳ Adjusted Match Score: 5.29 / 6.00
   ↳ System Ledger Trace: genre match (+2.0), mood match (+1.0), energy proximity match (+2.79), diversity penalty: genre clustering (-0.5)
--------------------------------------------------

==================================================
👤 PROFILE: Chill Lofi
   Targets: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35}
==================================================
1. Harpy Hare by Yaelokre (folk/chill)
   ↳ Adjusted Match Score: 4.00 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+3.00)
--------------------------------------------------
2. Headlock by Imogen Heap (pop/chill)
   ↳ Adjusted Match Score: 3.70 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.70)
--------------------------------------------------
3. Sometimes by Mattyeux & Princess Chelsea (indie/chill)
   ↳ Adjusted Match Score: 3.52 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.52)
--------------------------------------------------
4. Toes by Glass Animals (indie pop/chill)
   ↳ Adjusted Match Score: 3.43 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.43)
--------------------------------------------------
5. forwards beckon rebound by Adrianne Lenker (folk/chill)
   ↳ Adjusted Match Score: 3.41 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.91), diversity penalty: genre clustering (-0.5)
--------------------------------------------------

==================================================
👤 PROFILE: Adversarial Rock Cluster
   Targets: {'genre': 'synthwave', 'mood': 'moody', 'energy': 0.9}
==================================================
1. Demons by Imagine Dragons (rock/moody)
   ↳ Adjusted Match Score: 3.43 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.43)
--------------------------------------------------
2. Carousel by Neoni (pop/moody)
   ↳ Adjusted Match Score: 3.40 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.40)
--------------------------------------------------
3. Take Me to Church by Hozier (indie rock/moody)
   ↳ Adjusted Match Score: 3.28 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.28)
--------------------------------------------------
4. Somebody that I Used to Know by Gotye & Kimbra (indie pop/moody)
   ↳ Adjusted Match Score: 3.25 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.25)
--------------------------------------------------
5. He's My Man by Luvcat (indie/moody)
   ↳ Adjusted Match Score: 3.04 / 6.00
   ↳ System Ledger Trace: mood match (+1.0), energy proximity match (+2.04)
--------------------------------------------------

📊 SYSTEM RELIABILITY SUMMARY MATRIX:
Profile Name | Items Count | Diversity Failure Check
High-Energy Pop | 5 | False
Chill Lofi | 5 | False
Adversarial Rock Cluster | 5 | False


---

## Experiments You Tried

I wanted to see how sensitive this whole system was, so I ended up trying a few different experiments to see what would happen to the rankings:

1. **The Base Version**: At first, I just ran the normal point system. It worked mathematically, but I noticed that it immediately fell into some heavy "filter bubbles". It kept suggesting the exact same artist (`Neon Echo`) over and over in the top spots just because the first couple of songs matched perfectly. 

2. **The Acoustic Booster**: Since the `acousticness` data was just sitting there unused in the CSV, I added a quick `+0.5` booster if a user says they like acoustic sounds and the song is above 0.6. This actually worked pretty well, since it finally pushed some folk and ambient tracks up into the recommendations. 

3. **The Agentic Critique Loop**: To fix the repetitive artist issue, I built a secondary check where the system looks at its own playlist draft. If it sees the same artist or genre showing up too much, it applies a penalty right then and there (`-1.5` for duplicate artists, `-0.5` for genre clustering) and completely re-sorts the list. This probably made the biggest difference because it actually forced the system to offer some variety. 

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

Building this project really showed me that turning data into predictions involves a lot more human bias than people probably think. I used to think algorithms had to be objective since they were just programs, but now I believe it’s mostly just a developer making highly personal choices; like deciding a genre match is worth exactly 2.0 points while a mood match is worth 1.0. If you change those numbers even a little bit, the whole output shifts completely, which means the "vibe" is really just whatever the programmer decided it should be.

I think algorithmic bias usually happens naturally when your data is small or your rules are too rigid. In a smaller catalog like this, a simple content-matching loop gets stuck in a loop of predictability super easily. Without adding that extra agentic layer to actively critique the playlist and penalize repetition, I think any automated system will just end up creating a boring echo chamber for the user.




