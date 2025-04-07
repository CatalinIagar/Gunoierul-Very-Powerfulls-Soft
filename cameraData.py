import asyncio
import cv2
import time

async def log_camera_data():
    try:
        # Initialize OpenCV to capture video from the camera
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera
        if not cap.isOpened():
            print("Error: Unable to access the camera")
            return

        while True:
            # Capture frame-by-frame from the camera
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame from camera")
                break

            # Log the camera frame details (such as timestamp and frame size)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            height, width, _ = frame.shape
            print(f"Timestamp: {timestamp} | Frame size: {width}x{height}")

            # Optionally, display the frame locally
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Exit the loop if 'q' is pressed

        # Release the camera and close any OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print("An error occurred: {}".format(e))

# Run the camera data logging
asyncio.get_event_loop().run_until_complete(log_camera_data())
