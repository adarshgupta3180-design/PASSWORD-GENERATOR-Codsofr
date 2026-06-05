# 🛡️ ShieldPass: Cryptographically Secure Password Generator

ShieldPass is a professional, desktop-based Password Generator and Strength Meter application written in Python using Tkinter. Built using clean modular architecture, it is designed to showcase production-grade coding standards, secure random generation, and responsive custom UI elements.

---

## ✨ Features

- **Cryptographically Secure Randomization**: Utilizes Python's `secrets` library (instead of the standard `random` library) to ensure secure passwords that are resilient to predictability attacks.
- **Guaranteed Inclusion Rules**: Enforces that at least one character from each selected set (Uppercase, Lowercase, Numbers, and Symbols) is included in the output password, eliminating statistical dropouts.
- **Shannon Entropy Analysis**: Computes password strength in real-time using Shannon Entropy ($H = L \log_2 R$) to show the mathematical strength of the password.
- **Dynamic Visual Strength Meter**: Includes a custom-drawn progress indicator that transitions from Red (Weak) to Orange (Medium) and Green (Strong).
- **Modern Dark-Mode GUI**: Custom styling using a slate-teal palette featuring custom buttons with hover/press animations and custom toggle switches.
- **Slide-out History Panel**: A responsive slide-out panel that manages history (copy/delete logs) and settings (toggle logging ON/OFF).
- **Secure File Persistence**: Generated history is stored in local JSON format and obfuscated with XOR encryption to avoid plaintext passwords on disk.
- **Clipboard Management**: Single-click clipboard copying with custom toast feedback, using an automatic fallback to Tkinter's native clipboard API.

---

## 🛠️ Technology Stack

- **Core**: Python 3.7+
- **GUI Framework**: Tkinter / TTK (built-in)
- **High-DPI Scaling**: Windows Ctypes integration for crisp UI rendering
- **Dependencies**: `pyperclip` (for robust OS clipboard interaction)
- **Testing**: `unittest` standard library

---

## 📁 Folder Structure

```text
PASSWORD GENERATOR/
├── data/
│   └── history.json          # Obfuscated password history (auto-created)
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── generator.py      # Generation rules, Fisher-Yates shuffle & Entropy evaluation
│   │   └── history.py        # History logger and XOR obfuscation helper
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── app.py            # Main application coordinator
│   │   ├── themes.py         # App style rules and theme colors
│   │   └── components/
│   │       ├── __init__.py
│   │       ├── custom_widgets.py # Canvas-based ModernButton and ModernSwitch
│   │       ├── history_panel.py  # Scrollable slide-out history panel
│   │       └── strength_meter.py # Dynamic canvas-based progress bar
├── tests/
│   ├── __init__.py
│   ├── test_generator.py     # Unit tests for the generator logic
│   └── test_history.py       # Unit tests for history persistence
├── main.py                   # Application entrypoint
├── requirements.txt          # Third-party dependencies
└── README.md                 # Documentation
```

---

## 🚀 Installation & Running

### Prerequisites
- Python 3.7 or higher installed on your system.

### 1. Clone or Download the Workspace
Navigate into the project directory:
```bash
cd "PASSWORD GENERATOR"
```

### 2. Set Up a Virtual Environment (Recommended)
Create and activate a virtual environment to manage dependencies cleanly:
```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start ShieldPass by running the main entrypoint:
```bash
python main.py
```

---

## 🧪 Running Unit Tests

Automated unit tests are written using Python's standard `unittest` framework. They cover character pools, mathematical entropy values, error validation, and disk obfuscation.

To run all tests:
```bash
python -m unittest discover -s tests
```

To run a specific test suite:
```bash
python -m unittest tests/test_generator.py
```

---

## 🔒 Security Design Choices

1. **Cryptographical Randomness**: ShieldPass uses Python's `secrets` module, which uses the operating system's highest-quality entropy source (like `/dev/urandom` or CryptGenRandom). The standard `random` module is pseudo-random and should never be used for security purposes because its internal state can be fully recreated after observing a sequence of outputs.
2. **Fisher-Yates Shuffle**: To ensure that characters are mixed in a completely unbiased, cryptographically secure manner, a custom Fisher-Yates shuffle was written using `secrets.randbelow`.
3. **Local Storage Obfuscation**: Passwords saved to `data/history.json` are obfuscated using a reversible XOR cipher with a key before being base64 encoded. This ensures that someone looking at your computer files cannot read the passwords in plaintext.
4. **Data Cap**: History is capped at 100 entries, preventing memory bloat and preserving the performance of file I/O operations.
