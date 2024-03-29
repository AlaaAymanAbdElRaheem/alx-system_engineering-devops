#custom HTTP header with Puppet

exec { 'update packages':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update packages'],
}

exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx'],
}

exec {'set X-Served-By header':
  command => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By \$hostname;' /etc/nginx/sites-available/default",
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}