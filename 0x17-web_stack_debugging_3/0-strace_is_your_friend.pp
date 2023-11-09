#replacing "phpp" to "php" in wp-settings.php

exec { 'replace phpp to php':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}