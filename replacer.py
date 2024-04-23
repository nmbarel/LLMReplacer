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
    if flow.request.host == "gemini.google.com" and flow.request.urlencoded_form["f.req"]:
        ctx.log.info(flow.request.urlencoded_form["f.req"])
        requestContent = flow.request.urlencoded_form["f.req"]
        promptstartIndex = 11 # gemini messages always start with 11 chars of filler before the prompt is written
        promptendIndex = promptstartIndex + requestContent[promptstartIndex:].find("\\\",0,null,null,null,null") # this always comes after the prompt
        newContent = requestContent[:promptstartIndex] + prompt + requestContent[promptendIndex:]
        flow.request.urlencoded_form["f.req"] = newContent
