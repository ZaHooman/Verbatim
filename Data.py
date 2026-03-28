# Extracts landmarks from MY OWN images only
# Kaggle was actually trash

from function import *
import cv2

YOUR_PATH = 'Image'

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.3
) as hands:
    for action in actions:
        os.makedirs(os.path.join(DATA_PATH, action), exist_ok=True)

        your_dir = os.path.join(YOUR_PATH, action)

        if not os.path.exists(your_dir):
            print(f'Missing folder: {your_dir} — run collectdata.py first')
            continue

        my_imgs = [f for f in os.listdir(your_dir)
                   if f.endswith('.jpg') or f.endswith('.png')]

        print(f'{action}: {len(my_imgs)} images')

        for sequence, img_name in enumerate(my_imgs):
            frame = cv2.imread(os.path.join(your_dir, img_name))

            if frame is None:
                print(f'Warning: could not read {img_name}')
                np.save(os.path.join(DATA_PATH, action, f'{sequence}.npy'), np.zeros(21 * 3))
                continue

            image, results = mediapipe_detection(frame, hands)

            if results.multi_hand_landmarks:
                print(f'Hand detected: {action} seq {sequence}')
            else:
                print(f'No hand: {action} seq {sequence}')

            keypoints = extract_keypoints(results)
            np.save(os.path.join(DATA_PATH, action, str(sequence)), keypoints)

            cv2.putText(image, f'{action} - {sequence}/{len(my_imgs)}',
                        (15, 12), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('OpenCV Feed', image)

            if cv2.waitKey(1) & 0xFF == ord('9'):
                break

cv2.destroyAllWindows()
