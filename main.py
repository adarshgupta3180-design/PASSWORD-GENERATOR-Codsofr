import tkinter as tk
import sys
import os
import glob

# Add the project directory to sys.path to ensure absolute imports resolve properly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# ---------------------------------------------------------------------------
# Tcl/Tk self-healing: On Windows, some Python distributions place the Tcl
# libraries in a non-standard location. We probe common candidate directories
# and set TCL_LIBRARY / TK_LIBRARY so that tkinter can always find init.tcl.
# ---------------------------------------------------------------------------
def _fix_tcl_library_paths():
    if not sys.platform.startswith("win"):
        return
    # Already set externally — trust it
    if os.environ.get("TCL_LIBRARY") and os.environ.get("TK_LIBRARY"):
        return

    # Candidate root directories to search for tcl8.x / tk8.x sub-folders
    search_roots = [
        os.path.join(os.path.dirname(sys.executable), "tcl"),
        os.path.join(sys.base_prefix, "tcl"),
        r"C:\Users\Aman\AppData\Local\Programs\Python\Python314\tcl",
        r"C:\Python314\tcl",
    ]

    for root in search_roots:
        if not os.path.isdir(root):
            continue
        tcl_dirs = glob.glob(os.path.join(root, "tcl8*"))
        tk_dirs  = glob.glob(os.path.join(root, "tk8*"))
        if tcl_dirs and tk_dirs:
            os.environ.setdefault("TCL_LIBRARY", tcl_dirs[0])
            os.environ.setdefault("TK_LIBRARY",  tk_dirs[0])
            return

_fix_tcl_library_paths()

from src.gui.app import PasswordGeneratorApp

def main():
    # Enable High DPI scaling on Windows to ensure UI elements are crisp
    if sys.platform.startswith("win"):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            # Fallback gracefully if ctypes or system call is not supported
            pass

    # Initialize Tkinter root
    root = tk.Tk()
    
    # Initialize the main Password Generator Application controller
    app = PasswordGeneratorApp(root)
    
    # Run the event loop
    root.mainloop()

if __name__ == "__main__":
    main()
