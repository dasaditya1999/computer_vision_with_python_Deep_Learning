import cv2

# Ask user which object tracker to use
def ask_user_for_tracker():
    print('drop 0 for Boosting Tracker')
    print('drop 1 for MIL Tracker')
    print('drop 2 from KCF Tracker')
    print('drop 3 for TLD Tracker')
    print('drop 4 for Median Flow Tracker')
    user_input = input('Enter the desired number please')

    if user_input == '0':
        tracker = cv2.legacy.TrackerBoosting_create()

    if user_input == '1':
        tracker = cv2.TrackerMIL_create()

    if user_input == '2':
        tracker = cv2.legacy.TrackerKCF_create()

    if user_input == '3':
        tracker = cv2.TrackerTLD_create()

    if user_input == '4':
        tracker = cv2.TrackerMedianFlow_create()
    
    return tracker




# print(ask_user_for_tracker())
tracker = ask_user_for_tracker()
tracker_name = str(tracker).split()[1].split('.')[-1]


cap = cv2.VideoCapture(0)

# Read first frame.
ret, frame = cap.read()


# Special function allows us to draw on the very first frame our desired ROI
roi = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ret = tracker.init(frame, roi)

while True:
    # Read a new frame
    ret, frame = cap.read()
    
    
    # Update tracker
    success, roi = tracker.update(frame)
    
    # roi variable is a tuple of 4 floats
    # We need each value and we need them as integers
    (x,y,w,h) = tuple(map(int,roi))
    
    # Draw Rectangle as Tracker moves
    if success:
        # Tracking success
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
    else :
        # Tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)

    # Display tracker type on frame
    cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3);

    # Display result
    cv2.imshow(tracker_name, frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : 
        break
        
cap.release()
cv2.destroyAllWindows()


