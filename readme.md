# QuestionPicker

QuestionPicker is a Python class that helps manage and track progress on coding questions, particularly useful for interview preparation or systematic learning of data structures and algorithms.

## Overview

The QuestionPicker class provides functionality to:
- Get random unsolved questions
- Mark questions as done or favorite
- View favorite questions
- Show progress by topic
- Reset sheet progress with backup

## Setup

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the `question_picker.py` file.
3. Prepare a `sheet.json` file with your questions data (see JSON Structure below).

## Requirements

- Python 3.x
- JSON file (`sheet.json`) with question data

## Installation

No additional libraries are required. The script uses only Python standard libraries.

## Usage

```python
from question_picker import QuestionPicker

# Initialize QuestionPicker with your JSON file
picker = QuestionPicker('sheet.json')

# Use the various methods as needed
random_question = picker.get_random_unsolved_question()
picker.mark_question_done()
picker.mark_question_favorite()
picker.show_favorite_questions()
picker.show_topic_progress()
picker.reset_sheet()
```

## check out @
https://automatic-goldfish-jvjqg9r6g74hwv-8000.app.github.dev/
user: freeuser
password: freeuser

## JSON Structure

Your `sheet.json` file should have the following structure:

```json
{
    "sheetData": [
        {
            "head_step_no": "Arrays",
            "topics": [
                {
                    "id": "stmtrixzrs",
                    "title": "Set Matrix Zeros",
                    "lc_link": "https://leetcode.com/problems/set-matrix-zeroes/",
                    "status": "Not Suggested"
                },
                // More questions...
            ]
        },
        // More topics...
    ]
}
```

Note: The `status` field is optional and will be added by the script if not present.

## Functionality

1. **Get Random Unsolved Question**: Selects a random question that hasn't been suggested or is marked as favorite.

2. **Mark Question as Done**: Allows you to mark a suggested question as completed.

3. **Mark Question as Favorite**: Marks a suggested question as a favorite for later review.

4. **Show Favorite Questions**: Displays all questions marked as favorites, grouped by topic.

5. **Show Topic Progress**: Provides a visual representation of your progress for each topic.

6. **Reset Sheet Progress**: Resets all questions to "Not Suggested" status, creating a backup of the current progress.

## Color Coding

The script uses ANSI color codes to enhance the command-line interface:
- Blue: Headers and prompts
- Cyan: Menu options and data labels
- Green: Success messages and completed items
- Yellow: Warnings and important choices
- Red: Error messages

## Note

This script is designed for local use and doesn't include any external dependencies for simplicity. Ensure your terminal supports ANSI color codes for the best experience.
