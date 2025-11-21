import os
import json
import glob

def main():
    fragments_dir = "catalogue/fragments"
    manifest_path = "catalogue/manifest.json"
    index_path = "catalogue/index.md"
    
    master_manifest = []

    # Read all fragment files
    fragment_files = glob.glob(os.path.join(fragments_dir, "*.json"))
    for fragment_file in fragment_files:
        with open(fragment_file, "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    master_manifest.extend(data)
            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {fragment_file}")
                continue

    # Sort the manifest for consistency, e.g., by issue number then artifact path
    master_manifest.sort(key=lambda x: (int(x.get("issue", 0)), x.get("artifact", "")))

    # Write the new master manifest
    with open(manifest_path, "w") as f:
        json.dump(master_manifest, f, indent=2)

    # Write the new index file
    with open(index_path, "w") as f:
        f.write("# Wisdom Library Catalogue Index\n\n")
        if not master_manifest:
            f.write("No artifacts have been generated yet.\n")
        else:
            for entry in master_manifest:
                if all(k in entry for k in ("artifact", "issue", "target", "intent", "created")):
                    f.write(f"- [{entry['artifact']}]({entry['artifact']}) — Issue #{entry['issue']}, Target: {entry['target']}, Intent: {entry['intent']}, Date: {entry['created']}\n")
                else:
                    f.write(f"- [INVALID MANIFEST ENTRY: {entry}]\n")

if __name__ == "__main__":
    main()
