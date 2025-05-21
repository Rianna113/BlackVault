# 🤝 Contributing to BlackVault

Thank you for your interest in strengthening global security. BlackVault is a defense-first encrypted communications framework. It requires high-integrity contributions — technically and ethically.

---

## 🔑 Guiding Values

- **Security > Speed**  
- **Clarity > Cleverness**  
- **Transparency > Hype**  

This is not a hype project. It's a protective shield for people who need it.

---

## 🧰 How to Contribute

1. **Fork the repo** and clone your fork.
2. Create a branch for your feature or fix: git checkout -b feature/<your-feature-name>

3. Make changes locally. Ensure tests pass: ./run_tests.sh

4. Commit using conventional commits: feat: add session timeout handler
fix: resolve nonce validation bug

5. Push your branch and open a Pull Request.

---

## ✅ PR Requirements

Before your PR will be reviewed, make sure:

- It includes **comments** where logic may not be obvious.
- Tests are updated or added for new functionality.
- It does not weaken security posture without discussion.

---

## 🔐 Security-Impacting Changes

If your PR involves any of the following, tag it with `SECURITY OVERRIDE REQUIRED` in the PR title:

- Key exchange logic
- Signature validation
- Trap, kill, or fail-safe systems
- Defense heuristics

These will require review by the Lead Maintainer.

---

## 🧪 Test Coverage

All new features must be accompanied by:

- Unit tests for core logic
- Fuzz/abuse tests for edge cases (if applicable)
- Optional: performance benchmarks

We use `pytest` and `hypothesis` (property-based testing) where possible.

---

## 💬 Communication

- Bug reports: [GitHub Issues](https://github.com/BryceWDesign/BlackVault/issues)
- Feature discussions: Start a thread in Discussions
- Urgent security concerns: DM or email the Lead Maintainer (PGP key coming soon)

---

## ⚠️ Ethics Clause

By contributing, you agree your work will **not be used for mass surveillance, commercial spyware, or authoritarian misuse**.  
Violation of this clause = permanent ban from contribution and repo access.

---

## 🙏 Thank You

You’re not just writing code. You’re helping build armor for people who don’t have it yet.


