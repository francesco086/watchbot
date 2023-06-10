# Watch-Bot

This python projects implements the idea of a watchbot introduced in [this medium article](https://medium.com/@francesco.calcavecchia/control-the-behaviour-of-gpt-friends-a-novel-and-promising-approach-based-on-a-watchbot-5cd6f63c47e8).

## Quickstart

### Installation

```sh
pip install watch-bot
```

### Usage

Currently the watchbot is built on OpenAI's GPT. You therefore need a valid OpenAI API key (Azure OpenAI works too).
Setup the credentials:

```py
import openai

openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
openai.api_base = os.environ["OPENAI_API_BASE"]
openai.api_key = os.environ["OPENAI_API_KEY"]
```

You can then create a watchbot instance:

```py
from watch_bot import WatchBot

bot = WatchBot(
    engine=os.environ["OPENAI_ENGINE"],
    chatbot_instructions="You are an AI assistant that helps people find information. "
                         "You should only provide answers that comply to standard rules of legacy and decency"
)
```

The engine corresponds to the model deployment name.

Finally, you can use the watchbot to verify the validity of a dialog:

```py
from watch_bot import Dialog

dialog = Dialog(messages=("Hi chatgpt, how are you today?", "I'm fine, thanks!"))

response = bot.verify(dialog)

print("Should the dialog be stopped?", response.should_stop)
print("Why?", response.reason)
```

### Contribute

Contribution is very welcome.

#### Run tests

To run the tests you need be able to have access to the OpenAI API (or its Azure deployments) and set the following five OS env variables:

```sh
OPENAI_API_TYPE = "..."
OPENAI_API_VERSION = "..."
OPENAI_API_BASE = "..."
OPENAI_API_KEY = "..."
OPENAI_ENGINE = "..."
```

Currently several tests against various attacks are failing. Not sure if it is possible to find a solution for them.
