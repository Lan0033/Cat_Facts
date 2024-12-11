# Cat Chatbot with Fun Facts

This project is a chatbot that combines the power of OpenAI's GPT-4 and the Cat Facts API to provide fun and informative answers to user queries about cats. The chatbot enriches its responses by integrating random, interesting cat facts.

## Features

- **Cat Facts**: The bot fetches random fun and interesting facts about cats using the Cat Facts API.
- **Chatbot**: Powered by OpenAI's GPT-4, the chatbot answers user queries about cats with relevant information, enhanced by cat facts.
- **Cat-themed Responses**: The chatbot responds with a personality that aligns with a fun and informative cat theme.

## Prerequisites

Before running this project, ensure you have the following:

- **Python 3.x** installed.
- **OpenAI API** access (specifically Azure OpenAI).
- **Azure Key and Endpoint** (you will need to configure these in your environment variables).

## Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/yourusername/cat-chatbot.git
   cd cat-chatbot
   ```

2. **Install required Python packages**:

   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file or set the following environment variables:

   - `AZURE_KEY`: Your Azure OpenAI API key.
   - `AZURE_ENDPOINT`: The endpoint for Azure OpenAI.

   Example of `.env` file:

   ```
   bashCopy codeAZURE_KEY=your-azure-api-key
   AZURE_ENDPOINT=your-azure-endpoint
   ```

4. **Run the script**:

   After setting up the environment, you can run the Python script to interact with the chatbot.

   ```
   python chatbot.py
   ```



## Example Usage

1. The bot answers questions related to cats, integrating interesting facts into its responses.

2. Example interaction:

   ![](https://cdn.discordapp.com/attachments/1309100112504688650/1316357436101099520/Screenshot_2024-12-11_104447.png?ex=675ac0e5&is=67596f65&hm=fa5997241d4ca0fffef3e395bb4d8c10576335f955746d09aa9dffcab731066e&)

   