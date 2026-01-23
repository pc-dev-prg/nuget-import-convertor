# Payroll Data Transformer (XLSX to CSV)

A robust Python-based desktop utility designed for payroll accountants to recursively search for Excel files and transform them into a specific CSV format required for payroll system imports.

## 🚀 Key Features

- **Interactive Directory Picker**: User-friendly folder selection using native Windows dialogs.
- **Recursive Processing**: Automatically finds all `.xlsx` files in the selected directory and its subfolders.
- **Smart Data Validation**: Powered by Pydantic to ensure data integrity, handling common Excel formatting issues (e.g., float precision, thousand separators).
- **Automated Directory Management**: Creates an `/Import` subdirectory in every location where source files are found.
- **Beautiful Terminal TUI**: Rich terminal output with progress bars, status panels, and detailed error summaries.

## 🛠 Tech Stack

- **Python 3.10+**: Core logic.
- **Pandas & Openpyxl**: High-performance Excel data processing.
- **Pydantic (v2)**: Strict data validation and cleaning.
- **Rich**: Enhanced terminal user interface and progress tracking.
- **Tkinter**: Native directory selection dialog.
- **Pytest**: Comprehensive unit testing suite.

## 📋 Data Transformation Logic

The tool strictly follows these transformation rules for the import format:

1.  **Date Logic (OBD)**: Converts `YYYYMM` to `[M]YYYY` (e.g., `202501` → `12025`, `202511` → `112025`).
2.  **Number Formatting**: Removes thousand separators and converts decimal commas to dots.
3.  **CSV Specification**:
    - **Delimiter**: `;` (Semicolon)
    - **Columns**: `POD`, `L0001` (ID), `L0004` (0), `OBD` (Period), `L4901` (Code), `L4902` (Value), `L4907` (A), `JMENO` (Name from Col B).

## 💻 Getting Started

### Windows (Quick Start)

Simply double-click the **`run.bat`** file. It will:

1. Create a virtual environment (`.venv`) if it doesn't exist.
2. Install all necessary dependencies from `requirements.txt`.
3. Launch the application.

### Manual Installation

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python main.py
   ```

## 🧪 Testing

The project includes a suite of unit tests to verify transformation logic.

Run tests using:

```bash
export PYTHONPATH=$PYTHONPATH:.  # Ensure the root is in path
pytest tests/test_logic.py
```

## 📖 Localization

A detailed user manual in Czech is available in [Manual.md](./Manual.md) or [Manual.pdf](./Manual.pdf).

## 📄 License

This project is private and intended for internal payroll processing use.
