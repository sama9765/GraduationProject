# agent/emotion_agent.py

def emotion_aware_response(emotion):
    """
    Emotion-Aware AI Agent:
    Responds with empathy + practical guidance based on detected emotion
    """

    if emotion == "sadness":
        return (
            "I can sense that you’re feeling low, and that’s completely okay. "
            "Try taking a short walk, listening to calming music, or talking to someone you trust. "
            "You don’t have to go through this alone, and small steps can really help."
        )

    elif emotion == "anger":
        return (
            "I sense a lot of frustration right now. Let’s pause for a moment. "
            "Try taking a few deep breaths or stepping away from the situation briefly. "
            "Once you feel calmer, things often become clearer."
        )

    elif emotion == "fear":
        return (
            "Feeling scared can be overwhelming, but remember that fear does not mean failure. "
            "Try grounding yourself by focusing on what you can control right now. "
            "Break the problem into small steps, and don’t hesitate to ask for support."
        )

    elif emotion == "joy":
        return (
            "That’s really great to hear! I’m glad you’re feeling happy. "
            "Take a moment to enjoy this feeling and celebrate your progress. "
            "Sharing this joy with friends or loved ones can make it even more meaningful."
        )

    elif emotion == "disgust":
        return (
            "That sounds uncomfortable and unpleasant. It’s okay to distance yourself from things "
            "that make you feel this way. Focus on something that brings you comfort or positivity."
        )

    elif emotion == "surprise":
        return (
            "That sounds unexpected! Surprises can be confusing at first, but they often bring new perspectives. "
            "Take some time to reflect — you might discover something valuable from this experience."
        )

    else:  # neutral
        return (
            "Thank you for sharing your thoughts. If there’s anything specific you’d like to talk about, "
            "I’m here to listen and help however I can."
        )

