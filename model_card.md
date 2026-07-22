# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeSeeker 1.0  


---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
  - It mostly generates basic, content-focused music suggestions by looking at how well a track's metadata matches up with what a user says they want in the moment.

- What assumptions does it make about the user  
  - It sort of seems to assume that a user's taste can be neatly summarized by a few simple choices, like a single favorite genre or a specific energy level, which might be a bit of an oversimplification of how people actually listen to music.


- Is this for real users or classroom exploration  
  - This is strictly for classroom exploration and simulation purposes, just to help understand the basic mechanics behind recommendation logic without dealing with real, massive streaming data.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
  - The system looks at text labels for the song's `genre` and `mood`, and it also uses a numerical value for its `energy` to get a sense of the track's overall intensity.

- What user preferences are considered  
  - It considers a user's favorite genre, current mood, and a target energy score on a decimal scale from 0.0 to 1.0.

- How does the model turn those into a score  
  - I ended up using a weighted point system out of 6.0 total points. If a song matches the user's genre exactly, it gets 2.0 points, and an exact mood match adds 1.0 point. For the energy, I believe a distance-based calculation works best—it checks how far away the song's energy is from the user's target and awards up to 3.0 points the closer it gets, so it rewards a song for being a good "vibe" fit rather than just being high or low.

- What changes did you make from the starter logic  
  - The original starter logic just grabbed the first few songs in the list, so I replaced that entirely with this weighted distance math and added a ranking step that sorts everything from highest score to lowest before showing the top results.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
  - Right now, there are 18 songs total in the catalog.

- What genres or moods are represented  
  - It covers a few different areas like `pop`, `lofi`, `rock`, `ambient`, `jazz`, `synthwave`, `reggae`, `classical`, `hip-hop`, and `folk`. The moods range from `happy` and `chill` to `intense`, `relaxed`, and `focused`.

- Did you add or remove data  
  - Yes, I expanded the starter dataset by adding 8 new songs with some different genres and moods to give the algorithm more variety to sort through.

- Are there parts of musical taste missing in the dataset  
  - I think a lot is missing, honestly. It doesn't capture things like lyrics, instrumentation, release eras, or cultural context, which I believe play a massive role in whether someone actually enjoys a song or not.


---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
  - It seems to work quite well for users who have very straightforward, consistent preferences, like someone who explicitly wants low-energy lofi to study to, or high-energy pop for a workout.

- Any patterns you think your scoring captures correctly  
  - I think giving energy a higher weight (3.0 points) than the text labels was a good choice because it successfully captures the actual physical intensity or pacing of a track, which keeps the overall "vibe" consistent.

- Cases where the recommendations matched your intuition  
  - When testing a standard pop profile, it placed "Sunrise City" right at the top, which felt entirely accurate based on the high energy and happy mood metrics.


---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
  - It completely ignores other built-in features like `valence` (how positive the track sounds), `danceability`, and `acousticness`, even though that data is technically sitting right there in the CSV file.

- Genres or moods that are underrepresented  
  - Because the dataset is so small, genres like classical or reggae only have one or two songs, so the system can't give much variety if someone selects them.

- Cases where the system overfits to one preference  
  - The system heavily overfits to the exact text strings for genre. If you love rock, a song labeled as "hip-hop" will lose 2.0 full points immediately, even if it has the exact intense energy and mood you are looking for.

- Ways the scoring might unintentionally favor some users  
  - I suspect the scoring might accidentally create a "middle-of-the-road" bias. Songs with moderate energy levels (around 0.50) might constantly show up as safe, average recommendations for a lot of different profiles, while more extreme tracks get buried unless a user targets them perfectly.


---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
  - I tested three separate setups: a "High-Energy Pop" lover, a "Chill Lofi" listener, and a conflicting edge case targeting "Intense, Moody Rock".

- What you looked for in the recommendations
  - I was looking closely at whether the final scores made mathematical sense and whether the system would blow up or get confused when given a profile with conflicting traits.

- What surprised you  
  - I was a bit surprised by how easily the exact genre match dominated the results. In the conflicting rock profile, an intense rock song won first place easily even though its mood was a complete mismatch, just because the 2.0 genre points insulated it from other closer mood matches.

- Any simple tests or comparisons you ran  
  - I ran a quick sensitivity experiment where I temporarily cut the genre weight in half and doubled the energy weight. It was fascinating to see how the rankings completely shifted from a strict text filter to a genuine sound-intensity matcher, which showed me how sensitive these point systems really are.


No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
  - If I kept developing this, I would definitely try to incorporate the `valence` and `acousticness` values into the distance math to make the acoustic profile feel a bit deeper. 

- Better ways to explain recommendations  
  - I think it would be nice to generate more conversational explanations instead of just printing a list of point additions, maybe saying something like, "We picked this because it matches your energy goal, even though the genre is a bit different."

- Improving diversity among the top results 
  - I believe adding a rule that limits how many songs from the same artist or genre can appear in the top 5 would help keep the final output from feeling too repetitive.

- Handling more complex user tastes  
  - Perhaps we could allow the user profile to accept a list of multiple acceptable genres or moods, rather than forcing them to pick just one strict string.


---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
  - Building this really showed me how much human bias goes into creating an algorithm. It isn't just some objective machine learning all of these things; it's also a developer making specific choices about how many points a feature should be worth, or having their own bias really. 

- Something unexpected or interesting you discovered  
  - I found it really interesting how a incredibly simple mathematical formula—just subtracting distances—can still produce a list of suggestions that genuinely feels like a personalized music recommendation.

- How this changed the way you think about music recommendation apps  
  - I think it makes me look at commercial apps like Spotify a bit differently now. It makes me realize that when an app gets stuck playing the exact same style of music over and over, it's likely just caught in a strict content-matching loop similar to the one we built here. 

