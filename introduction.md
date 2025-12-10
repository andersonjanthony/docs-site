# 1. Introduction

This section defines the purpose, scope, definitions, and control structure for the Security Benchmark for Salesforce (SBS).

## 1.1 Purpose

SBS provides a **consistent and measurable compliance standard** for Salesforce security posture. The benchmark exists to:

- Establish mandatory security requirements that organizations must meet to be considered compliant  
- Enable organizations to definitively answer: **"Is my Salesforce org secure?"**  
- Provide auditors and consultants a formal benchmark for structured compliance evaluations  
- Establish a foundation for security tools to measure, scan, and report compliance automatically  

**Important:** SBS is not a Salesforce product, is not endorsed by Salesforce, Inc., and does not represent an official Salesforce standard. It is created and maintained independently by practitioners.

## 1.2 Value of Compliance

SBS compliance requires a combination of automated scanning, organizational practices, and documentation requirements. It is not satisfied through automated tools alone, but through establishing governance processes, maintaining system-of-record inventories, and implementing continuous monitoring.

**The core value:** When a security breach affects your Salesforce environment, SBS compliance means you know exactly where to look. Every control is mapped, documented, and traceable—enabling rapid assessment of what was compromised, what was protected, and where gaps exist.

This foundation delivers:

- **Complete visibility** — Know who has access to what, why they have it, and how it's governed across permissions, integrations, and third-party connections.

- **Effective incident response** — Quickly determine which controls were at risk, what protections limited damage, and where to focus remediation efforts.

- **Governance and accountability** — Maintain auditable trails for justifications, exceptions, and security decisions that support compliance and regulatory requirements.

- **Baseline for risk management** — Measure security posture over time, detect configuration drift, and maintain assurance that critical controls remain enforced.

## 1.3 Control Format and Interpretation

Each SBS control is written in a **prescriptive, binary format** designed to determine compliance. Controls include the following components:

- **Control ID** — A unique identifier for reference (e.g., SBS-AG-003).  
- **Description** — A clear requirement that must be met for compliance.  
- **Rationale** — The security justification for the control.  
- **Audit Procedure** — Steps to evaluate whether the requirement is met.  
- **Remediation** — Actions needed to bring the environment into compliance.  
- **Default Value** — Salesforce’s default behavior relevant to this control.  
- **References** — External standards or Salesforce documentation supporting the requirement.

**Interpretation:**  
- If a control’s requirement is not satisfied, the environment is **noncompliant** with SBS.  
- Partial compliance is not recognized.  
- Organizations may choose to implement compensating controls, but these do not replace formal compliance unless explicitly documented and accepted by their internal security authority.

This format ensures that SBS remains consistent, measurable, and suitable for auditing, consulting, and automated scanning tools.
