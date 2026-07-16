# Random Password Generator

A secure, interactive command-line Python application that generates strong, randomized passwords based on user-defined criteria. This project is a task for the Oasis Infobyte Python Programming internship.

## Features
* **Custom Length:** Allows users to specify the exact length of their password (enforces a minimum of 8 characters for security).
* **Character Diversity:** Prompts users to include uppercase letters, lowercase letters, numbers, and symbols. 
* **Security Rules:** Enforces the selection of at least two different character types and guarantees that at least one character from every selected type is present in the final password.
* **Continuous Generation:** Users can generate multiple passwords in a single session without restarting the script.
* **Input Validation:** Gracefully handles invalid inputs (non-numeric lengths, invalid yes/no responses) to prevent application crashes.

## Tech Stack
* **Language:** Python 3.x
* **Modules:** `random`, `string` (Built-in Python modules, no external dependencies required).

## Getting Started

### Prerequisites
Ensure you have Python 3 installed on your machine. 

### Installation & Execution
1. Clone the repository or download the project files.
2. Open your terminal or command prompt and run the code.
