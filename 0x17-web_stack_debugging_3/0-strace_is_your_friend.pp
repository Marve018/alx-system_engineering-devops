# debugging apache 

exec { 'fix_apache_error_config':
        command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
