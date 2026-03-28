# Collecting hand data for all 26 letters

import cv2
import os
import shutil

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Clear old images if retraining
if os.path.exists('Image'):
    shutil.rmtree('Image')
    print('Cleared old images')

# Create directories for each letter
for letter in letters:
    os.makedirs(f'Image/{letter}', exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found.")
    exit()

# Track which letter we're currently collecting
current_idx = 0
TARGET = 100 # images per letter

print(f'Starting with letter: {letters[current_idx]}')
print('Press the current letter key to save an image')
print('Press SPACE to move to the next letter')
print('Press 9 to quit')

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Failed to grab frame")
        break

    current_letter = letters[current_idx]
    count = len(os.listdir(f'Image/{current_letter}'))

    cv2.rectangle(frame, (50, 100), (350, 400), (255, 255, 255), 2)

    # Current letter, count, and instructions
    cv2.rectangle(frame, (0, 0), (640, 50), (245, 117, 16), -1)
    cv2.putText(frame,
                f'Letter: {current_letter}  |  {count}/{TARGET}  |  Press "{current_letter.lower()}" to capture',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)

    # Progress bar
    progress = int((count / TARGET) * 300)
    cv2.rectangle(frame, (50, 410), (50 + progress, 430), (0, 255, 0), -1)
    cv2.rectangle(frame, (50, 410), (350, 430), (255, 255, 255), 1)

    # Show if we hit target
    if count >= TARGET:
        cv2.putText(frame, 'DONE! Press SPACE for next letter',
                    (50, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2, cv2.LINE_AA)

    cv2.imshow('Collect Data', frame)
    cv2.imshow('ROI', frame[100:400, 50:350])

    interrupt = cv2.waitKey(10)

    # Press the specific letter key to take the picture
    if interrupt & 0xFF == ord(current_letter.lower()):
        crop = frame[100:400, 50:350]
        cv2.imwrite(f'Image/{current_letter}/{count}.png', crop)
        print(f'Saved {current_letter}/{count}.png')

    # Space = next letter
    if interrupt & 0xFF == ord(' '):
        if current_idx < len(letters) - 1:
            current_idx += 1
            print(f'Moving to letter: {letters[current_idx]}')
        else:
            print('All letters done!')
            break

    if interrupt & 0xFF == ord('9'):
        break

cap.release()
cv2.destroyAllWindows()
print('Done collecting!')
