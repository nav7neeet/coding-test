# Infrastructure as Code
<h3>What is it?</h3>

IaC is a method for defining, provisioning, and managing infrastructure using code instead of manually using the UI and click operations. For example, for creating an EC2 instance, we can specify all the required resources in a configuration file and deploy them using a single command or a CI/CD pipeline. Some popular IaC tools include [HashiCorp Terraform](https://www.terraform.io/), [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/), and [Pulumi](https://www.pulumi.com/)
<div>
  <img src="https://www.datocms-assets.com/2885/1620155116-brandhcterraformverticalcolor.svg" width="100" float="left">
  
  <img src="https://seeklogo.com/images/A/aws-cloudformation-logo-11F173F931-seeklogo.com.png" width="100" float="left">
  
  <img src="https://www.pulumi.com/logos/brand/avatar-on-white.svg" width="125" float="right">
</div>

<h3> Why would I want it? </h3>

- Security: IaC undergoes scanning for security vulnerabilities using SAST tools to prevent the provisioning of insecure and non-compliant resources.

- Consistency and Reusability: IaC ensures the creation of consistent infrastructure across various environments such as Dev, Test, and Production, minimizing the chances of inconsistencies.

- Speed: IaC significantly reduces the time required for provisioning and deprovisioning infrastructure. This proves invaluable in disaster recovery scenarios, where rapid infrastructure creation is crucial for recovery.

- Version Control: IaC files can be stored in version control systems like Git, making it easy to track the history of infrastructure changes, identify who made the changes, and understand when the changes were made.


<h3>Are there any alternatives?</h3>
IaC tools provide high-level, declarative language or configuration format that allows users to describe the desired state of their infrastructure. It abstracts the complexity of making API calls by encapsulating the necessary interactions with the underlying cloud provider's API. <br>

So to acheive the same objective without IaC tools, we can directly use the API provided by the service to create and manage the infrastructure.

[AWS EC2 API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)

# Observability
In the context of microservices, observability means the ability to monitor and gain insights into the behavior and performance of a distributed system. It involves collecting and analyzing data from various components of the microservices architecture to ensure that the system is running smoothly, and that issues can be quickly identified and resolved. Key components of observability include monitoring, logging, tracing, and alerting.

<h3>What do we want to observe?</h3>

- Latency: Time taken by requests to traverse the entire microservices ecosystem.
- Throughput: Volume of requests and responses.
- Error Rates: Occurrence of errors and exceptions across microservices.
- Availability: Uptime and availability of individual microservices.
- CPU Usage, Memory, Disk I/O: Resource consumption to identify potential bottlenecks or inefficiencies.

<h3>What kind of challenges do you see in a distributed environment?</h3>

- Increased Complexity: Microservices introduce complexity due to their distributed nature. Observing interactions across a number of different services can be very challenging.

- Dynamically Changing Architecture: Microservices can scale independently, and new services may be added or removed dynamically. Observability solutions must adapt to these changes.

<h3>How can we solve them?</h3>

- Design and build microservices by embedding monitoring and logging code within the application to gather relevant data.
- Use centralized logging solutions to aggregate logs from various microservices. This aids in troubleshooting and debugging.
- Utilize observability tools and platforms such as [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), [ELK stack](https://www.elastic.co/elastic-stack) and others that are specifically designed for monitoring and analyzing distributed systems.
- Foster a culture of observability within the organization, encouraging collaboration between development and operations teams to build and maintain observable systems.

<div>
  <img src="https://static-00.iconduck.com/assets.00/file-type-prometheus-icon-360x512-uvrmbt7e.png" width="70" float="right">
  
  <img src="https://static-00.iconduck.com/assets.00/grafana-icon-512x512-0v0st1xm.png" width="100" float="right">
  
</div>

# Security

<h3>What are the first three things that you check, to limit the risk of a breach? Explain why. </h3>

A security breach happens when a threat actor gains unauthorized access to our system/services/infrastructure/environment. The top 3 things that I will check to limit the risk of a breach in AWS are - 

- [Cross-Account Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html#access_policies-cross-account-using-resource-based-policies): Several AWS services allow external entities to be granted access across accounts. It could be as straightforward as setting up an IAM role with admin privileges and providing access to an external AWS account. This essentially gives temporary credentials to a potential threat actor, allowing them access to the AWS account. Consider the implications if this occurs in a production account with sensitive data. It's crucial to regularly audit and ensure there are no unmonitored external entities with access to AWS accounts.

- [Multi-Factor Authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication): MFA is crucial for security because it adds an additional layer of protection beyond passwords. By requiring users to provide multiple forms of identification, such as a password and a temporary code from a mobile device, MFA significantly reduces the risk of unauthorized access. It serves as a powerful deterrent against various cyber threats, including password breaches, phishing attacks, and unauthorized account access.

  According to this [Microsoft blog](https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/) 99.9 percent of attacks on your accounts can be prevented by using MFA.

- [Publicly Exposed Resources & Hardcoded Secrets](https://github.com/SummitRoute/aws_exposable_resources): Publicly Exposed Resources: Numerous AWS resources, such as S3 buckets and EBS volumes, can be inadvertently exposed to the public. It is essential to verify whether resources are accessible on the open internet without a valid business justification. This exposure may result from misconfigurations or oversights by users, and it is a common area where mistakes can occur.

  It is a very common practise to use hardcoded passwords or API keys, directly within the source code of a program or application. This practice poses a significant security risk as it makes it easier for unauthorized individuals to discover and exploit these credentials.

  [Samsung secrets in public GitLab repositories](https://techcrunch.com/2019/05/08/samsung-source-code-leak/)

  [Uber’s private GitHub repositories with AWS tokens](https://www.ftc.gov/system/files/documents/federal_register_notices/2018/04/152_3054_uber_revised_consent_analysis_pub_frn.pdf)
