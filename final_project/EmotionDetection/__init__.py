"""
EmotionDetection package
Exposes: emotion_detector(text_to_analyze) -> dict
"""

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
__version__ = "1.0.0"