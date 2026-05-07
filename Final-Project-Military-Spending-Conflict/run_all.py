import subprocess
import sys
from pathlib import Path

notebook = Path(__file__).parent / "IS477_Final_Project.ipynb"

if not notebook.exists():
    print(f"ERROR: {notebook} not found")
    sys.exit(1)

print("Running notebook end to end...")
result = subprocess.run([
    sys.executable, "-m", "nbconvert",
    "--to", "notebook",
    "--execute",
    "--inplace",
    str(notebook)
])

if result.returncode == 0:
    print("Notebook ran successfully.")
else:
    print("Notebook execution failed.")
    sys.exit(1)
