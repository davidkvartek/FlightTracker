# Flight Tracker

A simple web application to track flight status in real-time (mock data).

## Features

- Search for flights by flight number.
- View start/end times and locations.
- Visual flight path representation.
- Mock API for demonstration purposes.

## Getting Started

### Prerequisites

- Python 3.x installed.
- `pip` package manager.

### Installation

1.  Clone the repository (if applicable) or download the source code.
2.  Navigate to the project directory:
    ```bash
    cd FlightTracker
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the Flask development server:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Running Tests

This project includes unit tests to verify functionality. To run the tests:

```bash
python -m unittest discover tests
```

or specifically:

```bash
python tests/test_app.py
```

## Mock Data

Currently, the app uses mock data. You can try searching for these flight numbers:
- **AA123**
- **DL456**
- **UA789**