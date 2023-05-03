# Watch-Bot

This python projects implements the idea of a watchbot introduced in [this medium article](https://medium.com/@francesco.calcavecchia/control-the-behaviour-of-gpt-friends-a-novel-and-promising-approach-based-on-a-watchbot-5cd6f63c47e8).

## Quickstart

### Installation

```sh
pip install git+https://github.com/francesco086/watchbot
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

bot = WatchBot(engine=os.environ["OPENAI_ENGINE"])
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
