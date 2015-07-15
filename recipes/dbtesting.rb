if platform?('ubuntu') && node[:platform_version] == '14.04'
    %w(mysql-server).each do |pkg|
        package pkg do
            action :install
        end
    end
end
