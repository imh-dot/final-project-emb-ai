from EmotionDetection import emotion_detector

def test_emotion_detection():
    tests = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected in tests.items():
        result = emotion_detector(statement)
        dominant = result["dominant_emotion"]
        print(f"Statement: {statement}")
        print(f"Expected: {expected}, Got: {dominant}")
        print("PASS" if dominant == expected else " FAIL")
        print("-" * 50)

if __name__ == "__main__":
    test_emotion_detection()