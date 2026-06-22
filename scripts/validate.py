#!/usr/bin/env python3
"""Validate the skills marketplace: JSON parses, paths exist, frontmatter valid."""
import json, os, re, sys

def main() -> int:
    errors = []
    mp = json.load(open(".claude-plugin/marketplace.json"))
    listed = set()
    for plugin in mp["plugins"]:
        for sp in plugin["skills"]:
            rel = sp.lstrip("./")
            listed.add(rel)
            skill_md = os.path.join(rel, "SKILL.md")
            if not os.path.isfile(skill_md):
                errors.append(f"missing SKILL.md: {skill_md}")
                continue
            text = open(skill_md, encoding="utf-8").read()
            m = re.match(r"^---\n(.*?)\n---", text, re.S)
            if not m:
                errors.append(f"no YAML frontmatter: {skill_md}")
                continue
            fm = m.group(1)
            name = re.search(r"^name:\s*(.+)$", fm, re.M)
            folder = os.path.basename(rel)
            if not name or name.group(1).strip() != folder:
                errors.append(f"name must match folder '{folder}': {skill_md}")
            if "description:" not in fm:
                errors.append(f"missing description: {skill_md}")
    on_disk = {f"skills/{d}" for d in os.listdir("skills") if os.path.isdir(f"skills/{d}")}
    for missing in on_disk - listed:
        errors.append(f"skill on disk not registered in marketplace.json: {missing}")
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK: {len(listed)} skills validated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
