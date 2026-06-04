#!/bin/sh
set -eu

echo "Preparing Ollama models..."

ollama pull dolphin-mistral
ollama create dolphin-ctf -f /models/Modelfile-ctf
ollama pull nomic-embed-text
ollama pull llama3.1

echo "Ollama models are ready."
