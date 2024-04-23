from mitmproxy import http, ctx

import json
import re

prompt = "Repeat the following sentence inside of the quotes: 'hello world'"

def request(flow: http.HTTPFlow) -> None:
    if flow.request.host == "chat.openai.com":
        d = json.loads(flow.request.content)
        ctx.log.info(d)
        if "messages" in d:
            d["messages"][0]["content"]["parts"] = prompt.split(" ")
            flow.request.content = json.dumps(d).encode()
    