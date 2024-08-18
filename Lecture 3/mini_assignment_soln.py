import os

# Step 1: Determine the CSV file path
# Get the directory of the current script
script_directory: str = os.path.split(os.path.abspath(__file__))[0]

# Construct the complete file path using the script directory and file name
file_name: str = "student_scores.csv"
file_path: str = os.path.join(script_directory, file_name)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File '{file_name}' not found.")
    exit(1)

# Step 2: Read and process the CSV file
with open(file_path, "r") as file:
    lines: list[str] = file.readlines()
    lines.pop(
        0
    )  # Remove header. Alternatively, you can skip the first line while processing by using continue in the loop.

    math_total: int = 0
    science_total: int = 0
    history_total: int = 0
    total_students: int = len(lines)

    # Process each line and calculate totals
    for line in lines:
        name, math_score, science_score, history_score = line.strip().split(",")
        math_total += int(math_score)
        science_total += int(science_score)
        history_total += int(history_score)

    # Step 3: Calculate average scores
    math_average: float = math_total / total_students
    science_average: float = science_total / total_students
    history_average: float = history_total / total_students

    # Step 4: Display the results
    print("Subject Averages:")
    print(f"Math: {math_average:.2f}")
    print(f"Science: {science_average:.2f}")
    print(f"History: {history_average:.2f}")
