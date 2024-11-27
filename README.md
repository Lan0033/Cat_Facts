# Cat Chatbot Powered by OpenAI & Azure

This is a fun and interactive chatbot that answers questions about cats from a cat's perspective, integrating OpenAI's GPT-4 model via Azure, and providing random cat facts fetched from an external API.

## Features

- Chat with a cat who loves to share fun and interesting cat facts.
- Every response is influenced by a random cat fact fetched from the Cat Fact API.
- Powered by OpenAI's GPT-4 model through Azure OpenAI API.
- Continuous interaction loop that stops only when the user types 'exit'.

## Requirements

To run this project, you'll need:

- Python 3.x
- An Azure OpenAI subscription (to access GPT-4)
- An internet connection for fetching cat facts

## Installation

1. Clone this repository to your local machine:

   ```
   bashCopy codegit clone https://github.com/yourusername/cat-chatbot.git
   cd cat-chatbot
   ```

2. Create a virtual environment (optional but recommended):

   ```
   bashCopy codepython -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:

   ```
   pip install -r requirements.txt
   ```
   
   The `requirements.txt` should include:
   
   ```
   plaintextCopy codeopenai
   requests
   ```
   
4. Set up your environment variables for Azure API access:

   - `AZURE_KEY`: Your Azure API key for OpenAI GPT.
   - `AZURE_ENDPOINT`: Your Azure OpenAI endpoint URL.

   On Linux/macOS:

   ```
   bashCopy codeexport AZURE_KEY="your_azure_api_key"
   export AZURE_ENDPOINT="your_azure_endpoint"
   ```

   On Windows (in Command Prompt):

   ```
   bashCopy codeset AZURE_KEY=your_azure_api_key
   set AZURE_ENDPOINT=your_azure_endpoint
   ```

## Usage

1. Run the script to start chatting with the cat:

   ```
   python cat_chatbot.py
   ```
   
2. Ask the chatbot anything about cats, or type 'exit' to quit the conversation.

3. The bot will respond with a cat's perspective and include a fun cat fact in its answers.

   Example:

   ```
   vbnetCopy codeAsk me anything about cats (or type 'exit' to quit): What's your favorite food?
   (=①ω①=): I love tuna! Here's an interesting cat fact: Cats can make over 100 different sounds!
   ```

![](https://cdn.discordapp.com/attachments/1309100112504688650/1311281849804263445/Screenshot_2024-11-27_010405.png?ex=674849e3&is=6746f863&hm=7d779acbf7e5b1d440005f2fde356afbc01adf9078dc4210a61dd128ba975675&)

## Code Overview

- **`get_cat_fact()`**: Fetches a random cat fact from the Cat Fact API.
- **`generate_openai_response(user_question, cat_fact)`**: Generates a response from OpenAI's GPT-4 model, incorporating the random cat fact.
- **Main Loop**: Continuously prompts the user for input and responds until 'exit' is typed.