if platform?('ubuntu') && node[:platform_version] == '14.04'
    %w(curl php5).each do |pkg|
        package pkg do
            action :install
        end
    end
end
