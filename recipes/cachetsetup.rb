# Installs cachet.
# See https://docs.cachethq.io/v1.0/docs/installing-cachet and
# also http://trevormanternach.com/2015/03/24/installing-cachet/

cookbook_file '/etc/apache2/sites-available/cachet-app.conf' do
  source 'cachet-app.conf'
  owner 'root'
  group 'www-data'
  mode '0640'
  action :create
end

# FIXME git: don't get from a public and source.
# And when that's done we won't need the next few rules.
execute "cacheclone" do
    command <<-EOC
      cd /var/www && \
      /usr/bin/git clone https://github.com/cachethq/Cachet.git && \
      cd Cachet && \
      /bin/chown www-data:www-data /var/www/Cachet/storage/logs
    EOC
    not_if { ::File.directory?('/var/www/Cachet') }
    action :run
end

# Some files in Cachet's git need to be modified.
# FIXME: We're going to overwrite it no doubt will cause problems down
# the line. But better is to address FIXME git above
# See:
# http://laravel.io/forum/06-09-2015-no-supported-encrypter-found-the-cipher-and-or-key-length-are-invalid
cookbook_file '/var/www/Cachet/config/app.php' do
    source 'app.php'
    owner 'root'
    group 'www-data'
    mode '0640'
    action :create
end

# FIXME: Again this disappears when FIXME.git is addressed
cookbook_file '/var/www/Cachet/.env' do
    source '.app-env'
    # Lock this down somewhat...
    owner 'root'
    group 'www-data'
    mode '0440'
    action :create
end

# Composer is installed in a prior recipe.
# FIXME: is there a way to note the dependency?
execute "Cachet dependencies and artisan framework setup" do
    command <<-EOC
      cd /var/www/Cachet && \
      /usr/local/bin/composer install --no-dev -o && \
      /usr/bin/php artisan migrate
    EOC
    # not_if { ...  } ?
    action :run
end

execute "enable apache cachet" do
    command <<-EOC
      /usr/bin/a2ensite cachet-app && \
      /usr/sbin/service apache2 restart
    EOC
    not_if { ::File.exist?('/etc/apache2/sites-enabled/cachet-app.conf')  }
    action :run
end
