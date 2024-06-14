# Youtube Script Generator

Welcome to the Youtube Script Generator repository! This repository contains a Python application that generates scripts for YouTube videos using the OpenAI API, LangChain, Wikipedia wrapper, and Streamlit.

## Table of Contents
- [About](#about)
- [Files](#files)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About
This repository includes a Python application designed to help users generate scripts for YouTube videos by leveraging the capabilities of the OpenAI API, LangChain for managing the flow of the language model, a Wikipedia wrapper for fetching information, and Streamlit for creating an interactive UI.

## Files
- **apikey.py**: Script to handle API key configuration.
- **app.py**: Main application script that generates the YouTube script using Streamlit for the user interface.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rishi-kumar0612/Yotube-script-generator.git
   cd Yotube-script-generator
   ```
2. Install the required dependencies:

  ```bash
  pip install openai streamlit langchain wikipedia-api
  ```
3. Set up your OpenAI API key in the apikey.py file.

## Usage
Run the application:

  ```bash

  streamlit run app.py
  ```
## How It Works
1. API Key Configuration: The apikey.py script manages the OpenAI API key required to access the GPT-3 model.
2. Script Generation: The app.py script prompts the user for input through a Streamlit interface, such as the topic of the YouTube video.
3. Information Retrieval: The Wikipedia wrapper fetches relevant information based on the input topic.
4. LangChain Integration: LangChain manages the flow and integration of the language model to ensure coherent script generation.
5. OpenAI API Call: The script sends the input and retrieved information to the OpenAI API, which processes it and returns a generated script.
6. Output: The generated script is displayed to the user through the Streamlit interface, ready for use in creating a YouTube video.

## Contributing
Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
Rishi Kumar - [GitHub Profile](https://github.com/rishi-kumar0612)
