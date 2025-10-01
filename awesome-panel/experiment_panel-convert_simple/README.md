https://panel.holoviz.org/how_to/wasm/convert.html

```bash
uvx --from 'panel==1.8.1' panel convert script.py --to pyodide-worker --out pyodide

# Compiled and faster
uvx --from 'panel==1.8.1' panel convert script.py --compiled --to pyodide-worker --out pyodide


# Start a web server locally
(cd pyodide && uvx python -m http.server)

Open http://localhost:8000/pyodide/script.html to try out the
```

Takes long to load but work fine!
