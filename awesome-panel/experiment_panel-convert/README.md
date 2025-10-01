https://panel.holoviz.org/how_to/wasm/convert.html

```bash
uvx --from 'panel==1.8.1' panel convert script.py --to pyodide-worker --out pyodide --requirements xgboost scikit-learn pandas

# Start a web server locally
uvx python -m http.server 

Open http://localhost:8000/pyodide/script.html to try out the
```


Error:
```
ERROR:bokeh.application.application:Error running application handler <panel.io.handlers.ScriptHandler object at 0x731241eeb620>: No module named 'sklearn'
File 'script.py', line 3, in <module>:
from sklearn.datasets import load_iris Traceback (most recent call last):
  File "/home/maerki/.cache/uv/archive-v0/HRjRGKqzmceI2qRzXAekx/lib/python3.13/site-packages/panel/io/handlers.py", line 495, in run
    exec(self._code, module.__dict__)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/maerki/experiment/experiment_pyscript/experiment_pyscript/awesome-panel/experiment_panel-convert/script.py", line 3, in <module>
    from sklearn.datasets import load_iris
ModuleNotFoundError: No module named 'sklearn'
 
Failed to convert /home/maerki/experiment/experiment_pyscript/experiment_pyscript/awesome-panel/experiment_panel-convert/script.py to pyodide-worker target: The file /home/maerki/experiment/experiment_pyscript/experiment_pyscript/awesome-panel/experiment_panel-convert/script.py does not publish any Panel contents. Ensure you have marked items as servable or added models to the bokeh document manually.
```