# PDF Merger

A simple web application that allows users to upload multiple PDF files and combine them into one downloadable document.

## Features

- Upload multiple PDF files
- Review the selected file order
- Choose the output filename
- Merge all pages into one PDF
- Download the merged document
- Display helpful errors for unsupported or password-protected files

## Technologies

- Python
- Streamlit
- pypdf

## Run locally

1. Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2. Start the application:

```bash
streamlit run app.py
```

3. Open the local address displayed in the terminal.

## Deploy on Streamlit Community Cloud

1. Upload this project to a public GitHub repository.
2. Sign in to Streamlit Community Cloud.
3. Select **Create app**.
4. Choose the repository and set the main file path to `app.py`.
5. Deploy the app.

## Why Streamlit instead of Tkinter?

Tkinter creates a desktop window and requires a local graphical display. Streamlit creates a browser-based interface, so it works on Streamlit Community Cloud and can be linked from a portfolio.
