import json
import sys

from jinja2 import Environment, FileSystemLoader

INPUT_FILE_NAME = "heating01.json"
OUTPUT_FILE_NAME = "area.yaml"
TEMPLATE_FILE_NAME = "heating.j2"


if sys.argv[1]:
    input_file_name = sys.argv[1]
else:
    input_file_name = INPUT_FILE_NAME


env = Environment(loader=FileSystemLoader("."))

with open(input_file_name, encoding="utf-8") as f:
    data = json.load(f)


circuit_count = 0
for a in data["areas"]:
    circuit_count += len(a["circuits"])

print(f"--Anzahl der Stellkreise: {circuit_count}")

circuit_offset = 0
for aindex, a in enumerate(data["areas"]):
    print("Processing area: " + a["name"])

    weighted_sensors_string = []
    weight_sum = 0.0
    for i, s in enumerate(a["ha_sensors"]):
        weight_sum += float(s["weight"])
        s["id"] = f"sensor_{a['id']}_{str(i + 1)}"
        weighted_sensors_string.append(
            f"id({s['id']}).state * {float(s['weight']):0.1f}"
        )

    weighted_sensors_string = (
        "(" + " + ".join(weighted_sensors_string) + ")/" + str(weight_sum)
    )

    a["weighted_sensors"] = weighted_sensors_string

    # insert globals into each area
    a["interval"] = data["interval"]
    a["level"] = data["level"]
    a["friendly_name"] = data["friendly_name"]
    a["circuit_offset"] = circuit_offset
    # print(f" -- circuit_offset: {circuit_offset}")
    a["circuit_count"] = circuit_count

    circuit_offset += len(a["circuits"])

    template = env.get_template(TEMPLATE_FILE_NAME)

    rendered_template = template.render(a)
    output_file_name = f"area_{a['id']}.yaml"
    print(f" - output file name: {output_file_name}")
    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(rendered_template)
