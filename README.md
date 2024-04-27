## LLMReplacer
Simple script for mitmproxy that catches messages to popular LLM websites and replaces the question asked, all while the end user is oblivious

# How to use
---
simply download mitmproxy, and run it like so: mitmdump -s /path/to/replacer.py
In order for the client computers to view the connection to the proxied sites as secure, you will need to create a Certificate Authority (tutorials on how to do so using OpenSSL are available online), add it to the clients' trust store, and replace the ~/.mitmproxy/mitmproxy-ca.pem file with your own.
