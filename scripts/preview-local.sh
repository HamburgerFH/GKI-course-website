#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "$project_dir"

export QUARTO_PYTHON="$project_dir/.venv/bin/python"
if [[ ! -x "$QUARTO_PYTHON" ]]; then
  echo "Missing Python environment: $project_dir/.venv" >&2
  exit 1
fi

# Refresh the kernel path when the checkout has been moved.
"$QUARTO_PYTHON" -m ipykernel install \
  --prefix "$project_dir/.venv" --name gki-venv --display-name "GKI local"

exec quarto preview --no-browser --host 127.0.0.1 \
  --port "${GKI_PREVIEW_PORT:-4444}" "$@"
