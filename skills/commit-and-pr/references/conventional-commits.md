# Conventional Commits — quick reference

Format: `<type>(<optional scope>): <description>`

## Types

| Type | Use for |
|------|---------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace — no code-behavior change |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | A performance improvement |
| `test` | Adding or correcting tests |
| `build` | Build system or dependencies |
| `ci` | CI configuration |
| `chore` | Maintenance that doesn't touch src or tests |
| `revert` | Reverts a previous commit |

## Rules

- Description is imperative, lowercase, no trailing period, ideally <= 72 chars.
- Scope is optional and names the area affected, e.g. `feat(auth):`.
- Breaking changes: append `!` after the type/scope (`feat(api)!:`) **and/or**
  add a `BREAKING CHANGE:` footer explaining the break and migration.
- Footers reference issues: `Closes #123`, `Refs #456`.

## Examples

```
feat(parser): support ISO-8601 durations
fix: prevent crash on empty upload
docs(readme): add quick-start section
refactor(db)!: drop deprecated sync API

BREAKING CHANGE: removeUser() is now async and returns a Promise.
Closes #214
```
