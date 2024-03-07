import os
import random


def generate_document(rows, columns):
    document = f"{rows} {columns}\n"
    for i in range(1, rows + 1):
        row_data = [str(i)]
        remaining_values = list(range(1, columns + 1))
        random.shuffle(remaining_values)
        row_data.extend(str(remaining_values[j % columns])
                        for j in range(columns))
        document += " ".join(row_data) + "\n"
    return document


# Specify the desired document sizes
document_sizes = [
    (10, 5),
    (10, 10),
    (10, 50),
    (10, 100),
    (10, 500),
    (100, 5),
    (100, 10),
    (100, 50),
    (100, 100),
    (100, 500),
    (500, 5),
    (500, 10),
    (500, 50),
    (500, 100),
    (500, 500),
    (1000, 5),
    (1000, 10),
    (1000, 50),
    (1000, 100),
    (1000, 500),
    (5000, 5),
    (5000, 10),
    (5000, 50),
    (5000, 100),
    (5000, 500),
    (7500, 5),
    (7500, 10),
    (7500, 50),
    (7500, 100),
    (7500, 500),
    (10000, 5),
    (10000, 10),
    (10000, 50),
    (10000, 100),
    (10000, 500),
]


def save_document(directory, name, content):
    with open(os.path.join(directory, name), "w") as file:
        file.write(content)


def generate_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, (rows, columns) in enumerate(document_sizes, start=1):
        content = generate_document(rows, columns)
        filename = f"time_{rows}_{columns}.txt"
        save_document(directory, filename, content)


# Specify the directory to save the files
directory = "D:\КПІ\ТА. Лабораторні\TA.Lab2\src\\time_inputs"

# Generate files
generate_files(directory)

print("Files generated successfully.")
