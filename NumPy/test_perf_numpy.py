import os
import subprocess
import sys
import tempfile
import textwrap
import timeit
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
SCRIPT_OLD = ROOT_DIR / "iteration.py"
SCRIPT_CLEAN = ROOT_DIR / "iteration_clean.py"


def _write_stub_modules(temp_dir: Path) -> None:
    (temp_dir / "matplotlib").mkdir(parents=True, exist_ok=True)
    (temp_dir / "matplotlib" / "__init__.py").write_text(
        "from . import pyplot\n",
        encoding="utf-8",
    )
    (temp_dir / "matplotlib" / "pyplot.py").write_text(
        textwrap.dedent(
            """
            def imshow(*args, **kwargs):
                pass

            def show():
                pass
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )

    (temp_dir / "sklearn").mkdir(parents=True, exist_ok=True)
    (temp_dir / "sklearn" / "__init__.py").write_text("", encoding="utf-8")
    (temp_dir / "sklearn" / "datasets.py").write_text(
        textwrap.dedent(
            """
            import numpy as np

            def load_sample_image(name):
                return np.zeros((4, 4, 3), dtype=np.uint8)
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def _run_script(script_path: Path, stub_dir: Path) -> None:
    env = os.environ.copy()
    env.setdefault("MPLBACKEND", "Agg")
    env["PYTHONPATH"] = os.pathsep.join(
        [str(stub_dir), env.get("PYTHONPATH", "")]
    ) if env.get("PYTHONPATH") else str(stub_dir)

    subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(ROOT_DIR),
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )


def test_compare_iteration_scripts() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        stub_dir = Path(tmp_dir_name)
        _write_stub_modules(stub_dir)

        old_time = min(
            timeit.repeat(
                lambda: _run_script(SCRIPT_OLD, stub_dir),
                repeat=2,
                number=1,
            )
        )
        clean_time = min(
            timeit.repeat(
                lambda: _run_script(SCRIPT_CLEAN, stub_dir),
                repeat=2,
                number=1,
            )
        )

        print(f"iteration.py: {old_time:.6f}s")
        print(f"iteration_clean.py: {clean_time:.6f}s")
        print(f"difference: {old_time - clean_time:.6f}s")


if __name__ == "__main__":
    test_compare_iteration_scripts()
