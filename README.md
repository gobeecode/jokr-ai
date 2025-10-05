# Joker AI
Joke telling AI assistant developed using python and large language models (LLMS) in artificial intelligence.

## Installation
- Download and install Ollama application.
- Pull a model from ollama using the below command.
  ```shell
    ollama run llama3.2
    ```
- Clone the repo and change directory to the root of the repo.
- Upgrade pip
  ```shell
    python -m pip install --upgrade pip
  ```
- Run the below command to install all the dependencies.
  ```shell
    pip install -r requirements.txt
  ```

## Configuration
- By default, the script uses llama3.2 model in ollama platform. 
- If you want to use other opensource models, Follow the below steps.
  - Download them using `ollama run MODEL_NAME`.
  - To view the list of all available models, Click [here](https://ollama.com/search)
  - Enter the model name to use, when the script prompts for the model name.

## Usage
- Execute the below command in the commandline.
  ```shell
    python ./main.py
  ```
- Enter the topic to tell the joke on. Default: any.
- By default, the assistant uses ollama model and llama3.2 for generating a joke.
- Wait for a few seconds for the joke to be generated.
