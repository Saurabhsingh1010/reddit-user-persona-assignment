
# Reddit User Persona Generator 

This project is a coding assignment for the Generative AI Internship at BeyondChats.  
It extracts Reddit user data and generates a user persona with cited references.

---

##  Project Structure

```
.
├── scrape_user_data.py         # Script to extract posts and comments from Reddit users
├── kojied.txt                  # Raw Reddit data for user u/kojied
├── persona_kojied_final.txt    # Generated persona for user u/kojied
├── Hungry-Move-6603.txt        # Raw Reddit data for user u/Hungry-Move-6603
├── persona_hungry_move_6603.txt# Generated persona for user u/Hungry-Move-6603
└── README.md                   # Project instructions and description
```

---

##  How to Run

1. **Clone this repo** or download the `.zip`.
2. Install required Python package:

```bash
pip install praw
```

3. Update your `client_id`, `client_secret`, and `user_agent` in `scrape_user_data.py`:

```python
client_id = "your_client_id"
client_secret = "your_client_secret"
user_agent = "your_user_agent"
```

4. Run the script to fetch data from Reddit:

```bash
python scrape_user_data.py
```

This will generate a `.txt` file containing user posts/comments.

5. Based on that data, the script (or manual analysis) is used to write a `persona_<username>.txt` file.

---

## Example Output

Persona files include:
- Location guess
- Profession guess
- Interests
- Personality traits
- Writing style
- Cited insights from Reddit

---

##  Completed Users
- `u/kojied`
- `u/Hungry-Move-6603`

---

##  Submission Notes

This repo includes:
-  Python script
-  Raw data files (`<username>.txt`)
-  Persona files with citation
-  README with setup instructions

---

##  Disclaimer
This code and data are shared only for evaluation as part of the internship assignment. The Reddit content belongs to respective users.

