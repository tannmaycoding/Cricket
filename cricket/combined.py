from batting.overall_shot_detection import CricketShotClassifier
from balling.overall_bowl_detection import CricketBallAnalyzer
import utils


def classify_overall(video, ball_colour, pitch_length):
    bat = CricketShotClassifier()
    bat_decision = bat.classify_entire_video(video)
    ball_decision = CricketBallAnalyzer(video, utils.color_ranges[ball_colour][0], utils.color_ranges[1], pitch_length)
    return {"ball": ball_decision, "bat": bat_decision}
