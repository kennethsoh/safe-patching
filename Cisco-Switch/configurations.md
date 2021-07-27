## Cisco 3850 L3 Switch Configuration

#### Introduction
The following is the configurations used to configure the cisco switch to work with the MUD Manager. 

VLAN 10 is used as the internal VLAN, and interface G1/0/7 is reserved for MUD Client.

The radius server is assumed to be at 192.168.1.10.

```

aaa new-model 
! 
aaa authentication dot1x default group radius 
aaa authorization network default group radius 
aaa accounting identity default start-stop group radius 
aaa accounting network default start-stop group radius 
! 
aaa server radius dynamic-author 
  client 192.168.1.10 server-key cisco 
  server-key cisco 
! 
aaa session-id common 
radius server AAA 
address ipv4 192.168.1.10 auth-port 1812 acct-port 1813 
  key cisco 
access-session attributes filter-list list mudtest 
  lldp 
  dhcp 
! 
ip dhcp snooping 
ip dhcp snooping vlan 10 
! 
access-session accounting attributes filter-spec include list mudtest 
access-session monitor 
! 
lldp run 
! 
policy-map type control subscriber mud-mab-test 
  event session-started match-all 
    10 class always do-until-failure 
      10 authenticate using mab 
! 
template mud-mab-test 
  switchport mode access 
  mab 
  access-session port-control auto 
  service-policy type control subscriber mud-mab-test 
! 
interface GigabitEthernet1/0/7 
  source template mud-mab-test 
!
```
