#using puppet changing config file
file {'~/.ssh/school':
  ensure  => 'file',
  path    => '/etc/ssh/ssh_config',
  content => "
  Host 98.98.98.98
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no",
}