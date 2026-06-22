---
name: security-review
description: >-
  Review code or a diff for security vulnerabilities and report them ranked by
  severity with concrete remediations. Use this whenever the user asks to
  "security review", "check for vulnerabilities", "is this secure?", "audit this
  code", review auth/crypto/input-handling, or before shipping anything that
  touches authentication, user input, secrets, file paths, or external requests
  — even if they just ask "is it safe to ship this?"
---

# Security Review

The goal is to find the issues an attacker would, and explain them so they get
fixed correctly. Think in terms of trust boundaries: wherever untrusted input
crosses into trusted execution, data access, or output is where vulnerabilities
live. Prioritize exploitability and impact over theoretical purity.

## What to check

Walk the code with these categories in mind (a practical subset of OWASP):

1. **Injection** — SQL, NoSQL, OS command, LDAP, template, header injection.
   Any place user input is concatenated into a query, command, or markup.
2. **AuthN / AuthZ** — missing or broken authentication; missing authorization
   checks (can user A act on user B's resources?); insecure direct object
   references; privilege escalation.
3. **Secrets & crypto** — hardcoded credentials/keys/tokens, secrets in logs,
   weak or home-grown crypto, predictable randomness for security purposes,
   missing TLS/verification.
4. **Input validation & output encoding** — XSS (stored/reflected), unvalidated
   input crossing a boundary, missing output encoding, mass assignment.
5. **Unsafe operations** — path traversal, unsafe deserialization, SSRF
   (user-controlled URLs fetched server-side), unrestricted file upload, XXE,
   open redirects.
6. **Data exposure** — sensitive data in responses/logs/errors, missing access
   controls on endpoints, verbose error messages leaking internals.
7. **Dependencies & config** — known-vulnerable dependencies, insecure defaults,
   debug mode in prod, permissive CORS.

## Output format

Lead with an overall risk read, then findings by severity. Each finding names
the location, explains the vulnerability and a realistic exploit, rates
severity, and gives a concrete fix.

```
**Overall:** <Critical / High / Medium / Low / Looks clean> — <one line>

### Critical / High
- `path:line` — <vulnerability>. **Exploit:** <how an attacker abuses it>.
  **Severity:** <why this rating>. **Fix:** <specific remediation>.

### Medium
- ...

### Low / hardening
- ...

### Notes
- <what you reviewed, and what was out of scope or couldn't be assessed>
```

## Guardrails

- Rate by real exploitability and impact, not theory. Don't cry wolf — false alarms train people to ignore reviews.
- Give remediations that fix the root cause (parameterized queries, not input blocklists).
- Be explicit about scope and confidence: what you reviewed, what you couldn't see (runtime config, infra), and where you're inferring.
- This is a code review, not a penetration test or a guarantee. Say so — say "no obvious issues in what I reviewed," never "this is secure."
- Do not produce working exploit payloads beyond what's needed to demonstrate the issue to the developer.

## Example

**Overall:** High — one command injection and a missing authorization check.

### Critical / High
- `routes/export.py:54` — `os.system(f"convert {filename} ...")` runs a
  user-supplied filename through a shell. **Exploit:** a filename like
  `x; rm -rf /` executes arbitrary commands. **Severity:** High — remote code
  execution. **Fix:** avoid the shell; pass an argument list to
  `subprocess.run([...], shell=False)` and validate the filename.
