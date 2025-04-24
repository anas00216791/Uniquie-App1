
from datetime import datetime

class MoodEntry:
    def __init__(self, mood, journal):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.mood = mood
        self.journal = journal

    def analyze(self):
        mood_map = {
            "happy": "positive",
            "calm": "balanced",
            "sad": "low energy",
            "angry": "high tension",
            "anxious": "unsettled"
        }
        return mood_map.get(self.mood.lower(), "neutral")

    def suggest(self):
        suggestions = {
            "positive": "Keep up the great mood! Maybe share your joy with someone.",
            "balanced": "Try a short walk or meditation to maintain the balance.",
            "low energy": "Consider journaling more or listening to calm music.",
            "high tension": "Deep breathing or stretching might help.",
            "unsettled": "Try writing your thoughts out more or a 5-minute focus task.",
            "neutral": "Track your mood for a few days to detect patterns."
        }
        return suggestions.get(self.analyze(), "Reflect and take a break if needed.")

    def to_dict(self):
        return {
            "date": self.date,
            "mood": self.mood,
            "journal": self.journal,
            "analysis": self.analyze(),
            "suggestion": self.suggest()
        }

