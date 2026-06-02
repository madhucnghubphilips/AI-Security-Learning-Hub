Philips Healthcare AI Security Demo - RAG Edition
===================================================

QUICK START

1. Double-click START.bat.
2. Wait for setup to finish.
3. Open your browser and go to:
       http://localhost:8000/
4. Keep the START.bat terminal window open while using the demo.

WHAT START.bat DOES

- Creates a local Python virtual environment in .venv.
- Installs Python dependencies into .venv only.
- Checks that Ollama is installed and running.
- Creates the dolphin-ctf Ollama model from Modelfile-ctf if needed.
- Pulls the nomic-embed-text Ollama embedding model if needed.
- Starts the demo server at http://localhost:8000/.

PREREQUISITES

- Python 3.10 or newer must be installed.
- Ollama must be installed.

If Ollama is missing and winget is available, START.bat can try to install Ollama for you.
If Python is missing, install it from https://www.python.org/downloads/ and run START.bat again.

NOTES

- The default chat model runs locally via Ollama using dolphin-ctf:latest.
- You can set CTF_MODEL=glm-5:cloud in .env if you want to use the cloud model.
- Your progress is saved in the browser. Refreshing the page keeps it.
- To reset progress: open browser dev tools -> Application -> Local Storage -> delete ctf_progress.

QUESTIONS
Contact: <your name / email here>
