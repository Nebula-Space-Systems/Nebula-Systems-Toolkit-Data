from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

try:
    __version__ = version("nebula-data")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"


def get_package_root() -> Path:
    """Return the installed package root for bundled Nebula data assets."""

    return Path(__file__).resolve().parent


def _require_directory(path: Path, description: str) -> Path:
    if not path.is_dir():
        raise FileNotFoundError(f"Expected {description} at '{path}', but it was not found.")
    return path


def get_cartopy_data_dir() -> Path:
    """Return the installed offline Cartopy data directory."""

    return _require_directory(get_package_root() / "cartopy", "installed nebula-data Cartopy directory")


def get_orekit_data_dir() -> Path:
    """Return the installed offline Orekit data directory."""

    return _require_directory(
        get_package_root() / "orekit-data",
        "installed nebula-data Orekit directory",
    )


__all__ = [
    "__version__",
    "get_cartopy_data_dir",
    "get_orekit_data_dir",
    "get_package_root",
]
