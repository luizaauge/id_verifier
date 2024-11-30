# ID Document Analysis with Azure Document Intelligence

This Python-based application leverages Azure's Document Intelligence capabilities to analyze ID documents. It extracts key information such as full name, document number, date of birth, and expiration date from ID documents. The application interacts with Azure's Document Intelligence API using the `azure-ai-documentintelligence` library. It also provides a user-friendly interface built with Streamlit to easily interact with and visualize the results.

## Features
- Extract key information from ID documents: full name, document number, date of birth, expiration date.
- User-friendly interface powered by Streamlit for easy interaction.
- Secure management of API keys and endpoints using environment variables.
- Simple installation and setup via `pip` and `requirements.txt`.

## Installation

### Prerequisites
- Python 3.7+
- Azure Document Intelligence API key (can be obtained from Azure Portal)
- Streamlit

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/id-document-analysis.git
   cd id-document-analysis
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for Azure API credentials: Create a .env file in the root directory and add the following:

   ```bash
   AZURE_API_KEY=<your_azure_api_key>
   AZURE_ENDPOINT=<your_azure_endpoint>
   ```

5. Run the application:

   ```bash
   Copiar código
   streamlit run app.py
   Open your browser and navigate to the URL provided by Streamlit (typically http://localhost:8501) to interact with the application.
   ```

## Usage

1. **Upload an ID Document**
   - Open the application in your browser at the provided Streamlit URL (typically `http://localhost:8501`).
   - Use the file uploader in the user interface to upload an ID document (such as a passport, driver's license, or other government-issued IDs).

2. **Document Analysis**
   - The application will send the uploaded document to Azure's Document Intelligence API for analysis.
   - The API will extract key details from the ID document, including:
     - **Full Name**: The name of the individual on the ID.
     - **Document Number**: The unique identification number of the document.
     - **Date of Birth**: The individual's date of birth.
     - **Expiration Date**: The expiration date of the ID document.

3. **View Results**
   - After the document has been processed, the extracted information will be displayed on the Streamlit interface.
   - You will see the details in a readable format, ready for review or further processing.

4. **Additional Features**
   - If needed, you can upload multiple documents for analysis one by one.
   - The user interface is designed to be intuitive, with clear feedback and error handling for unsupported or invalid documents.

## Example Workflow

1. Open the application in your browser.
2. Upload an ID document.
3. Wait for the processing to complete.
4. View the extracted information such as full name, document number, date of birth, and expiration date on the results page.

Note: Make sure the uploaded document is clear and legible for optimal results.

## Project Structure

The project directory is organized as follows:

```bash
   id-document-analysis/
   │
   ├── app.py                  # Streamlit interface and application logic
   ├── requirements.txt        # Python dependencies
   ├── .env                    # Environment variables (API keys and endpoints)
   ├── README.md               # Project documentation
   └── images/                 # Folder for storing uploaded ID images (if needed)
```

## Dependencies

The project requires the following Python libraries:

- **`azure-ai-documentintelligence`**: Azure SDK for interacting with the Document Intelligence API.
- **`streamlit`**: A framework for building interactive web applications.
- **`python-dotenv`**: To load environment variables from a `.env` file.

To install the required dependencies, you can use the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

API Key: Obtain your API key from the Azure Portal after setting up Document Intelligence and include it in your .env file.
Azure Endpoint: The endpoint for the Azure service should also be added to the .env file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### MIT License

The MIT License (MIT)

Copyright (c) [2024] [Luiza Auge]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
