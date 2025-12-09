## Code Security

This section defines controls related to secure development practices for Salesforce code, including Apex, Lightning Web Components, and other programmatic assets. These controls ensure that organizations implement quality gates, peer review, and automated security testing within their development lifecycle to prevent vulnerable or flawed code from entering production environments.

### SBS-CODE-001: Mandatory Peer Review for Salesforce Code Changes

**Control Statement:** All Salesforce code changes must undergo peer review and receive approval before merging into any production-bound branch.

**Description:**  
Organizations must configure their source control system to require at least one peer reviewer to approve all changes to Apex, Lightning Web Components, and other programmatic assets before those changes are merged into branches used for production deployments.

**Rationale:**  
Mandatory peer review prevents insecure or flawed code from entering the deployment pipeline and ensures shared oversight of changes to sensitive business logic.

**Audit Procedure:**  
1. Inspect source control settings to confirm merge rules require peer review on production-bound branches.  
2. Review merge history or representative pull requests to verify peer approvals were recorded.  
3. Flag any repositories or branches that allow merging without peer approval.

**Remediation:**  
1. Update branch protection rules to require peer review before merge.  
2. Train developers on the peer review workflow.  
3. Block direct commits to production-bound branches.

**Default Value:**  
Salesforce does not enforce code review requirements; these controls depend on the organization's source control configuration.

**References:**  
- OWASP Code Review Guide  
- NIST SP 800-53: SA-11 Developer Testing and Evaluation

### SBS-CODE-002: Pre-Merge Static Code Analysis for Apex and LWC

**Control Statement:** Static code analysis with security checks for Apex and Lightning Web Components must execute successfully before any code change is merged into a production-bound branch.

**Description:**  
Organizations must implement static application security testing (SAST) in their CI/CD pipeline and configure it to run prior to merge, enforcing security rulesets that detect vulnerabilities specific to Apex and LWC.

**Rationale:**  
Requiring static analysis before merge ensures that security issues are identified early and prevents vulnerable code from entering the release pipeline.

**Audit Procedure:**  
1. Inspect CI/CD pipeline configuration to confirm a static code analysis step runs before merges.  
2. Verify the SAST tool includes security rulesets for Apex and Lightning Web Components.  
3. Review pipeline logs from representative merges to ensure scans executed and passed.  
4. Flag pipelines or branches missing enforced pre-merge scanning.

**Remediation:**  
1. Integrate static code analysis into the CI/CD pipeline for all production-bound branches.  
2. Enable Apex and LWC security rulesets within the scanning tool.  
3. Configure pipelines to block merges when static analysis fails.

**Default Value:**  
Salesforce does not provide or enforce static code analysis; organizations must implement external SAST tooling.

**References:**  
- OWASP ASVS: Section 1.11 Secure Development Practices  
- NIST SP 800-53: SA-11 Developer Testing and Evaluation  
- Salesforce Developer Guide: Apex Security Best Practices
