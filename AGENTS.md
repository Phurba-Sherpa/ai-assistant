# AGENTS.md

Guidance for agentic coding tools working in this repository.
Scope: entire repo (`/Users/phurba/personal/ai-assistant`).

## Project Snapshot

- Primary code is in `backend/`.
- Language is Python (`requires-python = ">=3.11"`).
- Dependency/tool runner is `uv`.
- Main scripts today: `backend/chat.py`, `backend/search.py`, `backend/store.py`.
- Current style is script-oriented and env-driven.
- There are no committed tests yet.
- There is no configured linter/formatter/type checker yet.

## Rules Files Check

At time of writing, these files were not found:
- `.cursorrules`
- `.cursor/rules/`
- `.github/copilot-instructions.md`

If any of those files are added later, treat them as higher-priority constraints and update this file.

## Where To Run Commands

Run Python project commands from `backend/`.

Example:
`cd backend`

## Setup Commands

1. Install/sync dependencies:
   `cd backend && uv sync`
2. Ensure `.env` exists under `backend/`.
3. Required env vars used by current scripts:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `OLLAMA_BASE_URL`
4. Optional vars may be referenced in comments (LangSmith/OpenRouter).

## Build, Lint, Test Commands

No formal build pipeline is configured yet.
Use the commands below as the practical operating set.

### Build/Run

- Run chat agent flow:
  `cd backend && uv run python chat.py`
- Run search/similarity query check:
  `cd backend && uv run python search.py`
- Run ingestion/storage script:
  `cd backend && uv run python store.py`

### Lint/Format (Current)

No lint/format tools are configured in `backend/pyproject.toml`.

- Syntax sanity pass:
  `cd backend && uv run python -m compileall .`

If you add linting, prefer first-class `ruff` commands and document them here.

### Test (Current)

No tests currently exist in the repository.

When tests are introduced, prefer `pytest` and use these patterns:

- Run all tests:
  `cd backend && uv run pytest`
- Run one file:
  `cd backend && uv run pytest tests/test_example.py`
- Run one test (single-test command, important):
  `cd backend && uv run pytest tests/test_example.py::test_specific_case`
- Run one unittest method (if unittest is used):
  `cd backend && uv run python -m unittest tests.test_example.TestClass.test_method`

## Code Style Guidelines

Follow these defaults for all new or modified Python code.

### Imports

- Group imports as: standard library, third-party, local modules.
- Keep one blank line between groups.
- Do not use wildcard imports.
- Remove unused imports before finishing.
- Avoid duplicate symbol imports from different packages.

### Formatting

- Follow PEP 8 with 4-space indentation.
- Keep lines readable (target roughly 88-100 chars).
- Use trailing commas in multiline literals/calls when helpful.
- Prefer small focused functions over large monolithic blocks.
- Avoid heavy module-level side effects; use `main()` when adding new scripts.

### Types

- Add type hints to new function parameters and returns.
- Keep type hints explicit for external boundary values.
- Prefer concrete types over `Any` when practical.
- Handle `None` explicitly when using optional values.
- Keep helper signatures stable and predictable.

### Naming

- Use `snake_case` for functions, variables, and modules.
- Use `PascalCase` for classes.
- Use `UPPER_SNAKE_CASE` for true constants.
- Keep environment variable names uppercase with underscores.
- Choose descriptive names over short abbreviations.

### Error Handling

- Fail fast when required configuration is missing.
- Raise clear exceptions with actionable messages.
- Do not silently swallow exceptions.
- Catch specific exception types only when you can recover or enrich context.
- Include enough context around external calls (DB/API/vector store failures).

### Logging and Output

- Prefer structured logging in reusable code.
- Use `print` only for simple script output/diagnostics.
- Never print secrets, keys, or tokens.
- Keep user-facing terminal output concise and actionable.

### Config and Secrets

- Load secrets from environment variables.
- Do not hardcode credentials or endpoints that should be configurable.
- Keep `.env` out of commits.
- Centralize env validation in helper functions when touching related code.

### Testing Expectations For New Code

- Add tests for non-trivial new logic.
- Prefer deterministic unit tests.
- Isolate network/integration tests and make dependencies explicit.
- Ensure at least one documented single-test invocation in PR notes.

### Documentation Expectations

- Update `backend/README.md` when commands/env vars/flows change.
- Use comments to explain intent, not obvious syntax.
- Add short docstrings for non-obvious helpers.

## Agent Workflow Recommendations

- Start by reading `backend/pyproject.toml` and the target script/module.
- Keep edits narrow and aligned with existing patterns.
- Preserve existing behavior unless change is requested.
- If adding tooling (pytest/ruff/mypy), update this file in the same change.
- If command execution fails due to env setup, report missing keys explicitly.

## Known Gaps

- No formal CI commands are defined yet.
- `backend/README.md` is currently empty and should be expanded.
- Current scripts run top-level code on import; refactor carefully when modularizing.

Keep this document current as project tooling matures.
