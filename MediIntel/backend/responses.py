# backend/responses.py

def get_bot_response(message):
    msg = message.lower()

    if "fever" in msg:
        return "It sounds like you may have a fever. Rest, drink fluids, and monitor your temperature."

    elif "headache" in msg:
        return "A headache can have many causes — try drinking water and resting."

    elif "emergency" in msg:
        return "If this is a medical emergency, call emergency services immediately."

    elif "mri" in msg:
        return "Please upload your MRI scan for further analysis."

    elif "skin" in msg:
        return "Please upload your skin image for visual analysis."
    elif "Frequent urination"or "excessive thirst" or "fatigue, blurred vision" in msg:
        return "These could be symptoms of diabetes. It's best to consult a healthcare professional for proper diagnosis."
    elif "diabetes" in msg:
        return "If you suspect diabetes, please consult a healthcare professional for proper diagnosis and management."
    elif "cough" in msg or "cold" in msg:
        return "For a cough or cold, rest and stay hydrated. If symptoms persist, see a doctor."    
    elif "allergy" in msg:
        return "If you have an allergy, try to avoid the allergen and consider taking antihistamines if needed."
    else:
        return "I'm not sure about that. Could you describe your symptoms in more detail?"
