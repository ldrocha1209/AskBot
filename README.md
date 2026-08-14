# AskBot

AskBot is a Python chatbot that uses the Wikimedia API to search
Wikipedia and answer questions about people, concepts, and definitions.

The project started as a command-line assignment and was later expanded
with a Tkinter graphical user interface and improved Wikipedia search
and error handling.

## Features

-   Search Wikipedia for people, topics, and concepts
-   Supports questions such as:
    -   `Who is Michael Jackson`
    -   `What is Python`
    -   `Define computer science`
    -   `Tell me about basketball`
-   Multiple greeting options
-   Thank-you responses
-   Wikipedia search with relevance matching
-   Handles ambiguous topics and provides possible choices
-   Handles misspelled or imperfect searches
-   Automatic retries when a Wikipedia request fails
-   Request timeout and error handling
-   Command-line interface
-   Tkinter graphical user interface
-   Scrollable conversation window
-   Send messages with the Send button or Enter key
-   Clear Chat option
-   Automatic input focus
-   Goodbye message before closing

## Technologies

-   Python 3
-   Tkinter
-   Requests
-   Wikimedia API

## Project Structure

``` text
FINAL_PROJECT/
│
├── chatbot.py          # Main AskBot class and chatbot functionality
├── chatbot_gui.py      # Tkinter graphical interface
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── chat_log.txt        # Chat log file
```

## Running AskBot

### Command-Line Version

Open Terminal and navigate to the project directory:

``` bash
cd /path/to/FINAL_PROJECT
```

Then run:

``` bash
python3 chatbot.py
```

Depending on your Python installation, you may also be able to use:

``` bash
python chatbot.py
```

### Graphical Version

To launch the Tkinter interface:

``` bash
python3 chatbot_gui.py
```

A graphical window will open where you can type questions and interact
with AskBot.

## Example Questions

``` text
Who is George Washington
What is Mercury
Define Python
Tell me about computer science
```

For topics with multiple possible meanings, AskBot may provide several
possible Wikipedia results rather than guessing.

## Wikipedia API

AskBot uses the Wikimedia API directly instead of relying on the Python
`wikipedia` package.

The application includes:

-   A User-Agent identifying the application
-   Search-based topic retrieval
-   Exact-title matching when available
-   Disambiguation detection
-   Request timeouts
-   Automatic retries
-   Error handling for failed requests

This allows AskBot to handle Wikipedia searches more reliably than the
original implementation.

## GUI

The Tkinter version provides a simple graphical interface with:

-   Conversation display
-   Scrollbar
-   Text formatting for user and AskBot messages
-   Input field
-   Send button
-   Enter-to-send support
-   Clear Chat button
-   Automatic scrolling
-   Automatic input focus
-   Resizable conversation area

## Project History

AskBot was originally created as a command-line chatbot for a CSCI 308
final project. After completing the class assignment, the project was
expanded as a personal portfolio project.

The major development stages were:

1.  Initial command-line chatbot
2.  Improved Wikipedia API integration
3.  Improved search and disambiguation handling
4.  Added retry and error handling
5.  Added Tkinter graphical interface
6.  Improved GUI usability and presentation

## Future Improvements

Possible future additions include:

-   More natural language understanding
-   More flexible question formats
-   Improved Wikipedia result selection
-   Additional APIs or information sources
-   More advanced GUI styling
-   Conversation history management

## Author

Lucas Rocha

Computer Science Student
