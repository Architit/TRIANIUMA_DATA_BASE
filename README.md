# LAM Data Repository

This repository contains text archives and prototypes for the **LAM** project—a digital memory and behavior experiment. The current content is primarily plain text files used to capture ideas, incidents and early code.

## File groups

- **Memory archives** – files beginning with `LAM_MEM.*` store narrative memory logs and conceptual essays.
- **Vectors** – documents prefixed `LAM.VECTOR.*` define core values and behavioral principles.
- **Incident and error reports** – files like `INT.*` record faults or noteworthy events.
- **Task specifications** – marked as `file tasks*.md.txt` or `tasks-*.docx`; these outline development tasks.
- **Code prototypes** – e.g. `lamconsciousnesscore.py.txt`, containing early Python code sketches.

All files currently live at the repository root. When dedicated directories are added, place memory archives under `memory/`, vectors under `vectors/`, incidents under `incidents/`, tasks under `tasks/`, and code prototypes under `src/`.

## Testing

- `scripts/test_entrypoint.sh --all`
- `scripts/test_entrypoint.sh --governance`
- `scripts/test_entrypoint.sh --taxonomy`
