import cv2 as cv

def camera_normal(capture_device: int, video_width: int, video_height: int) -> None:
    """
    initializes the camera, sets its desired frame size, and displays the frames in a window

    :param capture_device: integer representing the capture device index
    :param video_width: desired video frame width
    :param video_height: desired video frame height
    :return: None
    """
    cam = cv.VideoCapture(capture_device)

    # override default values
    cam.set(cv.CAP_PROP_FRAME_WIDTH, video_width)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, video_height)

    if not cam.isOpened():
        print('Error: camera cannot be initialized.')
        return

    print('Initializing camera...')
    print('Frame size:', cam.get(cv.CAP_PROP_FRAME_WIDTH), 'x', cam.get(cv.CAP_PROP_FRAME_HEIGHT))
    cv.namedWindow('Video', cv.WINDOW_NORMAL)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: could not read frame.")
            break

        cv.imshow('Video', frame)
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            break

    cam.release()
    cv.destroyAllWindows()

def camera_box(capture_device: int, video_width: int, video_height: int) -> None:
    """
    performs face detection on the frames, draws a rectangle around the detected faces

    :param capture_device: integer representing the capture device index
    :param video_width: desired video frame width
    :param video_height: desired video frame height
    :return: None
    """

    # load Haar cascade classifier for face detection
    faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # create VideoCapture object to access the camera
    cam = cv.VideoCapture(capture_device)

    # override default values
    cam.set(cv.CAP_PROP_FRAME_WIDTH, video_width)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, video_height)

    # check if the camera is on, if not print error message and return
    if not cam.isOpened():
        print('Error: camera cannot be initialized.')
        return
    print('Initializing camera...')
    print('Frame size:', cam.get(cv.CAP_PROP_FRAME_WIDTH), 'x', cam.get(cv.CAP_PROP_FRAME_HEIGHT))
    
    # create a window to display the video
    cv.namedWindow('Video', cv.WINDOW_NORMAL)

    # loop to process frames from the camera 
    while True:
        # read a frame 
        ret, frame = cam.read()

        # if a frame cannot be read, error and break
        if not ret:
            print("Error: could not read frame.")
            break
        
        # convert the frame to grayscale to simplify the image processing
        grayframe = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

        # detect the faces in the frame
        detected_faces = faceCascade.detectMultiScale(grayframe, 1.3, 5)

        # draw a rectangle around the detected faces
        for (x, y, w, h) in detected_faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # display the frame
        cv.imshow('Video', frame)

        # check if 'q' key is pressed
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            break
    
    # release the camera and destroy the window
    cam.release()
    cv.destroyAllWindows()

def camera_zoom(capture_device: int, video_width: int, video_height: int) -> None:
    """
    performs face detection on the frames, zooms in on the largest detected face

    :param capture_device: integer representing the capture device index
    :param video_width: desired video frame width
    :param video_height: desired video frame height
    :return: None
    """
    faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv.VideoCapture(capture_device)

    # override default values
    cam.set(cv.CAP_PROP_FRAME_WIDTH, video_width)
    cam.set(cv.CAP_PROP_FRAME_HEIGHT, video_height)

    if not cam.isOpened():
        print('Error: camera cannot be initialized.')
        return

    print('Initializing camera...')
    print('Frame size:', cam.get(cv.CAP_PROP_FRAME_WIDTH), 'x', cam.get(cv.CAP_PROP_FRAME_HEIGHT))
    cv.namedWindow('Video', cv.WINDOW_NORMAL)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: could not read frame.")
            break
        
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)
        roi_frame = frame
        
        if len(face_rects) > 0:
            for (x, y, w, h) in face_rects:
                roi_frame = frame[y:y + h, x:x + w]
            if roi_frame.size != frame.size:
                roi_frame = cv.resize(roi_frame, (500, 500))

        cv.imshow('Video', roi_frame)
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            break

    cam.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    # camera_normal(2, 1920, 1080)
    # camera_box(2, 1920, 1080) 
    camera_zoom(2, 1920, 1080)
