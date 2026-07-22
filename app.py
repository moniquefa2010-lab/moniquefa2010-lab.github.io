import io

import streamlit as st
from pypdf import PdfReader, PdfWriter


st.set_page_config(
    page_title="PDF Merger",
    page_icon="📄",
    layout="centered",
)

st.title("📄 PDF Merger")
st.write("Upload two or more PDF files, arrange them in the order you want, and download one merged PDF.")

uploaded_files = st.file_uploader(
    "Select PDF files",
    type=["pdf"],
    accept_multiple_files=True,
    help="Files are merged in the order shown below.",
)

if uploaded_files:
    st.subheader("Selected files")
    for number, uploaded_file in enumerate(uploaded_files, start=1):
        size_mb = uploaded_file.size / (1024 * 1024)
        st.write(f"{number}. **{uploaded_file.name}** — {size_mb:.2f} MB")

    output_name = st.text_input(
        "Merged file name",
        value="merged_document.pdf",
    ).strip()

    if output_name and not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    if len(uploaded_files) < 2:
        st.warning("Please upload at least two PDF files.")
    else:
        if st.button("Merge PDFs", type="primary", use_container_width=True):
            try:
                writer = PdfWriter()

                for uploaded_file in uploaded_files:
                    uploaded_file.seek(0)
                    reader = PdfReader(uploaded_file)

                    if reader.is_encrypted:
                        try:
                            reader.decrypt("")
                        except Exception as exc:
                            raise ValueError(
                                f'"{uploaded_file.name}" is password-protected and cannot be merged.'
                            ) from exc

                    for page in reader.pages:
                        writer.add_page(page)

                merged_pdf = io.BytesIO()
                writer.write(merged_pdf)
                writer.close()
                merged_pdf.seek(0)

                st.success(
                    f"Successfully merged {len(uploaded_files)} PDFs "
                    f"into {len(PdfReader(merged_pdf).pages)} pages."
                )
                merged_pdf.seek(0)

                st.download_button(
                    label="Download merged PDF",
                    data=merged_pdf,
                    file_name=output_name or "merged_document.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            except Exception as error:
                st.error(f"Unable to merge the selected files: {error}")
else:
    st.info("Upload your PDF files to begin.")

st.caption("Your files are processed only for the current session.")
