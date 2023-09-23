#using puppet changing config file
file {'~/.ssh/school':
  ensure  => 'file',
  content => "
  Host 98.98.98.98
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no",
}