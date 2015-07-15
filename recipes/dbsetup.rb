# Create cachet table and grant access to that, if it's not there
# already
execute "mysql-create-table" do
    db_cmd="CREATE DATABASE cachet;
GRANT ALL PRIVILEGES on cachet.* TO
\"cachet\"@\"%\"
IDENTIFIED BY \"abc123\";"
    command "/usr/bin/mysql -u root -psecret -e'#{db_cmd}'"
    not_if "/usr/bin/mysql -u root -psecret cachet -e'SHOW TABLES' | grep incident_templates"
    action :run
end
