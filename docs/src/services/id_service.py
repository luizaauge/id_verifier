import logging
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.exceptions import HttpResponseError

from src.utils.config import Config


def analyze_id(id_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        print(f"Analysing ID document from URL: {id_url}")

        id_info = document_client.begin_analyze_document(
            "prebuilt-idDocument", {"url": id_url})
        result = id_info.result()

        for document in result.documents:
            fields = document.fields
            return {
                "id_name": fields.get("FullName", {}).get("content"),
                "id_number": fields.get("DocumentNumber", {}).get("content"),
                "date_of_birth": fields.get("DateOfBirth", {}).get("content"),
                "expiration_date": fields.get("DateOfExpiration", {}).get("content"),
            }
    except HttpResponseError as e:
        logging.error(f"HttpResponseError: {e.message}")
        if e.response:
            logging.error(f"Response: {e.response.text()}")
        return None
    except Exception as e:
        logging.error(f"Exception: {e}")
        return None
