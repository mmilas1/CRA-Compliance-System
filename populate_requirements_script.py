from assessment.models import Requirement, Recommendation

# Optional: clear previous entries
Requirement.objects.all().delete()
Recommendation.objects.all().delete()

entries = [
    ("(1) Products with digital elements shall be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity based on the risks;", "A cybersecurity risk analysis should be conducted and monitored during the complete lifecycle of the product. Cybersecurity should be taken into account in every step of the product creation (e.g. secure coding, security by design principles, etc.)"),
    ("(2) Products with digital elements shall be delivered without any known exploitable vulnerabilities;", "A vulnerability assessment should be performed against the digital elements of a product. Known exploitable vulnerabilities shall be fixed before the release of the product."),
    ("(3a) Delivered with a secure by default configuration, including the possibility to reset the product to its original state;", "In case default configurations cover cybersecurity items, they should adopt a reasonable level of security. The default configuration should be placed in a non-erasable memory. A function to reset the product configuration to the default one should be implemented."),
    ("(3b) Ensure protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity or access management systems;", "Implement appropriate authentication and authorization systems. Ensure access to sensitive data and administrative functions is granted only to authenticated and authorized users."),
    ("(3c) Protect the confidentiality of stored, transmitted or otherwise processed data, personal or other, such as by encrypting relevant data at rest or in transit by state of the art mechanisms;", "Use encryption at rest and in transit, ensure secure transmission protocols are used and enabled by default. Apply symmetric or asymmetric encryption schemes."),
    ("(3d) Protect the integrity of stored, transmitted or otherwise processed data, personal or other, commands, programs and configuration against any manipulation or modification not authorised by the user;", "Ensure data integrity using hashing and MACs. Implement secure protocols and self-tests to verify code and firmware integrity."),
    ("(3e) Process only data that are adequate, relevant and limited to what is necessary in relation to the intended use of the product (‘minimisation of data’);", "Follow GDPR best practices. Avoid requesting or retaining unnecessary data. Delete unneeded data promptly."),
    ("(3f) Protect the availability of essential functions, including the resilience against and mitigation of denial of service attacks;", "Harden the system against DDoS attacks using reverse proxies, load balancing, rate limiting, redundancy, and recovery strategies."),
    ("(3g) Minimise their own negative impact on the availability of services provided by other devices or networks;", "Limit outgoing network connections. Implement timeouts and proper exception handling to avoid unnecessary traffic."),
    ("(3h) Be designed, developed and produced to limit attack surfaces, including external interfaces;", "Restrict physical and network interfaces to those needed. Close unnecessary network ports and APIs by default."),
    ("(3i) Be designed, developed and produced to reduce the impact of an incident using appropriate exploitation mitigation mechanisms and techniques;", "Apply defense-in-depth. Encrypt sensitive data, avoid unnecessary data retention, and isolate functionalities."),
    ("(3j) Provide security related information by recording and/or monitoring relevant internal activity, including the access to or modification of data, services or functions;", "Log access and modifications to sensitive functions. Protect logs from tampering and make them accessible to privileged users."),
    ("(3k) Ensure that vulnerabilities can be addressed through security updates, including, where applicable, through automatic updates and the notification of available updates to users;", "Provide timely security updates, implement automatic update checks, and notify users securely."),
    ("(1) Identify and document vulnerabilities and components contained in the product, including a software bill of materials;", "Maintain an SBOM listing all software libraries and components. Ensure it follows standards like SPDX or CycloneDX."),
    ("(2) Address and remediate vulnerabilities without delay, including by providing security updates;", "Classify and fix vulnerabilities promptly. Monitor third-party components and distribute updates quickly."),
    ("(3) Apply effective and regular tests and reviews of the security of the product with digital elements;", "Conduct periodic vulnerability assessments and CI/CD-based testing. Re-evaluate risk assessments after significant changes."),
    ("(4) Publicly disclose information about fixed vulnerabilities after releasing security updates;", "Publish CVEs and notify users after updates are released."),
    ("(5) Put in place and enforce a policy on coordinated vulnerability disclosure;", "Adopt and enforce a Coordinated Vulnerability Disclosure (CVD) policy."),
    ("(6) Take measures to facilitate the sharing of information about vulnerabilities;", "Provide a clear PSIRT contact for vulnerability submissions and notify relevant authorities."),
    ("(7) Provide mechanisms to securely distribute updates;", "Digitally sign updates and publish hash checks. Provide verification instructions."),
    ("(8) Disseminate patches without delay and free of charge, with advisory instructions;", "Notify users of updates through alerts or newsletters, include instructions, and ensure they are free of charge."),
]

for title, advice in entries:
    req = Requirement.objects.create(title=title, description=title, requirement_class="class_1")
    Recommendation.objects.create(requirement=req, advice=advice)

print("✅ Requirements and Recommendations successfully added.")