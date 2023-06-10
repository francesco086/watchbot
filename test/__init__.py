import os
from unittest import TestCase

import openai


class BaseTestWatchBot(TestCase):
    def setUp(self) -> None:
        openai.api_type = os.environ["OPENAI_API_TYPE"]
        openai.api_version = os.environ["OPENAI_API_VERSION"]
        openai.api_base = os.environ["OPENAI_API_BASE"]
        openai.api_key = os.environ["OPENAI_API_KEY"]
