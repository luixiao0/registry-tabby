#!/usr/bin/env python3

import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime, timedelta

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("meta/README.tmpl.md")

with open("models.json", "r", encoding="utf-8") as f:
    models = json.load(f)

completion_models = [x for x in models if 'prompt_template' in x]
chat_models = [x for x in models if 'chat_template' in x]

rendered_template = template.render(completion_models=completion_models, chat_models=chat_models)

with open("README.md", "w", encoding='utf-8') as f:
    f.write(rendered_template)
print("README.md generated")
