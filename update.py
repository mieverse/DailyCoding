import os
import re

EXCLUDE = {"template.py", "update.py"}
SKIP_DIRS = {".git"}

README = "README.md"


def get_solved_files():
    files = []
    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".py") and f not in EXCLUDE:
                files.append((root, f))
    return sorted(files, key=lambda x: x[1])


def parse_metadata(filepath):
    metadata = {
        "number": "???",
        "title": "???",
        "difficulty": "???",
        "company": "???",
        "topic": "???",
        "path": filepath.replace("\\", "/").lstrip("./"),
    }

    try:
        with open(filepath, "r") as f:
            content = f.read()

        # p202 — Integer Palindrome [Easy]
        first_line = re.search(r'p(\d+)\s*[—-]+\s*(.+?)\s*\[(Easy|Medium|Hard)\]', content)
        if first_line:
            metadata["number"] = first_line.group(1).zfill(3)
            metadata["title"] = first_line.group(2).strip()
            metadata["difficulty"] = first_line.group(3).strip()

        # Asked by Palantir | Topic: Math
        company = re.search(r'Asked by (.+?)\s*\|', content)
        if company:
            metadata["company"] = company.group(1).strip()

        topic = re.search(r'Topic:\s*(.+)', content)
        if topic:
            metadata["topic"] = topic.group(1).strip()

    except Exception:
        pass

    return metadata


def build_table(files):
    rows = []
    for root, filename in files:
        filepath = os.path.join(root, filename)
        meta = parse_metadata(filepath)
        link = f'[{meta["title"]}]({meta["path"]})'
        row = f'| {meta["number"]} | {link} | {meta["difficulty"]} | {meta["company"]} | {meta["topic"]} |'
        rows.append((meta["number"], row))

    rows.sort(key=lambda x: x[0])
    return "\n".join(r for _, r in rows)


def update(table, count):
    with open(README, "r") as f:
        content = f.read()

    content = re.sub(r'## Progress: \d+ solved', f'## Progress: {count} solved', content)

    content = re.sub(
        r'(\|---\|.*\|\n)[\s\S]*',
        lambda m: m.group(1) + table + "\n",
        content
    )

    with open(README, "w") as f:
        f.write(content)

    print(f"README updated — {count} solved.")


if __name__ == "__main__":
    files = get_solved_files()
    table = build_table(files)
    update(table, len(files))