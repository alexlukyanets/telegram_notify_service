
---

# Telegram Message Sender

## Introduction

This project is a simple Flask application designed to send messages to a Telegram channel or chat through a REST API. It leverages Docker for easy deployment and isolation. The application is perfect for automating notifications or integrating Telegram messaging into other systems.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
    - [Docker](#docker)
    - [Manual Installation](#manual-installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Features

- Send messages to Telegram channels or chats through a REST API.
- Easy deployment with Docker.
- Minimal setup required.

## Installation

### Docker

1. Clone this repository.
2. Navigate to the cloned directory.
3. Build the Docker image:

    ```sh
    docker build -t telegram-sender .
    ```

4. Run the Docker container:

    ```sh
    docker run -d -p 5000:5000 telegram-sender
    ```

### Manual Installation

1. Ensure Python 3.12 or later is installed.
2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```sh
    flask run --host=0.0.0.0 --port=5000
    ```

## Usage

To send a message, make a POST request to `/send` with a JSON payload containing `TELEGRAM_TOKEN`, `TELEGRAM_CHANNEL`, and the `message`. For example:

```json
{
  "TELEGRAM_TOKEN": "your_telegram_bot_token",
  "TELEGRAM_CHANNEL": "your_channel_or_chat_id",
  "message": "Hello, Telegram!"
}
```

## Dependencies

- Flask
- Requests

These are specified in the `requirements.txt` file.

## Configuration

No additional configuration is required outside of the environment variables and parameters used in the POST request.

## Troubleshooting

Ensure all data in the POST request is correct, especially the Telegram token and chat ID. For detailed error information, check the application logs.

## Contributors

[List of contributors]

## License

[Specify the license or indicate "Unlicensed" if the project is not under any existing licenses.]

---