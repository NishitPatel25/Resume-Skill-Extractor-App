# Resume Skills Extractor

This is a Flask web application that extracts skills from a resume file (PDF or text) based on a predefined list of skills.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/resume-skills-extractor.git
    ```

2. Navigate to the project directory:

    ```bash
    cd resume-skills-extractor
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).
   
3. Upload a resume file (PDF or text format).

4. Click the "Upload" button.

5. The application will extract skills from the uploaded resume and display them on the webpage.

## Screenshot

![Screenshot 2024-05-31 115921](https://github.com/NishitPatel25/Resume-Skill-Extractor-App/assets/117337571/a17dde53-7571-42df-a190-4c8ce66f4307)


## Files

- `app.py`: Flask application code.
- `templates/upload.html`: HTML template for the web interface.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- Flask: Python web framework
- spaCy: Natural language processing library
- PyMuPDF: PDF parsing library

## Contributors

- [Nishit Patel](https://github.com/NishitPatel25)

## License

This project is licensed under the [MIT License](LICENSE).
