# 🔐 Security Policy

BlackVault is built for security-first communications. If you discover a vulnerability, we **urgently** request that you follow the responsible disclosure guidelines outlined below.

---

## 📫 Contact

To report a security issue privately and responsibly:

- GitHub: Open a security advisory (NOT a public issue)

I will acknowledge your report within **72 hours** and aim to provide a resolution timeline within **5 business days**.

---

## 🚨 Severity Levels

| Level     | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| CRITICAL  | Unauthorized remote access, session hijack, encryption bypass              |
| HIGH      | Local privilege escalation, logic error in trap triggers                   |
| MEDIUM    | Denial of service, obfuscation bypass, kill switch anomalies               |
| LOW       | Minor input validation gaps, informational leakage (non-critical)          |

---

## 🧪 Scope of Testing

You are authorized to test:

- Your own account(s)
- Your locally deployed BlackVault builds
- Public API endpoints provided by the maintainers (TBA)

You are NOT authorized to:

- Attempt denial-of-service against hosted services  
- Attack other users without explicit consent  
- Use third-party testing platforms without permission  

---

## 🧰 Preferred Report Format

Please include:

- Vulnerability summary  
- Affected modules and functions (e.g., `/core/handshake_engine/init_key`)  
- Steps to reproduce  
- Proof-of-concept code, if applicable  
- Suggested fixes (if known)

---

## 🛡️ Coordinated Disclosure

We believe in **transparency, not panic**. When a valid issue is confirmed:

1. Triage and confirm severity.
2. Patch will be developed and tested.
3. Security advisory and changelog will be published.
4. Credit will be given if the reporter consents.

---

## ❌ Out of Scope

We will NOT consider the following as valid issues:

- "Self-XSS" (requires user to attack themselves)  
- Reports without reproducible proof  
- Tools or payloads not relevant to BlackVault’s architecture

---

## ❤️ Thanks

BlackVault exists to protect the vulnerable. By reporting vulnerabilities, you are actively defending lives, freedoms, and rights.
