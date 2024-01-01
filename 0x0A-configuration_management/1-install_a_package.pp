# this puppet manifest install flask from pip3.

package { 'python3-pip':
  ensure => present,
}

package { 'Flask':
  ensure   => '2.1.0',  
  provider => 'pip3',
  require  => Package['python3-pip'],
}