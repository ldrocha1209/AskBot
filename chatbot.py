import requests
import re
from datetime import datetime

class AskBot:
    
    # initialize AskBot
    def __init__(self):
        self.log_file = "chat_log.txt"
        
    # run AskBot
    def run(self):

        # start the log session using the start_log_sesh method
        self.start_log_sesh()

        # initial starting message
        print("AskBot: Hi! Type your question or 'exit', 'bye', or 'quit' to exit.")

        # while loop that allows user to continue speaking to AskBot until they exit
        while True:
            user_input = input("You: ")

            # response if user input empty
            if not user_input.strip():
                print("AskBot: You did not type anything. Please enter a question or command.")
                continue

            # variable created for intent, used to determine type of response
            intent = self.detect_intent(user_input)

            # exits the while loop, ends the session
            if intent == "exit":
                bot_response = "Goodbye! Have a great day."
                print("AskBot:", bot_response)
                self.log_entry(user_input, bot_response)
                break

            # greeting if the user says one of the defined greetings in detect_intent method
            elif intent == "greeting":
                bot_response = "Hello! I am AskBot. You can ask me about people, concepts, or ask for definitions. Type 'exit', 'bye', or 'quit' to exit."
                print("AskBot:", bot_response)
                self.log_entry(user_input, bot_response)

            # response to user if they ask to define
            elif intent == "define":
                topic = re.match(r"^define\s+(.+)$", user_input, re.IGNORECASE).group(1)
                self.wiki_response(user_input, topic)
                
            # response to user if they ask who is...
            elif intent == "who_is":
                topic = re.match(r"^who is\s+(.+)$", user_input, re.IGNORECASE).group(1)
                self.wiki_response(user_input, topic)

            # response to user if they say tell me about...
            elif intent == "tell_me_about":
                topic = re.match(r"^tell me about\s+(.+)$", user_input, re.IGNORECASE).group(1)
                self.wiki_response(user_input, topic)

            # response to user if they ask who is...
            elif intent == "what_is":
                topic = re.match(r"^what is\s+(.+)$", user_input, re.IGNORECASE).group(1)                
                self.wiki_response(user_input, topic)

            # reponse to user if they thank AskBot
            elif intent == "thank_you":
                bot_response = "You're welcome! Any other questions?"
                print("AskBot:", bot_response)
                self.log_entry(user_input, bot_response)

            # fallback response if the program does not understand the user input
            else:
                bot_response = "I'm not sure how to help with that. Try asking me to define something or ask 'who is' followed by a name."
                print("AskBot:", bot_response)
                self.log_entry(user_input, bot_response)

    # method for detereming intent, uses regex library
    def detect_intent(self, user_input):
        user_input = user_input.strip()

        # check for exit commands
        if user_input.lower() in ['exit', 'bye', 'quit']:
            return "exit"

        # check for greetings
        if re.match(r"^(hi|hello|hey|yo|howdy|greetings|good morning|good afternoon|good evening|what'?s up)(\s+there)?[!,.]?$", user_input, re.IGNORECASE):
            return "greeting"

        # check for thank you
        if re.match(r"^(thanks|thank you)[!,.]?$", user_input, re.IGNORECASE):
            return "thank_you"

        # check for define requests
        if re.match(r"^define\s+(.+)$", user_input, re.IGNORECASE):
            return "define"
        
        # check for who is requests
        if re.match(r"^who is\s+(.+)$", user_input, re.IGNORECASE):
            return "who_is"

        # check for what is requests
        if re.match(r"^what is\s+(.+)$", user_input, re.IGNORECASE):
            return "what_is"

        # check for tell me about requests
        if re.match(r"^tell me about\s+(.+)$", user_input, re.IGNORECASE):
            return "tell_me_about"

        # if user input is not understood, return unknown intent
        return "unknown"

    # method used to retrieve wikipedia information, used in run method
    def get_wikipedia_summary(self, topic):
        url = "https://en.wikipedia.org/w/api.php"

        headers = {
            "User-Agent": "AskBot/1.0 (Python chatbot portfolio project)"
        }

        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": topic,
            "gsrnamespace": 0,
            "gsrlimit": 5,
            "prop": "extracts|pageprops",
            "explaintext": 1,
            "exintro": 1,
            "exsentences": 2,
            "ppprop": "disambiguation"
        }

        try:
            for attempt in range(3):
                try:
                    response = requests.get(
                        url,
                        headers=headers,
                        params=params,
                        timeout=10
                    )

                    response.raise_for_status()

                    data = response.json()
                    break

                except requests.exceptions.RequestException:
                    if attempt == 2:
                        return "I was unable to connect to Wikipedia right now."

            pages = data.get("query", {}).get("pages", {})

            if not pages:
                return "I could not find information on that topic."

            topic_lower = topic.strip().lower()

            page = None

            for result in pages.values():
                if result["title"].strip().lower() == topic_lower:
                    page = result
                    break

            if page is None:
                page = next(iter(pages.values()))

            if "pageprops" in page and "disambiguation" in page["pageprops"]:
                choices = []

                for result in pages.values():
                    if result["title"].strip().lower() != topic_lower:
                        choices.append(result["title"])

                if choices:
                    return "That topic has multiple possible meanings. Some choices are: " + ", ".join(choices[:5])

            if "extract" not in page or not page["extract"]:
                return "I could not find information on that topic."

            return page["extract"]

        except (ValueError, KeyError, StopIteration):
            return "Wikipedia returned an unexpected response."

        except Exception:
            return "I was unable to retrieve information right now."

    # method used to log every conversation between AskBot and user
    def log_entry(self, user_input, bot_response):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # logs every prompt and answer, with a timestamp using datetime
        with open(self.log_file, "a") as file:
            file.write(f"[{timestamp}] You: {user_input}\n")
            file.write(f"[{timestamp}] AskBot: {bot_response}\n\n")

    # method used to mark the start of a new session on the log
    def start_log_sesh(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # new session is labled and dated on the log
        with open(self.log_file, "a") as file:
            file.write("\n")
            file.write("=" * 40 + "\n")
            file.write(f"New AskBot Session: {timestamp}\n")
            file.write("=" * 40 + "\n\n")

    # method used to display wikipedia information retrieved from the get_wikipedia_summary method
    def wiki_response(self, user_input, topic):
        bot_response = self.get_wikipedia_summary(topic)

        print("AskBot:", bot_response)
        self.log_entry(user_input, bot_response)
            
def main():

    # create AskBot object
    bot = AskBot()

    # start and run AskBot
    bot.run()

if __name__ == "__main__":
    main()
