# increasing the open file limit for the user

exec { 'change from 4 to 2048':
  command => "sed -i 's/4/2048/' /etc/security/limits.conf",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  }

exec { 'change from 5 to 2048':
  command => "sed -i 's/5/2048/' /etc/security/limits.conf",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  }
