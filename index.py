# Open AI Documentation: https://platform.openai.com/docs/quickstart?context=python

# Import the key modules and variables
import openai
import secrets

# Set the openai api key to the api key variable
openai.api_key = secrets.API_KEY


# Select the model that we will use for the completion 
model = secrets.MODEL

# Main function to be run
def main():
    # Create a list called memory to store your messages

    # Create a while loop that completes the following
    # 1. While the user input is not equal to stop, the loop will continue
    # 2. Add the user message to your memory
    # 3. create a variable to call your open ai chat completion model
    # 4. Add the message from the ai to the memory
    # Hint: select the current message from the response with response.choices[0].message


# Runs the main function
if __name__ == "__main__":
    main()