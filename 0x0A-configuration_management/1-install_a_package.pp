# installs the package puppet-lint
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Address potential pip vulnerability (highly recommended):
exec { 'upgrade_pip':
  command => 'pip3 install --upgrade pip',
  unless  => 'pip3 --version | grep -q ">=21.3"',  # Check for a more recent version
  before  => Package['Flask'],
}
