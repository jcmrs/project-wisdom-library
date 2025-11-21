import yaml
import re
import os

# This script will require the PyYAML package.
# Ensure it is installed in the GitHub Actions workflow:
# pip install PyYAML

with open("issue_body.txt", "r", encoding="utf-8") as f:
    issue_body = f.read()

# Find the YAML code block
match = re.search(r"```yaml\n(.*?)\n```", issue_body, re.DOTALL)

if match:
    yaml_content = match.group(1)
    data = yaml.safe_load(yaml_content)

    # Access the nested agent_prompt dictionary
    agent_data = data.get("agent_prompt", {})

    depth = agent_data.get("depth", "")
    target = agent_data.get("target", "")
    intent = agent_data.get("intent", "")
    clues = agent_data.get("clues", "")
    
    # The 'tools' in YAML are expected to be a list of strings
    tools_list = agent_data.get("tools", [])
    tools_str = ", ".join(tools_list)

else:
    # Fallback to empty values if no YAML block is found
    depth, target, intent, clues, tools_str = "", "", "", "", ""

with open("issue_vars.sh", "w") as out:
    out.write(f'AGENT_TARGET="{target}"\n')
    out.write(f'AGENT_DEPTH="{depth}"\n')
    out.write(f'AGENT_TOOLS="{tools_str}"\n')
    out.write(f'AGENT_INTENT="{intent}"\n')
    out.write(f'AGENT_CLUES="{clues}"\n')

