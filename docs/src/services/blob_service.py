import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from src.utils.config import Config


def upload_blob(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.STORAGE_CONNECTION)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        blob_client.upload_blob(file, overwrite=True)
        blob_url = blob_client.url
        print(f"Blob URL: {blob_url}")
        return blob_url
    except Exception as e:
        st.write(f"Erro ao enviar o arquivo: {e}")
        print(f"Exception: {e}")
        return None
