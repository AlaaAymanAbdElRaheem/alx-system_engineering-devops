#Install Nginx web server (w/ Puppet)

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

exec {'redirection':
  command => "sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default;",
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}
