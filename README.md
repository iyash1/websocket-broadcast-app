# WebSocket Broadcast App 🔌

## Overview
A real-time WebSocket broadcasting application for seamless multi-client communication.

## Prerequisites 📋
- Python 3.8+
- Miniconda installed ([Download](https://docs.conda.io/projects/miniconda/latest/))
- Git

## Setup ⚙️

### 1. Clone & Navigate
```bash
git clone https://github.com/iyash1/websocket-broadcast-app.git
cd websocket-broadcast-app
```

### 2. Create Conda Environment
```bash
conda create -n websocket-app python=3.10
conda activate websocket-app
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Project Structure 📁
```
websocket-broadcast-app/
├── server.py
├── client.py
├── requirements.txt
└── README.md
```

## Running the App ▶️

### Start Server
```bash
python server.py
```
Server runs on `ws://localhost:8765`

### Connect Client
Open the `index.html` file in separate browsers. Use at least 2 browsers to observe the broadcasting.

## Input/Output 🔄

**Input:** Text messages from connected clients  
**Output:** Broadcast messages to all connected clients in real-time, except the sender.

## Features ✨
- Real-time message broadcasting
- Multiple concurrent connections
- Lightweight and efficient
