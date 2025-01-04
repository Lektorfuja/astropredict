import random

# List of zodiac signs
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# List of random predictions
predictions = [
    "Today is a great day to take on new challenges.",
    "You might find unexpected financial opportunities.",
    "A deep conversation could strengthen your relationships.",
    "Stay open to learning something new today.",
    "Your creativity is at its peak, use it wisely.",
    "An old friend might reconnect with you.",
    "Focus on self-care; your body will thank you.",
    "A small risk today might lead to great rewards.",
    "Patience will help you resolve a tricky situation.",
    "A pleasant surprise is on its way.",
    "Someone might look to you for advice or support.",
    "Trust your instincts—they will guide you well."
]

# Function to generate predictions
def generate_predictions():
    daily_predictions = {}
    for sign in zodiac_signs:
        prediction = random.choice(predictions)
        daily_predictions[sign] = prediction
    return daily_predictions

# Generate and display predictions
if __name__ == "__main__":
    print("🌟 Daily Astrological Predictions 🌟\n")
    daily_predictions = generate_predictions()
    for sign, prediction in daily_predictions.items():
        print(f"{sign}: {prediction}")
