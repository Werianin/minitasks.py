import numpy as np
import matplotlib.pyplot as plt
import time


def initialize_field(size):
    return np.random.randint(2, size=(size, size))


def game_of_life_python(field):
    size = len(field)
    new_field = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            live_neighbors = sum(
                field[i + di][j + dj]
                for di in (-1, 0, 1) for dj in (-1, 0, 1)
                if (di != 0 or dj != 0) and 0 <= i + di < size and 0 <= j + dj < size
            )
            new_field[i][j] = 1 if (field[i][j] and live_neighbors in (2, 3)) or (not field[i][j] and live_neighbors == 3) else 0
    return new_field


def game_of_life_numpy(field):
    padded_field = np.pad(field, pad_width=1, mode='constant', constant_values=0)
    neighbors = sum(np.roll(np.roll(padded_field, di, axis=0), dj, axis=1)[1:-1, 1:-1]
                    for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0))
    return ((neighbors == 3) | ((field == 1) & (neighbors == 2))).astype(int)


size = 128
iterations = 32
field = initialize_field(size)


field_python = field.tolist()
start_time_python = time.time()
for _ in range(iterations):
    field_python = game_of_life_python(field_python)
end_time_python = time.time()


field_numpy = field.copy()
start_time_numpy = time.time()
for _ in range(iterations):
    field_numpy = game_of_life_numpy(field_numpy)
end_time_numpy = time.time()


survivors_python = sum(sum(row) for row in field_python)
survivors_numpy = np.sum(field_numpy)


print("Python:", end_time_python - start_time_python, "seconds")
print("NumPy:", end_time_numpy - start_time_numpy, "seconds")
print("Survivors (Python):", survivors_python)
print("Survivors (NumPy):", survivors_numpy)


def visualize(field, title):
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.imshow(field, cmap='binary')
    plt.axis('off')
    plt.show()


visualize(field_numpy, "Game of Life")
