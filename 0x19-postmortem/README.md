Apache Server Outage - March 24, 2017

Issue Summary:
Duration: 
March 24, 2017, 07:32:16 to March 24, 2017, 07:45:23 (GMT)
Impact:
 HTTP/1.0 500 Internal Server Error for users accessing the Apache server; 100% of users affected.
Timeline:
Detection: 
07:32:16 - An HTTP/1.0 500 Internal Server Error was detected during a "curl -sI 127.0.0.1" request.
Actions Taken:
Investigated system using tmux and strace concurrently.
Identified a file attempting to open a "phpp" extension.
Located the problematic file using a command in a separate terminal.
Executed a Puppet command to replace "phpp" with "php" in wp-settings.php.
Misleading Paths:
Considered issues related to Apache or PHP configurations initially.
Explored server logs for common errors before narrowing down to the file with "phpp" extension.
Escalation:
No formal escalation; resolved at the individual level.

Root Cause and Resolution:
Root Cause:
The Apache server attempted to process a file with a "phpp" extension, causing a 500 Internal Server Error.
Resolution:
Used Puppet to replace "phpp" with "php" in wp-settings.php.
Puppet Exec Command:

  exec { 'replace phpp to php':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}

Corrective and Preventative Measures:
Improvements/Fixes:
Regularly review server configurations and file extensions to catch potential issues.
Implement more robust monitoring for unexpected file extensions or server errors.
Tasks:
Create a scheduled task to audit server configurations for anomalies.
Enhance monitoring to alert on unexpected file extensions.
Conduct periodic training to enhance troubleshooting skills for server-related issues.
This postmortem outlines the incident on March 24, 2017, where the Apache server experienced a 500 Internal Server Error due to an unexpected file extension. The root cause was identified as an attempt to process a file with a "phpp" extension. The issue was promptly resolved using Puppet to replace "phpp" with "php" in wp-settings.php. Moving forward, proactive measures, including regular configuration reviews and enhanced monitoring, will be implemented to prevent similar incidents.

