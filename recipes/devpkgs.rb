if platform?('ubuntu') && node[:platform_version] == '14.04'
    %w(emacs24 bashdb).each do |pkg|
        package pkg do
            action :install
        end
    end
end
