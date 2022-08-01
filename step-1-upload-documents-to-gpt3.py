#!/usr/bin/env python
# coding: utf-8

import gzip
import openai
openai.api_key = "INSERT YOUR KEY HERE"

with gzip.open('serious-seller-podcast.json.gz', 'rb') as f:
    file_content = f.read()
    file_content = file_content.decode('utf-8')

content = file_content[1:-1].replace('},{',  '}\n{').replace('"date":','"metadata":')

print(len(content.splitlines()))

with open('tmp/serious-seller-podcast.jsonl', 'w', encoding='utf-8') as f:
    f.write(content)

response = openai.File.create(file=open("tmp/serious-seller-podcast.jsonl"), purpose='answers')
print(response)