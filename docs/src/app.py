import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from services.blob_service import upload_blob
from services.id_service import analyze_id


SUPPORTED_FILE_TYPES = ["png", "jpg", "jpeg", "pdf", "txt"]


def configure_interface():
    st.title("Upload de arquivos - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=SUPPORTED_FILE_TYPES)

    if uploaded_file is not None:
        file_name = uploaded_file.name
        if file_name.split('.')[-1].lower() not in SUPPORTED_FILE_TYPES:
            st.write("Formato de arquivo não suportado. Por favor, envie um arquivo PNG, JPG, JPEG, PDF ou TIFF.")
            return

        blob_url = upload_blob(uploaded_file, file_name)
        print(f"Blob URL: {blob_url}")
        if blob_url:
            st.write(f"Arquivo {file_name} enviado com sucesso para o Azure Blob Storage")
            id_info = analyze_id(blob_url)
            if id_info:
                show_image_and_validation(blob_url, id_info)
            else:
                st.write("Erro ao analisar o documento de identidade")
                print("Erro ao analisar o documento de identidade")
        else:
            st.write("Erro ao enviar o arquivo")
            print("Erro ao enviar o arquivo")


def show_image_and_validation(blob_url, id_info):
    st.image(blob_url, caption="Imagem enviada!", use_container_width=True)
    st.write("Validação do cartão de crédito:")
    if id_info and id_info["id_name"]:
        st.markdown(f"<h3 style='color: green;'>Documento de identidade válido</h3>", unsafe_allow_html=True)
        st.write(f"Número do documento: {id_info['id_number']}")
        st.write(f"Data de nascimento: {id_info['date_of_birth']}")
        st.write(f"Data de validade: {id_info['expiration_date']}")
    else:
        st.markdown(f"<h3 style='color: red;'>Docuento de identidade inválido</h3>", unsafe_allow_html=True)
        st.write("Não foi possível validar o documento de identidade")
        print("Não foi possível validar o documento de identidade")


if __name__ == "__main__":
    configure_interface()
