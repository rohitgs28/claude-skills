# Scaffolding checklist by stack

Read the section that matches the project. These are baselines, not mandates —
add what's missing, skip what doesn't apply.

## Every repo

- `README.md` — what it does, install, run, results/usage
- `LICENSE` — only if the author wants one (MIT and Apache-2.0 are common defaults)
- `.gitignore` — language-appropriate
- At least one meaningful test
- Remove committed secrets, build artifacts, and large binaries

## Python

- `requirements.txt` or `pyproject.toml` with pinned-ish versions
- `.gitignore`: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `.env`, `*.egg-info/`
- Tests via `pytest`; a `tests/` directory
- Optional CI: GitHub Actions running `pip install -r requirements.txt && pytest`
- Replace Python 2 idioms (`print` statements, `raw_input`, `xrange`), fix mixed tabs/spaces

## Node / TypeScript

- `package.json` with `scripts` (`build`, `test`, `lint`) and a lockfile committed
- `.gitignore`: `node_modules/`, `dist/`, `.env`, coverage output
- `tsconfig.json` for TS projects
- Tests via the project's runner (jest/vitest/node:test)

## Go

- `go.mod` / `go.sum`
- `.gitignore`: built binaries, `vendor/` if not committed
- Tests as `*_test.go`; CI running `go test ./...` and `go vet ./...`

## Rust

- `Cargo.toml` / `Cargo.lock`
- `.gitignore`: `/target`
- Tests via `cargo test`; CI running `cargo test`, `cargo clippy`, `cargo fmt --check`

## Minimal GitHub Actions CI (adapt per stack)

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # add language setup + install + test for the project's stack
```
