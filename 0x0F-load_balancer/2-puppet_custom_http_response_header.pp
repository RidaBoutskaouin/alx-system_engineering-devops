
exec { 'update server':
	command => 'apt-get update',
	user => 'root',
	provider => 'shell',
}
->
package { 'nginx':
	ensure => present,
	require => 'apt',
}

file { 'Add HTTP HEADER':
	ensure => present,
	path => '/etc/nginx/sites-available/default',
	after => 'listen 80 default_server;',
	line => 'add_header X-Served-By $hostname;',
}
->
# start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
