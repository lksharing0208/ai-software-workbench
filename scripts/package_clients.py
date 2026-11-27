"""从同一份 skills/ 生成 ChatGPT 插件包和 Claude 单 Skill 包，使用 Python 标准库。"""
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"


def add_directory(archive, source, base):
    for path in sorted(source.rglob("*")):
        if path.is_file():
            archive.write(path, path.relative_to(base).as_posix())


def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/validate_skills.py")], check=True)
    adapter = ROOT / "clients/chatgpt"
    manifest = json.loads((adapter / "plugin.json").read_text(encoding="utf-8"))
    DIST.mkdir(exist_ok=True)
    plugin = DIST / f"{manifest['name']}-chatgpt.zip"
    with ZipFile(plugin, "w", ZIP_DEFLATED) as archive:
        add_directory(archive, adapter, adapter)
        add_directory(archive, SKILLS, ROOT)

    claude = DIST / "claude"
    claude.mkdir(exist_ok=True)
    skills = sorted(SKILLS.glob("*/SKILL.md"))
    for entry in skills:
        with ZipFile(claude / f"{entry.parent.name}.zip", "w", ZIP_DEFLATED) as archive:
            add_directory(archive, entry.parent, SKILLS)
    print(f"{plugin.name} + {len(skills)} Claude Skill ZIPs")


if __name__ == "__main__":
    main()
