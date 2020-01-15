from unittest import TestCase

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
YEAR = DAY * 365

def sentence_part(number: int, word: str) -> str:
    if number == 1:
        return f"{number} {word}"
    else:
        return f"{number} {word}s"

def format_duration(seconds):
    sentence_parts = []
    years = seconds // YEAR
    if years:
        sentence_parts.append(sentence_part(years, "year"))
    seconds = seconds % YEAR
    days = seconds // DAY
    if days:
        sentence_parts.append(sentence_part(days, "day"))
    seconds = seconds % DAY
    hours = seconds // HOUR
    if hours:
        sentence_parts.append(sentence_part(hours, "hour"))
    seconds = seconds % HOUR
    minutes = seconds // MINUTE
    if minutes:
        sentence_parts.append(sentence_part(minutes, "minute"))
    seconds = seconds % MINUTE
    if seconds:
        sentence_parts.append(sentence_part(seconds, "second"))
    if sentence_parts:
        if len(sentence_parts) == 1:
            return sentence_parts[0]
        else:
            return f"{', '.join(sentence_parts[0:-1])} and {sentence_parts[-1]}"
    return "now"




class PowerTest(TestCase):
    def test(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")

