import json

from jinja2 import Environment, FileSystemLoader

INPUT_FILE_NAME = "heating01.json"
OUTPUT_FILE_NAME = "heating.yaml"
TEMPLATE_FILE_NAME = "heating.j2"

env = Environment(loader=FileSystemLoader("."))

with open(INPUT_FILE_NAME, encoding="utf-8") as f:
    data = json.load(f)

template = env.get_template(TEMPLATE_FILE_NAME)

rendered_template = template.render(data)

with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as f:
    f.write(rendered_template)
