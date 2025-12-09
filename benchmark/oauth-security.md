## OAuth Security

This section defines controls related to OAuth-enabled Connected Apps, third-party integrations, and external access to Salesforce environments. These controls ensure that organizations maintain visibility, governance, and lifecycle management over external systems that authenticate to Salesforce via OAuth, reducing the risk of unauthorized access, data exfiltration, and stale integration pathways.

### SBS-OAUTH-001: Inventory and Criticality Classification of OAuth-Enabled Connected Apps

**Control Statement:** All OAuth-enabled Connected Apps must be recorded in an authoritative system of record and assigned a documented vendor criticality rating reflecting integration importance and data sensitivity.

**Description:**  
Organizations must maintain a complete, authoritative inventory of all OAuth-enabled Connected Apps and assign each an explicit vendor criticality rating based on operational importance and the sensitivity of accessible Salesforce data.

**Rationale:**  
Without a complete inventory and criticality classification, organizations cannot adequately assess the risk posed by third-party integrations, prioritize security controls, or meet governance requirements for external system connectivity.

**Audit Procedure:**  
1. Retrieve a list of all Connected Apps with active OAuth configurations from Salesforce Setup.  
2. Retrieve the organization's authoritative system of record for integration and vendor management.  
3. Compare the Salesforce Connected App list to the system of record and confirm every OAuth-enabled Connected App appears in the inventory.  
4. Verify each listed Connected App has an assigned vendor criticality rating documented in the system of record.  
5. Flag any apps missing from the inventory or lacking a documented criticality rating as noncompliant.

**Remediation:**  
1. Add any missing OAuth-enabled Connected Apps to the system of record.  
2. Document and assign a vendor criticality rating to each Connected App based on operational importance and data sensitivity.  
3. Implement a recurring process to synchronize Connected App changes with the system of record.

**Default Value:**  
Salesforce does not automatically maintain or enforce an external inventory or criticality classification for Connected Apps.

**References:**  
- Salesforce Help: Connected Apps and OAuth  
- NIST SP 800-53: SA-9 External Information System Services  
- CIS Controls v8: Control 15 – Service Provider Management

### SBS-OAUTH-002: Due Diligence Documentation for High-Risk Connected App Vendors

**Control Statement:** Organizations must review and retain available security documentation for all high-risk Connected App vendors and explicitly record any missing documentation as part of the vendor assessment.

**Description:**  
For each Connected App vendor classified as high-risk, the organization must collect, review, and store relevant security documentation—including terms of use, privacy policy, trust center or security overview, and any published information security guidelines—and must explicitly document when a required artifact does not exist.

**Rationale:**  
High-risk vendors introduce elevated exposure to sensitive data and business processes, and maintaining documented due diligence ensures that risks are understood, assessed, and traceable within the vendor management process.

**Audit Procedure:**  
1. Retrieve the list of Connected App vendors classified as high-risk from the organization’s system of record.  
2. For each high-risk vendor, verify that the following documents, where available, are stored in the designated repository:  
   - Terms of use  
   - Privacy policy  
   - Trust center or security overview  
   - Published information security guidelines  
3. Confirm that any missing documentation is explicitly recorded as unavailable in the vendor assessment.  
4. Flag any high-risk vendor lacking required documentation or missing explicit acknowledgment of unavailable documents as noncompliant.

**Remediation:**  
1. Collect and store all required documentation for each high-risk vendor.  
2. Where documentation does not exist, record this absence in the vendor assessment.  
3. Update the vendor management process to ensure ongoing due diligence for high-risk vendors.

**Default Value:**  
Salesforce does not manage or enforce vendor due diligence requirements for Connected App providers.

**References:**  
- NIST SP 800-53: SA-12 Supply Chain Protection  
- CIS Controls v8: Control 15 – Service Provider Management  
- OWASP ASVS: Section 1.5 Vendor Security Documentation
