#!/usr/bin/env python3
import json
import sys

input_path = sys.argv[1] if len(sys.argv) > 1 else "preds.json"
sub_path = input_path.split("/")
sub_path[-1] = "preds_converted.json"
output_path = sys.argv[2] if len(sys.argv) > 2 else "/".join(sub_path)

with open(input_path) as f:
    data = json.load(f)

result = []
for entry in data.values():
    item = dict(entry)
    item["prefix"] = item.pop("model_name_or_path").replace("/", "_")
    item["patch"] = item.pop("model_patch")
    result.append(item)

with open(output_path, "w") as f:
    json.dump(result, f, indent=2)

print(f"Converted {len(result)} entries -> {output_path}")
