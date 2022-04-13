# mininet_tests
Installing ubuntu vm on mac

*install virtual box, vagrant.
create a separate directory and add ‘Vagrantfile’ with needed network and other settings
#mkdir ubuntu
#cd ubuntu
#vi Vagrantfile

Vagrant.configure("2") do |config|
  config.ssh.insert_key = false
  config.vm.define "worker" do |worker|
    worker.vm.box = "ubuntu/bionic64"
  end
  config.vm.network "public_network", bridge: "en0: Wi-Fi (Wireless)"
end

#vagrant up

The virtual machine should come up and have 2 interfaces 1)nat to connect to the internet 2)bridge interface to connect to the local network.

* “public_network” config ensures that bridge interface is attached to the vm and by default gets dhcp ip address



Installing mininet and test module:

This can be done inside vm or in host machine

sudo apt update
sudo apt install mininet
git clone  https://github.com/saikat2sls/mininet_tests.git
---------------------------------------------------------------------
1. running bandwidth base tests on tree topology


         ISP1 
          |
         (RT1)
     /   /     \   \
   GW1  GW2   GW3  GW4    
    |   |      |     |  
 CPE1   CPE3   CPE5  CPE7
   CPE2   CPE4  CPE6   CPE8

#sudo ./bw_test.py

Verify the speed test-results in <cpe_final>. file


change bw allocation for the link snad rerun

---------------------------------------------------------------------

2.  *Connecting mininet hosts using Tunnel :*

Create 2 ubunti VM(s) say VM1 and VM2. Install mininet and oython in both of them.
Install pox controller in VM-1
Have 3 terminals open for VM1, VM2 and pox controller respectively.
Run testVM1.py in VM1, testVM2.py in VM2

