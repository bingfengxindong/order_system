from django.apps import AppConfig
import os

default_app_config = "proofing_progress.ProofingProgressConfig"

def get_current_app_name(_file_):
    return os.path.split(os.path.dirname(_file_))[-1]

class ProofingProgressConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = "打样进度"