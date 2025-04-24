
MoodGarden is a CLI-based emotional wellbeing tracker. It lets you log your mood, journal your thoughts, and get well-being suggestions based on your emotional state.

## 🚀 Features
- Daily mood journaling
- Simple mood-based sentiment analysis
- Self-care suggestions
- View saved entries anytime

## 🔧 Requirements
- Python 3.8+
- `pip install typer rich`

## 💻 Installation
```bash
git clone https://github.com/yourname/moodgarden
cd moodgarden
pip install -r requirements.txt
```

## 🏃‍♂️ Usage
```bash
python main.py start
```

## 🧠 OOP Principles Used
- **Encapsulation**: Each component handles its own logic.
- **Abstraction**: Complex behavior like mood analysis and suggestions hidden inside `MoodEntry`.
- **Polymorphism**: Could be extended for custom mood categories with different strategies.
- **Inheritance**: Could be used to build AI-based entries extending `MoodEntry`.

## Example:
```
How are you feeling today? calm
Write a journal: It was a peaceful day, I read a book and relaxed.
Mood Analysis: balanced
Suggestion: Try a short walk or meditation to maintain the balance.
```

---
Stay grounded 🌱
