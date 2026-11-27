"""Install the scenario workspace into a project, preserving existing project files."""
import argparse
from pathlib import Path
from shutil import copyfileobj

SOURCE = Path(__file__).resolve().parents[1]
ROOTS = (".agents", ".codex", ".codex-plugin", "docs", "examples", "prompts",
         "scenarios", "scripts", "AGENTS.md", "README.md", "LICENSE")


def sources():
    for name in ROOTS:
        path = SOURCE / name
        for asset in sorted(path.rglob("*")) if path.is_dir() else [path]:
            if asset.is_file() and "__pycache__" not in asset.parts:
                yield asset.relative_to(SOURCE)


def install(target):
    if target == SOURCE or SOURCE in target.parents or target in SOURCE.parents:
        raise SystemExit("安装目录与插件源目录不能相互包含")
    pending = []
    conflicts = []
    for rel in sources():
        dest = target / rel
        if any(p.is_symlink() or (p.exists() and not p.is_dir())
               for p in dest.parents if p == target or target in p.parents):
            conflicts.append(rel)
        elif dest.is_symlink() or (dest.exists() and not dest.is_file()):
            conflicts.append(rel)
        elif not dest.exists():
            pending.append(rel)
        elif dest.read_bytes() != (SOURCE / rel).read_bytes():
            if rel.as_posix() in {"AGENTS.md", "README.md"}:
                print(f"保留现有 {rel}，请按场景手动合并项目入口。")
            else:
                conflicts.append(rel)
    if conflicts:
        raise SystemExit("发现同名资产或路径冲突；请选择独立目录或先合并：" +
                         ", ".join(str(p) for p in conflicts))
    for rel in pending:
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        with (SOURCE / rel).open("rb") as source, dest.open("xb") as out:
            copyfileobj(source, out)
        if rel.suffix == ".sh":
            dest.chmod(dest.stat().st_mode | 0o100)
    print(f"安装完成：新增 {len(pending)} 个文件，目标 {target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    install(parser.parse_args().project.resolve())
