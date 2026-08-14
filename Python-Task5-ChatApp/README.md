# Real-Time Chat Application

A command-line real-time messaging application built in Python. It supports bidirectional communication between multiple clients over a local network. This project is a task for the Oasis Infobyte Python Programming internship.

## Features
* **Real-Time Messaging:** Instant, bidirectional message exchange using Python sockets.
* **Timestamping:** Every message is automatically prefixed with a timestamp (e.g., `[14:35] Alice: Hello`).
* **Multi-User Support:** Utilizes threading to handle multiple client connections simultaneously.
* **Graceful Disconnections:** Safely handles users exiting the application and automatically notifies the remaining clients in the chat room that someone has left.
* **Local Networking:** Runs directly on `localhost` for easy testing on a single machine.

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `socket`, `threading`, `datetime` (All built-in Python modules, no external dependencies required).

## Getting Started

### Prerequisites
Ensure you have Python 3 installed on your machine.

### Installation & Execution
This application requires running a server script to act as the host, and client scripts to act as the users.

1. Clone the repository or download the project files.
2. Open your terminal or command prompt.
