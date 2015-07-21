if platform?('ubuntu') && node[:platform_version] == '14.04'
    # Good packages
    %w(emacs24 bashdb remake python-pip
       python3-pip git.el python-pip).each do |pkg|
        package pkg do
            action :install
        end
    end

    # Good stuff in /usr/local/bin
    %w(sl xtermtitle).each do |script|
        cookbook_file "/usr/local/bin/#{script}" do
            source script
            owner 'root'
            group 'root'
            mode '0755'
        end
    end
end
