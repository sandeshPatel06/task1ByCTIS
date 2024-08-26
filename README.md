NAME : SANDESH PATEL <br>
COMPANY : CodTechItSolution <br>
ID : CT08DS5854 <br>
DOMAIN : DATA SCIENCE <br>
DURASION : AUGUST TO SEPTEMBER <br>
Project manager : Mohammed Muzammil Ahmed <br>

# Flask Text-to-Speech Application

## Overview

This Flask web application provides a simple interface to convert text into speech using the `gtts` (Google Text-to-Speech) library. Users can input text, select a language, and generate an MP3 file with the spoken text, which can then be downloaded.

## Features

- **Multiple Languages**: Supports various languages for text-to-speech conversion.
- **MP3 Output**: Generates and downloads an MP3 file with the spoken text.
- **Responsive Design**: User-friendly interface with responsive design adjustments for different devices.

## Technologies

- **Flask**: Web framework for Python.
- **gtts**: Google Text-to-Speech library for converting text into speech.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/sandeshpatel007/task01ByCTIS.git
    cd your-repository
    ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install gtts flask 
    OR...... 
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- **`GET /`**: Render the main interface with language options.
- **`POST /convert`**: Convert text to speech and return an MP3 file.

## Usage

1. Open the application in your browser.
2. Input the text you want to convert to speech.
3. Select the language.
4. Click "Submit" to generate and download the MP3 file.

## Code Overview

### Python Code (`app.py`)

- **`/` Endpoint**: Renders the main HTML interface.
- **`/convert` Endpoint**: Converts text to speech using `gtts`, and returns an MP3 file for download.

### HTML and CSS

The HTML form allows users to input text, select a language, and submit the form to generate the speech output. The CSS provides styling for a clean and responsive user interface.

### CSS (`static/style.css`)

- **Body**: Styles the body with a background image and font.
- **Form Container**: Provides styling for the form container with background color, padding, and shadow.
- **Form Elements**: Styles for form groups, labels, inputs, and buttons.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## Contact

For questions or feedback, you can reach me at [sandeshpatel.sp.93@gmail.com](mailto:sandeshpatel.sp.93@gmail.com).

## GitHub

[GitHub Repository](https://github.com/sandeshpatel007/task1ByCTIS.git)
![image](https://github.com/user-attachments/assets/c383a37c-9d6b-4263-ab1e-7f22ccd98771)
