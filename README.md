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

## How I Would Explain to Students:
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
-End by reflecting on how this assignment shaped your understanding of AI-generated code and your role in reviewing it.



## 📸 Demo

- [] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
