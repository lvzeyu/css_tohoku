source .venv/bin/activate
# source .venv/bin/activate.fish
jupyter-book build ./
ghp-import -n -p -f _build/html