# -*- mode: ruby -*-
# vi: set ft=ruby :

# hosts = {
#   "host01" => "192.168.44.11",
#   "host02" => "192.168.44.12",
# }

# Vagrant.configure("2") do |config|
#   hosts.each do |name, ip|
#     config.vm.define name do |machine|
#       machine.vm.box = "ubuntu/xenial64"
#       machine.vm.hostname = "%s.example.org" % name
#       machine.vm.network "private_network", ip: ip
#       machine.vm.network "forwarded_port", guest: 80, host: 8080
#       machine.vm.provider "virtualbox" do |v|
#           v.name = name
#           v.customize ["modifyvm", :id, "--memory", 1024]
#       end
#     end
#   end
# end

servers=[
  {
    :hostname => "host01",
    :ip => "192.168.44.11",
    :box => "ubuntu/xenial64",
    :ram => 1024,
    :cpu => 2,
    :fp => [80, 80],
  },
  {
    :hostname => "host02",
    :ip => "192.168.44.12",
    :box => "ubuntu/xenial64",
    :ram => 1024,
    :cpu => 2,
    :fp => [80, 80],
  }
]

Vagrant.configure("2") do |config|
  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
      node.vm.box = machine[:box]
      node.vm.hostname = machine[:hostname]
      node.vm.network "private_network", ip: machine[:ip]
      # print machine[:fp][0]
      # node.vm.network "forwarded_port", guest: machine[:fp][0], host: machine[:fp][1]
      node.vm.provider "virtualbox" do |vb|
        vb.name = machine[:hostname]
        vb.customize ["modifyvm", :id, "--memory", machine[:ram]]
      end
    end
  end
end