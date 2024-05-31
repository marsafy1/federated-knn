# Federated k-NN Learning Application
![Python](https://img.shields.io/badge/python-a4c330.svg?style=for-the-badge&logo=python&logoColor=white)
![.ENV](https://img.shields.io/badge/dotenv-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![React](https://img.shields.io/badge/react-61DAFB.svg?style=for-the-badge&logo=react&logoColor=white)
![MUI5](https://img.shields.io/badge/mui-007FFF.svg?style=for-the-badge&logo=mui&logoColor=white)




<br/>
This repository contains a federated k-Nearest Neighbors (k-NN) learning application built using Python. The application is designed to classify spam messages using a federated learning approach. The setup includes three clients and a main server that aggregates responses using various techniques.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

Federated learning is a machine learning technique that trains an algorithm across multiple decentralized devices or servers holding local data samples, without exchanging them. In this project, we use federated k-NN to classify spam messages, ensuring data privacy and security by keeping data localized on each client.

## Features

- Federated k-NN classification for spam messages
- Three clients participating in the federated learning process
- Main server for aggregating client responses
- Various aggregation techniques for federated learning
- Secure and private data handling

## Installation

To install and run this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/federated-knn-learning.git
   cd federated-knn-learning
   ```

2. **Set up a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To install and run this project, follow these steps:

1. **Option #1:** Using the `.sh` script (starts both the backend and the frontend servers)
   ```sh
   ./start.sh
   ```

2. **Option #2:** Start the servers manually
   - Start the venv:
     ```sh
     source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
     ```
     
   - Start the backend server:
     ```sh
     cd main && python3 flask_server.py
     ```

   - Start the frontend server:
     ```sh
     cd main && python3 flask_server.py
     ```

## Project Structure

```
federated-knn-learning/
├── code
├── datasets
│   ├── dataset_processing.ipynb
│   ├── new_spam.csv
│   └── spam.csv
├── knn-frontend
│   ├── src
│       ├── App.css
│       ├── App.js
│       ├── assets/
│       ├── components/
│       ├── index.css
│       └── index.js
├── main
│   ├── MyRedis.py
│   ├── client.py
│   ├── flask_server.py
│   ├── main.py
│   ├── script_dump
│   │   ├── client_1_output.txt
│   │   ├── client_2_output.txt
│   │   ├── client_3_output.txt
│   │   └── server_output.txt
│   └── server.py
├── requirements.txt
└── start.sh
```

## Technologies Used

- **Python**: The primary programming language for developing the application.
- **Federated Learning**: Technique used to ensure data privacy and security.
- **k-Nearest Neighbors (k-NN)**: The machine learning algorithm used for classification.
- **Redis**: Used for message handling between clients and servers.
- **React**: Used for the frontend.


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
