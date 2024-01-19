# installs the package puppet-lint
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],  # Ensure Werkzeug is installed first
}

# Address potential pip vulnerability (highly recommended):
exec { 'upgrade_pip':
  command => 'pip3 install --upgrade pip',
  unless  => 'pip3 --version | grep -q ">=21.3"',  # Check for a more recent version
  before  => Package['Werkzeug'],  # Upgrade pip before installing Werkzeug
}
