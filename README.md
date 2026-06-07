# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
- [X] Detail which bugs you found.
- [X] Explain what fixes you applied.

<!-- ## How I Would Explain to Students:
Describe the first issues you noticed when you ran the game. Explain:
- what the app was doing
- what you expected it to do instead
- why the behavior felt wrong or unreliable
Focus on concrete examples, such as incorrect hints, inconsistent reset behavior, attempt counter issues,or type mismatches in the game logic.

Explain how you used AI during the debugging process. Be specific about:
- which tool you used (for example, ChatGPT, Copilot, or both)
- one suggestion from AI that helped you move forward
- how you verified that suggestion
- one suggestion that was incomplete, misleading, or still required correction
The goal is not to say whether AI was “good” or “bad,” but to show how you evaluated its output critically.

Describe how you decided whether a bug was actually fixed. Include:
- at least one manual check you did in the Streamlit app
- at least one pytest case you ran
- how the test connected to the bug you were fixing
Make it clear how testing helped confirm the repair instead of just assuming the code worked.

Reflect on what this project taught you about how Streamlit behaves. In particular, explain:
- what it means that Streamlit reruns the script during interaction
- why st.session_state matters
- how state management affected the secret number, attempts, or reset logic
Try to explain this in a way that would make sense to another student who is new to Streamlit.

Discuss one or two habits you want to reuse in future debugging work. For example:
- testing small pieces of logic separately
- verifying AI suggestions before trusting them
- comparing expected output to actual output
- tracing bugs across multiple files
-End by reflecting on how this assignment shaped your understanding of AI-generated code and your role in reviewing it. -->

## 📋 Assignment Phases

### Phase 1: Glitch Hunt (Spot Check)

- **Identify at least 4 bugs**
  1. The secret number changes every time you click "Submit."
  2. The hints are backwards — guessing too high tells you to go "higher."
  3. You can never win, even when you guess the exact secret number.
  4. The "Reset Game" button doesn't actually give you a fresh, fixed number to guess.

- **Trace each bug to its source across the codebase**
  1. `app.py` — `secret_number = random.randint(1, 100)` sits at the top level of the script.
  2. `logic_utils.py` — `provide_hint()` returns "Go higher!" in the `guess > secret_number` branch.
  3. `logic_utils.py` — `is_game_won()` returns `guess > secret_number` instead of `guess == secret_number`.
  4. `app.py` — the reset button clears `attempts` and `game_won` but the secret number is still regenerated on the next rerun.

- **Be prepared to explain why the bug occurs**
  1. Streamlit reruns the whole script on every interaction, so the top-level `random.randint()` call generates a brand-new number each click. The value never persists because it isn't stored in `st.session_state`.
  2. The comparison branches are swapped — a guess larger than the secret should tell the player to go *lower*, but the code returns "higher."
  3. The win check uses the greater-than operator instead of equality, so an exact match (`guess == secret`) returns `False` and the game can never be won.
  4. Because the secret lives in a plain variable rather than session state, "resetting" only touches the counters; the number itself reshuffles on the next rerun, so a reset doesn't create a stable game.

### Phase 2: Investigate and Repair (Assigned)

- **Fix 2 bugs from start to finish**
  - **Bug 1 (secret resets):** Stored the secret in `st.session_state["secret"]` so it's generated once and persists across reruns instead of being recreated every click.
  - **Bug 2 (backwards hints):** Swapped the branches in `provide_hint()` so `guess > secret_number` now returns "Go lower!" and `guess < secret_number` returns "Go higher!"

- **Review at least one AI-generated code edit**
  - I asked ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"* It suggested initializing the value inside an `if "secret" not in st.session_state:` block. The suggestion was correct and I kept it, but it did not explain *why* the script reruns, so I confirmed the reasoning in the Streamlit docs before trusting it.

- **Generate and run pytest test cases successfully**
  - Wrote `test_hint_when_guess_too_high()` → `provide_hint(75, 50)` must contain "lower."
  - Wrote `test_game_won_with_correct_guess()` → `is_game_won(50, 50)` must be `True`.
  - Ran `pytest`: both tests **failed** against the broken code and **passed** after the fixes, confirming the repairs.

- **Write a short hint you would give a student to help them reach the solution**
  - *State bug:* "Streamlit reruns your whole file every click. Where could you store the secret so it survives a rerun?"
  - *Hint bug:* "If your guess is bigger than the secret, which direction should you actually go next? Read the if/else out loud."

### Phase 3: Reflection and README (Review)

- **Summary on the game and to students**
  - **The game:** A Streamlit number-guessing game where you try to find a secret number between 1 and 100. The AI-generated version is broken in four ways — the secret won't stay put, the hints point the wrong way, the win check never triggers, and reset doesn't help — which makes it a perfect target for practicing debugging and testing.
  - **To students:** Play the game first and write down exactly what's wrong with real examples (numbers and outputs), not just "it's broken." Remember that Streamlit reruns the entire script on every interaction, so anything that needs to survive a click belongs in `st.session_state`. When you fix a bug, write a test that fails before the fix and passes after — that's your proof it worked. And don't trust AI code just because it looks clean; verify every suggestion against a test or a manual check.

## 📝 Document Your Experience

- [X] **Describe the game's purpose.** A Streamlit number-guessing game: pick the secret number between 1 and 100, get higher/lower hints, track attempts, and win on a correct guess.
- [X] **Detail which bugs you found.** Secret resets every guess, backwards hints, an impossible win condition, and a reset button that doesn't fix the secret.
- [X] **Explain what fixes you applied.** Moved the secret into `st.session_state`, swapped the hint branches, changed `is_game_won()` to use `==`, and reset the secret through session state.

## How I Would Explain to Students:

**First issues I noticed.** The secret number changed on every Submit, the hints sent me the wrong way (guessed 75 vs secret 50 and was told "higher"), and an exact guess still wouldn't win. The game's basic rules kept shifting, which made it feel unreliable.

**How I used AI.** I used ChatGPT. It correctly suggested `st.session_state` for the reset bug, which I verified by clicking Submit five times and watching the debug number stay constant. It was vague on the hint logic — it said "fix the comparison" without saying which way — so I reasoned through it myself.

**How I confirmed a fix.** Manual check: replayed a high guess and saw the hint flip to "Go lower!". pytest check: `test_hint_when_guess_too_high` asserts "lower" appears in `provide_hint(75, 50)`. The test isolated the exact failing case, so passing it proved the logic was right.

**Streamlit lessons.** Streamlit reruns the whole script top-to-bottom on each interaction, so plain top-level variables reset every time. `st.session_state` is the only thing that persists across reruns. The secret and reset bugs were state problems; the hint and win bugs were pure logic.

**Habits to reuse.** Verifying AI suggestions before trusting them, and writing a test that fails on the bug and passes on the fix. This showed me AI code can look polished and still be badly broken — my job is to review and test it, not assume it works.

## 📸 Demo

(./test/glitchguess.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
