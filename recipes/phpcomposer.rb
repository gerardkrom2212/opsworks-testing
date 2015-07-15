# Install PHP composer if that is not there.
execute "phpcomposer" do
    command <<-EOC
    (/usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php) && \
        /bin/mv -v composer.phar /usr/local/bin/composer
    EOC
    not_if { ::File.executable?('/usr/local/bin/composer') }
    action :run
end
