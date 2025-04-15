import cv2
import time
import RPi.GPIO as GPIO
import os
from datetime import datetime

# === CONFIGURATION ===
IR_SENSOR_PIN = 3  # GPIO pin for the IR sensor
DURATION = 5  # Recording duration in seconds
FRAME_RATE = 20.0  # Frames per second (FPS)
RESOLUTION = (640, 480)  # Video resolution
SAVE_FOLDER = "detection_videos"  # Folder to save videos

# === SETUP GPIO ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # Set as input

# === ENSURE SAVE DIRECTORY EXISTS ===
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def get_timestamp():
    """Returns the current date & time formatted for filenames."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def record_video():
    """Records a video from the webcam when an object is detected."""
    filename = f"{SAVE_FOLDER}/{get_timestamp()}.mp4"
    
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3, RESOLUTION[0])  # Set width
    video_capture.set(4, RESOLUTION[1])  # Set height

    # Define codec for MP4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for MP4 files
    video_writer = cv2.VideoWriter(filename, fourcc, FRAME_RATE, RESOLUTION)

    print(f"Recording started: {filename}")

    frame_count = 0
    max_frames = int(FRAME_RATE * DURATION)

    while frame_count < max_frames:
        ret, frame = video_capture.read()
        if ret:
            video_writer.write(frame)
            frame_count += 1
            cv2.imshow("Recording...", frame)

        # Stop recording if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"Recording finished: {filename}")

    # Release resources
    video_writer.release()
    video_capture.release()
    cv2.destroyAllWindows()

# === MAIN PROGRAM ===
try:
    print("Waiting for object detection...")
    while True:
        if GPIO.input(IR_SENSOR_PIN) == 0:  # Object detected (LOW signal)
            print("Object detected! Starting video recording...")
            record_video()
            print("Waiting for next detection...")

except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
