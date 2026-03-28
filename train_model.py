# Training with Random Forest (NO TF/Keras version drama)
# Trains in seconds, wayyyy more accurate for 63 landmark coords

from function import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import numpy as np
import os

label_map     = {label: num for num, label in enumerate(actions)}
num_to_label  = {num: label for label, num in label_map.items()}

sequences, labels = [], []

for action in actions:
    action_dir = os.path.join(DATA_PATH, action)
    if not os.path.exists(action_dir):
        print(f'Missing data for {action} — skipping')
        continue

    for npy_file in os.listdir(action_dir):
        if not npy_file.endswith('.npy'):
            continue

        npy_path = os.path.join(action_dir, npy_file)
        keypoints = np.load(npy_path, allow_pickle=True)

        # Skip zero arrays (mediapipe found no hand in that image)
        if np.all(keypoints == 0):
            continue

        sequences.append(keypoints)
        labels.append(label_map[action])

print(f'\nTotal usable samples: {len(sequences)}')

X = np.array(sequences)
Y = np.array(labels)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.1, stratify=Y, random_state=42
)

print(f'Training on {len(X_train)} samples, testing on {len(X_test)}')

# Random Forest = robust, no version issues, trains EXTREMELY fast
model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, Y_train)

preds = model.predict(X_test)
acc   = accuracy_score(Y_test, preds)
print(f'\nAccuracy: {acc * 100:.1f}%')
print('\nPer-letter breakdown:')
print(classification_report(Y_test, preds, target_names=actions))

# Save as pickle — no keras, no tf, no drama
with open('classifier.p', 'wb') as f:
    pickle.dump({'model': model, 'labels': num_to_label}, f)

print('Saved classifier.p')
