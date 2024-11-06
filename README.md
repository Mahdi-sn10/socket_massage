# Socket Communication

This project consists of a simple socket application that allows two terminals to communicate with each other. One terminal acts as a server, while the other acts as a client. Messages can be sent back and forth once the connection is established.

## Requirements

- Python 3.x

### 1. Install Python

If you don't have Python installed, follow these steps:

**For Windows:**
1. Download the Python installer from the [official website](https://www.python.org/downloads/).
2. Run the installer and make sure to check the option "Add Python to PATH" during installation.
3. Verify the installation by running:
   ```bash
     python --version
   
**For macOS:**
1.You can install Python using Homebrew. First, install Homebrew if you haven't:
   ```bash
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2.Then install Python:
   ```bash
      brew install python
   ```
3.Verify the installation by running:
```bash
   python3 --version
```

**For Linux:**

Use your package manager to install Python. For example, on Ubuntu:
   ```bash
      sudo apt update
      sudo apt install python3
   ```
 Verify the installation by running:
```bash
   python3 --version
```


## Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:
```bash
git clone https://github.com/Mahdi-sn10/socket_massage.git
```
Run the Socket Server

Open a terminal window and run the server code:
```bash
python Socket.py
```
The server will start and wait for a client connection.
Run the Socket Client

Open another terminal window and run the client code:
```bash
python socket_cl.py
```
Once the client is connected to the server, you can start sending messages. Type your message in the client terminal and hit Enter to send it to the server.
