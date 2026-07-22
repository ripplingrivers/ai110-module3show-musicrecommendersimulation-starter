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

### Scoring & Selection Mechanics
1. **Scoring Rule**: To evaluate a single song, I think a weighted point system makes the most sense. For categorical things like genre or mood, it's a simple match or mismatch. But for numerical values like energy, I think we need a calculation that rewards a song for being *close* to the preference, rather than just being high or low. So, I'm using an absolute distance formula to see how far off the track is, and subtracting that from a maximum point value.
2. **Ranking Rule**: Once a single song can be scored, the system needs a way to handle the whole list. I believe the ranking rule is just the broader process of running every song through that scoring formula, sorting the whole catalog from highest to lowest score, and then pulling out the top `k` results to show the user. 


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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

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



