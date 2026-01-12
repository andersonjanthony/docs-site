## Integrations

This section defines controls related to outbound connectivity from Salesforce to external systems, including Remote Site Settings and Named Credentials. These controls ensure that organizations maintain visibility and governance over approved external endpoints, authentication mechanisms, and data flows initiated by Salesforce, reducing the risk of unauthorized data transmission, dependency on untrusted services, and configuration drift in integration pathways.

### SBS-INT-001: Enforce Governance of Browser Extensions Accessing Salesforce

**Control Statement:** Organizations must enforce a centrally managed mechanism that restricts which browser extensions are permitted to access Salesforce, and must not allow the use of unmanaged or uncontrolled extensions.

**Description:**  
Organizations must deploy a centrally managed governance mechanism—such as Chrome Browser Cloud Management, MDM policies, or configuration profiles—that enforces an allow-list or blocklist for browser extensions accessing Salesforce domains.

**Rationale:**  
Browser extensions can harvest session tokens, exfiltrate data, and execute unauthorized operations within authenticated Salesforce sessions. Without centralized governance, malicious or cloned extensions—increasingly common with AI-generated code—create an uncontrolled risk surface that Salesforce cannot detect or prevent natively.

**Audit Procedure:**
1. Request evidence of a browser-extension governance mechanism applied to user devices (e.g., Chrome Browser Cloud Management, Intune configuration profile, Jamf configuration profile, Active Directory GPO, or equivalent).
2. Require a screenshot, exported policy file, or screen capture demonstrating that extension controls are active and enforceable (e.g., an allow-list or blocklist configuration for Chrome extensions).
3. Verify that the mechanism explicitly restricts installation or execution of unapproved extensions that can access Salesforce domains.
4. Flag the organization as noncompliant if no enforceable governance mechanism exists or if extension governance is based solely on policy, awareness, or voluntary user behavior.
5. Download API Total Usage logs (EventLogFile - ApiTotalUsage, available in free tier of Event Monitoring) and analyze for indicators of unauthorized browser extension activity:
   - Review `USER_AGENT` field for patterns indicating browser extensions (e.g., extension identifiers, non-standard user agents).
   - Identify API call patterns characteristic of auto-refresh extensions (e.g., Inspector Reloader) such as regular-interval repeated requests.
   - Flag any anomalous patterns for investigation against approved extension inventory.

**Remediation:**  
1. Implement a centrally managed browser or device management solution capable of enforcing extension restrictions (e.g., Chrome Browser Cloud Management, Intune, Jamf, or GPO-based controls).  
2. Define and apply an allow-list or blocklist policy governing which extensions are permitted to interact with Salesforce.  
3. Remove or disable any unapproved browser extensions from managed devices.  
4. Apply enforcement policies to all corporate-managed devices accessing Salesforce.

**Default Value:**  
Salesforce provides no mechanism to prevent or detect browser extension usage; unmanaged browser extensions are permitted by default, including those capable of accessing Salesforce data and authenticated sessions.

### SBS-INT-002: Inventory and Justification of Remote Site Settings

**Control Statement:** Organizations must maintain an authoritative inventory of all Remote Site Settings and document a business justification for each endpoint approved for Apex HTTP callouts.

**Description:**  
All Remote Site Settings configured in Salesforce must be recorded in the organization’s system of record along with a clear business justification demonstrating why the endpoint is required and trusted for use in Apex HTTP callouts.

**Rationale:**  
Remote Site Settings authorize outbound communication from Salesforce to external endpoints; without documented justification, unvetted or insecure endpoints may expose the organization to data leakage, dependency risks, or communication with untrusted services.

**Audit Procedure:**  
1. Enumerate all Remote Site Settings via Salesforce Setup or the Metadata API.  
2. Retrieve the organization’s system of record for approved outbound endpoints.  
3. Compare the Salesforce list to the system of record to confirm each Remote Site Setting is documented.  
4. Verify that each documented Remote Site Setting includes a clear business justification.  
5. Flag any Remote Site Settings missing from the inventory or lacking justification as noncompliant.

**Remediation:**  
1. Add all undocumented Remote Site Settings to the system of record.  
2. Document a valid business justification for each endpoint.  
3. Remove or disable any Remote Site Settings that cannot be justified.  
4. Implement a recurring process to reconcile Remote Site Settings with the system of record.

**Default Value:**  
Salesforce does not require or maintain business justification for Remote Site Settings and does not enforce an external inventory.

### SBS-INT-003: Inventory and Justification of Named Credentials

**Control Statement:** Organizations must maintain an authoritative inventory of all Named Credentials and document a business justification for each external endpoint and authentication configuration approved for use in Salesforce.

**Description:**  
All Named Credentials defined in Salesforce—regardless of authentication type or use case—must be recorded in the organization’s system of record, including the endpoint URL, authentication model, and a clear business justification demonstrating why the connection is required and trusted for Apex callouts, External Services, or external data access.

**Rationale:**  
Named Credentials control authenticated outbound communication from Salesforce to external systems; undocumented or unjustified configurations may expose the organization to data leakage, unauthorized integrations, or reliance on insecure or untrusted endpoints.

**Audit Procedure:**  
1. Enumerate all Named Credentials using Salesforce Setup, Metadata API, Tooling API, or Connect REST API.  
2. Retrieve the organization’s system of record for approved external endpoints and integration credentials.  
3. Compare the Salesforce list to the system of record to confirm all Named Credentials are documented.  
4. Verify that each documented Named Credential includes:  
   - The external endpoint URL  
   - The authentication type (named principal or per-user)  
   - The business justification for the integration  
5. Flag any Named Credentials missing from the inventory or lacking justification as noncompliant.

**Remediation:**  
1. Add any undocumented Named Credentials to the system of record.  
2. Document a valid business justification for each Named Credential.  
3. Remove, disable, or reconfigure any Named Credentials that cannot be justified or that reference untrusted endpoints.  
4. Establish a recurring reconciliation process to ensure Named Credentials remain fully inventoried and justified.

**Default Value:**  
Salesforce does not maintain or enforce an external inventory or business justification for Named Credentials.

### SBS-INT-004: Retain API Total Usage Event Logs for 30 Days

**Control Statement:**
The organization must retain API Total Usage event log data (EventLogFile EventType=ApiTotalUsage) for at least the immediately preceding 30 days using Salesforce-native retention or automated external export and storage.

**Description**:
If the organization’s Salesforce does not provide at least 30 days of ApiTotalUsage EventLogFile availability in Salesforce, the organization must automatically export newly available ApiTotalUsage event log files at least once every 24 hours to an external log store that retains a minimum of 30 days of data.

**Rationale**:
API Total Usage logs provide visibility into REST, SOAP, and Bulk API activity and key attributes (for example, user, connected app, client IP, resource, and status code), which supports incident detection, investigation, and integration governance.

**Audit Procedure**:
1. Determine whether the organization relies on Salesforce-native retention (Event Monitoring/Shield/Event Monitoring add-on) or an external log store as the system of record for ApiTotalUsage EventLogFile data.
2. If the organization relies on Salesforce-native retention, verify that EventLogFile data is retained for at least 30 days (for example, confirm the org is entitled to and configured for Event Log File retention that is at least 30 days and can retrieve ApiTotalUsage EventLogFile data within the preceding 30-day window).
3. If the organization relies on an external log store (including all orgs with only 1-day ApiTotalUsage availability in Salesforce):
- Verify an automated process exists that retrieves EventLogFile entries where EventType='ApiTotalUsage' and downloads the associated log files at least once every 24 hours.
- Inspect job schedules/run history and confirm successful executions covering at least the last 30 days (no missed days).
- From the external log store, retrieve ApiTotalUsage logs for (a) the oldest day in the preceding 30-day window and (b) the most recent day, and confirm both are accessible and attributable to the organization.
- Verify access to the external log store is restricted to authorized roles and service identities responsible for monitoring and investigations.

**Remediation**:
1. If the organization has only 1-day ApiTotalUsage EventLogFile availability in Salesforce, implement an automated daily export that downloads newly available ApiTotalUsage log files and stores them externally for at least 30 days.
2. If the organization uses Salesforce-native retention, ensure the configured retention period for Event Log Files is not less than 30 days.
3. Restrict access to the retained logs (Salesforce-native or external) to authorized personnel and designated service identities.

**Default Value**:
Enterprise, Unlimited, and Performance Edition organizations have free access to the ApiTotalUsage event type with 1-day data retention, while organizations with Shield/Event Monitoring add-on retain Event Log Files for 30 days by default (and may be eligible to extend retention).

### SBS-INT-005: Provide UI-Based Monitoring and Anomaly Detection for API Total Usage Logs

**Control Statement:**
The organization must ingest API Total Usage (EventLogFile EventType=ApiTotalUsage) logs into a UI that enables anomaly detection through visualization and alerting over at least the preceding 30 days.

**Description**:
The organization must transform ApiTotalUsage event log files from their default CSV form into a queryable monitoring UI (Salesforce-native or SIEM) that refreshes at least daily and supports anomaly alerting.

**Rationale**:
ApiTotalUsage logs contain per-request details (for example, user, connected app, client IP, API family/resource, and status code) that are necessary to detect suspicious integrations, compromised credentials, abusive clients, and unexpected API surges.

**Audit Procedure**:
1. Identify the system used to monitor ApiTotalUsage logs (Salesforce-native analytics/dashboard or a corporate SIEM).
2. Verify the monitoring system ingests ApiTotalUsage data and presents it in a UI (not raw CSV files) with interactive filtering and drill-down.
3. Verify the UI provides, at minimum, the following views covering at least the preceding 30 days:
- Time-series visualization of total API request volume
- Breakdown/top-N views by CONNECTED_APP_ID or CONNECTED_APP_NAME, USER_ID or USER_NAME, CLIENT_IP, API_FAMILY, and STATUS_CODE
5. Verify the monitoring system is refreshed at least daily (for example, evidence of scheduled ingestion job runs and the latest ingested data timestamp).
6. Verify at least one enabled alerting mechanism exists for anomalous API usage (for example, threshold-based alerts for spikes in volume, increases in failed status codes, or new/rare calling clients), and review evidence that alerts would be delivered to an operational channel (email, ticketing, chat, or SIEM alert queue).
7. If the org has only 24-hour visibility in Salesforce for the daily API Total Usage event log files, verify the UI is backed by an external store/ingestion process rather than relying on in-org browsing/downloading alone.

**Remediation**:
1. Implement ingestion of ApiTotalUsage EventLogFile data into a monitoring platform (external SIEM or Salesforce-native) and parse the CSV fields into structured records.
2. Create dashboards/views that visualize API usage trends and allow drill-down by connected app, user, client IP, API family, and status code.
3. Configure and enable alerting rules to detect anomalous API usage patterns and route alerts to an operational response workflow.
4. Ensure the monitoring UI is refreshed at least daily and covers at least 30 days of searchable history.

**Default Value**:
By default, API Total Usage data is delivered as downloadable event log files (CSV), and all orgs can view only the daily API Total Usage event log files for the previous 24 hours without Event Monitoring, which is insufficient for sustained daily monitoring without an external monitoring/analytics layer.