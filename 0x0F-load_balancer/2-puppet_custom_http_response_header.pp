# Install Nginx
class { 'nginx':
  manage_repo => true,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  content => "# Managed by Puppet\nserver {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\troot /var/www/html;\n\tindex index.html index.htm;\n\n\tserver_name _;\n\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\n\t# Custom HTTP Header\n\tadd_header X-Served-By \$hostname;\n}\n",
  notify  => Service['nginx'],
}

# Enable Nginx default site
link { '/etc/nginx/sites-enabled/000-default':
  to      => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
