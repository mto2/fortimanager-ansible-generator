#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_system_dhcp_server
short_description: Configure DHCP servers.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/system/dhcp/server
    - /pm/config/global/obj/system/dhcp/server
    - Examples include all parameters and values need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
    schema_object0:
        methods: [add, set, update]
        description: 'Configure DHCP servers.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    auto-configuration:
                        type: str
                        description: 'Enable/disable auto configuration.'
                        choices:
                            - 'disable'
                            - 'enable'
                    conflicted-ip-timeout:
                        type: int
                        description: 'Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.'
                    ddns-auth:
                        type: str
                        description: 'DDNS authentication mode.'
                        choices:
                            - 'disable'
                            - 'tsig'
                    ddns-key:
                        type: str
                        description: 'DDNS update key (base 64 encoding).'
                    ddns-keyname:
                        type: str
                        description: 'DDNS update key name.'
                    ddns-server-ip:
                        type: str
                        description: 'DDNS server IP.'
                    ddns-ttl:
                        type: int
                        description: 'TTL.'
                    ddns-update:
                        type: str
                        description: 'Enable/disable DDNS update for DHCP.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ddns-update-override:
                        type: str
                        description: 'Enable/disable DDNS update override for DHCP.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ddns-zone:
                        type: str
                        description: 'Zone of your domain name (ex. DDNS.com).'
                    default-gateway:
                        type: str
                        description: 'Default gateway IP address assigned by the DHCP server.'
                    dns-server1:
                        type: str
                        description: 'DNS server 1.'
                    dns-server2:
                        type: str
                        description: 'DNS server 2.'
                    dns-server3:
                        type: str
                        description: 'DNS server 3.'
                    dns-service:
                        type: str
                        description: 'Options for assigning DNS servers to DHCP clients.'
                        choices:
                            - 'default'
                            - 'specify'
                            - 'local'
                    domain:
                        type: str
                        description: 'Domain name suffix for the IP addresses that the DHCP server assigns to clients.'
                    exclude-range:
                        -
                            end-ip:
                                type: str
                                description: 'End of IP range.'
                            id:
                                type: int
                                description: 'ID.'
                            start-ip:
                                type: str
                                description: 'Start of IP range.'
                    filename:
                        type: str
                        description: 'Name of the boot file on the TFTP server.'
                    forticlient-on-net-status:
                        type: str
                        description: 'Enable/disable FortiClient-On-Net service for this DHCP server.'
                        choices:
                            - 'disable'
                            - 'enable'
                    id:
                        type: int
                        description: 'ID.'
                    interface:
                        type: str
                        description: 'DHCP server can assign IP configurations to clients connected to this interface.'
                    ip-mode:
                        type: str
                        description: 'Method used to assign client IP.'
                        choices:
                            - 'range'
                            - 'usrgrp'
                    ip-range:
                        -
                            end-ip:
                                type: str
                                description: 'End of IP range.'
                            id:
                                type: int
                                description: 'ID.'
                            start-ip:
                                type: str
                                description: 'Start of IP range.'
                    ipsec-lease-hold:
                        type: int
                        description: 'DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).'
                    lease-time:
                        type: int
                        description: 'Lease time in seconds, 0 means unlimited.'
                    mac-acl-default-action:
                        type: str
                        description: 'MAC access control default action (allow or block assigning IP settings).'
                        choices:
                            - 'assign'
                            - 'block'
                    netmask:
                        type: str
                        description: 'Netmask assigned by the DHCP server.'
                    next-server:
                        type: str
                        description: 'IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.'
                    ntp-server1:
                        type: str
                        description: 'NTP server 1.'
                    ntp-server2:
                        type: str
                        description: 'NTP server 2.'
                    ntp-server3:
                        type: str
                        description: 'NTP server 3.'
                    ntp-service:
                        type: str
                        description: 'Options for assigning Network Time Protocol (NTP) servers to DHCP clients.'
                        choices:
                            - 'default'
                            - 'specify'
                            - 'local'
                    options:
                        -
                            code:
                                type: int
                                description: 'DHCP option code.'
                            id:
                                type: int
                                description: 'ID.'
                            ip:
                                -
                                    type: str
                            type:
                                type: str
                                description: 'DHCP option type.'
                                choices:
                                    - 'hex'
                                    - 'string'
                                    - 'ip'
                                    - 'fqdn'
                            value:
                                type: str
                                description: 'DHCP option value.'
                    reserved-address:
                        -
                            action:
                                type: str
                                description: 'Options for the DHCP server to configure the client with the reserved MAC address.'
                                choices:
                                    - 'assign'
                                    - 'block'
                                    - 'reserved'
                            description:
                                type: str
                                description: 'Description.'
                            id:
                                type: int
                                description: 'ID.'
                            ip:
                                type: str
                                description: 'IP address to be reserved for the MAC address.'
                            mac:
                                type: str
                                description: 'MAC address of the client that will get the reserved IP address.'
                    server-type:
                        type: str
                        description: 'DHCP server can be a normal DHCP server or an IPsec DHCP server.'
                        choices:
                            - 'regular'
                            - 'ipsec'
                    status:
                        type: str
                        description: 'Enable/disable this DHCP configuration.'
                        choices:
                            - 'disable'
                            - 'enable'
                    tftp-server:
                        -
                            type: str
                    timezone:
                        type: str
                        description: 'Select the time zone to be assigned to DHCP clients.'
                        choices:
                            - '00'
                            - '01'
                            - '02'
                            - '03'
                            - '04'
                            - '05'
                            - '06'
                            - '07'
                            - '08'
                            - '09'
                            - '10'
                            - '11'
                            - '12'
                            - '13'
                            - '14'
                            - '15'
                            - '16'
                            - '17'
                            - '18'
                            - '19'
                            - '20'
                            - '21'
                            - '22'
                            - '23'
                            - '24'
                            - '25'
                            - '26'
                            - '27'
                            - '28'
                            - '29'
                            - '30'
                            - '31'
                            - '32'
                            - '33'
                            - '34'
                            - '35'
                            - '36'
                            - '37'
                            - '38'
                            - '39'
                            - '40'
                            - '41'
                            - '42'
                            - '43'
                            - '44'
                            - '45'
                            - '46'
                            - '47'
                            - '48'
                            - '49'
                            - '50'
                            - '51'
                            - '52'
                            - '53'
                            - '54'
                            - '55'
                            - '56'
                            - '57'
                            - '58'
                            - '59'
                            - '60'
                            - '61'
                            - '62'
                            - '63'
                            - '64'
                            - '65'
                            - '66'
                            - '67'
                            - '68'
                            - '69'
                            - '70'
                            - '71'
                            - '72'
                            - '73'
                            - '74'
                            - '75'
                            - '76'
                            - '77'
                            - '78'
                            - '79'
                            - '80'
                            - '81'
                            - '82'
                            - '83'
                            - '84'
                            - '85'
                            - '86'
                            - '87'
                    timezone-option:
                        type: str
                        description: 'Options for the DHCP server to set the clients time zone.'
                        choices:
                            - 'disable'
                            - 'default'
                            - 'specify'
                    vci-match:
                        type: str
                        description: 'Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.'
                        choices:
                            - 'disable'
                            - 'enable'
                    vci-string:
                        -
                            type: str
                    wifi-ac1:
                        type: str
                        description: 'WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).'
                    wifi-ac2:
                        type: str
                        description: 'WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).'
                    wifi-ac3:
                        type: str
                        description: 'WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).'
                    wins-server1:
                        type: str
                        description: 'WINS server 1.'
                    wins-server2:
                        type: str
                        description: 'WINS server 2.'
    schema_object1:
        methods: [get]
        description: 'Configure DHCP servers.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'auto-configuration'
                            - 'conflicted-ip-timeout'
                            - 'ddns-auth'
                            - 'ddns-key'
                            - 'ddns-keyname'
                            - 'ddns-server-ip'
                            - 'ddns-ttl'
                            - 'ddns-update'
                            - 'ddns-update-override'
                            - 'ddns-zone'
                            - 'default-gateway'
                            - 'dns-server1'
                            - 'dns-server2'
                            - 'dns-server3'
                            - 'dns-service'
                            - 'domain'
                            - 'filename'
                            - 'forticlient-on-net-status'
                            - 'id'
                            - 'interface'
                            - 'ip-mode'
                            - 'ipsec-lease-hold'
                            - 'lease-time'
                            - 'mac-acl-default-action'
                            - 'netmask'
                            - 'next-server'
                            - 'ntp-server1'
                            - 'ntp-server2'
                            - 'ntp-server3'
                            - 'ntp-service'
                            - 'server-type'
                            - 'status'
                            - 'tftp-server'
                            - 'timezone'
                            - 'timezone-option'
                            - 'vci-match'
                            - 'vci-string'
                            - 'wifi-ac1'
                            - 'wifi-ac2'
                            - 'wifi-ac3'
                            - 'wins-server1'
                            - 'wins-server2'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/DHCP/SERVER
      fmgr_system_dhcp_server:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     auto-configuration: <value in [disable, enable]>
                     conflicted-ip-timeout: <value of integer>
                     ddns-auth: <value in [disable, tsig]>
                     ddns-key: <value of string>
                     ddns-keyname: <value of string>
                     ddns-server-ip: <value of string>
                     ddns-ttl: <value of integer>
                     ddns-update: <value in [disable, enable]>
                     ddns-update-override: <value in [disable, enable]>
                     ddns-zone: <value of string>
                     default-gateway: <value of string>
                     dns-server1: <value of string>
                     dns-server2: <value of string>
                     dns-server3: <value of string>
                     dns-service: <value in [default, specify, local]>
                     domain: <value of string>
                     exclude-range:
                       -
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     filename: <value of string>
                     forticlient-on-net-status: <value in [disable, enable]>
                     id: <value of integer>
                     interface: <value of string>
                     ip-mode: <value in [range, usrgrp]>
                     ip-range:
                       -
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     ipsec-lease-hold: <value of integer>
                     lease-time: <value of integer>
                     mac-acl-default-action: <value in [assign, block]>
                     netmask: <value of string>
                     next-server: <value of string>
                     ntp-server1: <value of string>
                     ntp-server2: <value of string>
                     ntp-server3: <value of string>
                     ntp-service: <value in [default, specify, local]>
                     options:
                       -
                           code: <value of integer>
                           id: <value of integer>
                           ip:
                             - <value of string>
                           type: <value in [hex, string, ip, ...]>
                           value: <value of string>
                     reserved-address:
                       -
                           action: <value in [assign, block, reserved]>
                           description: <value of string>
                           id: <value of integer>
                           ip: <value of string>
                           mac: <value of string>
                     server-type: <value in [regular, ipsec]>
                     status: <value in [disable, enable]>
                     tftp-server:
                       - <value of string>
                     timezone: <value in [00, 01, 02, ...]>
                     timezone-option: <value in [disable, default, specify]>
                     vci-match: <value in [disable, enable]>
                     vci-string:
                       - <value of string>
                     wifi-ac1: <value of string>
                     wifi-ac2: <value of string>
                     wifi-ac3: <value of string>
                     wins-server1: <value of string>
                     wins-server2: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/DHCP/SERVER
      fmgr_system_dhcp_server:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [auto-configuration, conflicted-ip-timeout, ddns-auth, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               id:
                  type: int
                  description: 'ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/system/dhcp/server'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               auto-configuration:
                  type: str
                  description: 'Enable/disable auto configuration.'
               conflicted-ip-timeout:
                  type: int
                  description: 'Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.'
               ddns-auth:
                  type: str
                  description: 'DDNS authentication mode.'
               ddns-key:
                  type: str
                  description: 'DDNS update key (base 64 encoding).'
               ddns-keyname:
                  type: str
                  description: 'DDNS update key name.'
               ddns-server-ip:
                  type: str
                  description: 'DDNS server IP.'
               ddns-ttl:
                  type: int
                  description: 'TTL.'
               ddns-update:
                  type: str
                  description: 'Enable/disable DDNS update for DHCP.'
               ddns-update-override:
                  type: str
                  description: 'Enable/disable DDNS update override for DHCP.'
               ddns-zone:
                  type: str
                  description: 'Zone of your domain name (ex. DDNS.com).'
               default-gateway:
                  type: str
                  description: 'Default gateway IP address assigned by the DHCP server.'
               dns-server1:
                  type: str
                  description: 'DNS server 1.'
               dns-server2:
                  type: str
                  description: 'DNS server 2.'
               dns-server3:
                  type: str
                  description: 'DNS server 3.'
               dns-service:
                  type: str
                  description: 'Options for assigning DNS servers to DHCP clients.'
               domain:
                  type: str
                  description: 'Domain name suffix for the IP addresses that the DHCP server assigns to clients.'
               exclude-range:
                  type: array
                  suboptions:
                     end-ip:
                        type: str
                        description: 'End of IP range.'
                     id:
                        type: int
                        description: 'ID.'
                     start-ip:
                        type: str
                        description: 'Start of IP range.'
               filename:
                  type: str
                  description: 'Name of the boot file on the TFTP server.'
               forticlient-on-net-status:
                  type: str
                  description: 'Enable/disable FortiClient-On-Net service for this DHCP server.'
               id:
                  type: int
                  description: 'ID.'
               interface:
                  type: str
                  description: 'DHCP server can assign IP configurations to clients connected to this interface.'
               ip-mode:
                  type: str
                  description: 'Method used to assign client IP.'
               ip-range:
                  type: array
                  suboptions:
                     end-ip:
                        type: str
                        description: 'End of IP range.'
                     id:
                        type: int
                        description: 'ID.'
                     start-ip:
                        type: str
                        description: 'Start of IP range.'
               ipsec-lease-hold:
                  type: int
                  description: 'DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).'
               lease-time:
                  type: int
                  description: 'Lease time in seconds, 0 means unlimited.'
               mac-acl-default-action:
                  type: str
                  description: 'MAC access control default action (allow or block assigning IP settings).'
               netmask:
                  type: str
                  description: 'Netmask assigned by the DHCP server.'
               next-server:
                  type: str
                  description: 'IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.'
               ntp-server1:
                  type: str
                  description: 'NTP server 1.'
               ntp-server2:
                  type: str
                  description: 'NTP server 2.'
               ntp-server3:
                  type: str
                  description: 'NTP server 3.'
               ntp-service:
                  type: str
                  description: 'Options for assigning Network Time Protocol (NTP) servers to DHCP clients.'
               options:
                  type: array
                  suboptions:
                     code:
                        type: int
                        description: 'DHCP option code.'
                     id:
                        type: int
                        description: 'ID.'
                     ip:
                        type: array
                        suboptions:
                           type: str
                     type:
                        type: str
                        description: 'DHCP option type.'
                     value:
                        type: str
                        description: 'DHCP option value.'
               reserved-address:
                  type: array
                  suboptions:
                     action:
                        type: str
                        description: 'Options for the DHCP server to configure the client with the reserved MAC address.'
                     description:
                        type: str
                        description: 'Description.'
                     id:
                        type: int
                        description: 'ID.'
                     ip:
                        type: str
                        description: 'IP address to be reserved for the MAC address.'
                     mac:
                        type: str
                        description: 'MAC address of the client that will get the reserved IP address.'
               server-type:
                  type: str
                  description: 'DHCP server can be a normal DHCP server or an IPsec DHCP server.'
               status:
                  type: str
                  description: 'Enable/disable this DHCP configuration.'
               tftp-server:
                  type: array
                  suboptions:
                     type: str
               timezone:
                  type: str
                  description: 'Select the time zone to be assigned to DHCP clients.'
               timezone-option:
                  type: str
                  description: 'Options for the DHCP server to set the clients time zone.'
               vci-match:
                  type: str
                  description: 'Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.'
               vci-string:
                  type: array
                  suboptions:
                     type: str
               wifi-ac1:
                  type: str
                  description: 'WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).'
               wifi-ac2:
                  type: str
                  description: 'WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).'
               wifi-ac3:
                  type: str
                  description: 'WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).'
               wins-server1:
                  type: str
                  description: 'WINS server 1.'
               wins-server2:
                  type: str
                  description: 'WINS server 2.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/system/dhcp/server'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/dhcp/server',
        '/pm/config/global/obj/system/dhcp/server'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'auto-configuration': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'conflicted-ip-timeout': {
                            'type': 'integer'
                        },
                        'ddns-auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'tsig'
                            ]
                        },
                        'ddns-key': {
                            'type': 'string'
                        },
                        'ddns-keyname': {
                            'type': 'string'
                        },
                        'ddns-server-ip': {
                            'type': 'string'
                        },
                        'ddns-ttl': {
                            'type': 'integer'
                        },
                        'ddns-update': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ddns-update-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ddns-zone': {
                            'type': 'string'
                        },
                        'default-gateway': {
                            'type': 'string'
                        },
                        'dns-server1': {
                            'type': 'string'
                        },
                        'dns-server2': {
                            'type': 'string'
                        },
                        'dns-server3': {
                            'type': 'string'
                        },
                        'dns-service': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'specify',
                                'local'
                            ]
                        },
                        'domain': {
                            'type': 'string'
                        },
                        'exclude-range': {
                            'type': 'array',
                            'items': {
                                'end-ip': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'start-ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'filename': {
                            'type': 'string'
                        },
                        'forticlient-on-net-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'interface': {
                            'type': 'string'
                        },
                        'ip-mode': {
                            'type': 'string',
                            'enum': [
                                'range',
                                'usrgrp'
                            ]
                        },
                        'ip-range': {
                            'type': 'array',
                            'items': {
                                'end-ip': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'start-ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ipsec-lease-hold': {
                            'type': 'integer'
                        },
                        'lease-time': {
                            'type': 'integer'
                        },
                        'mac-acl-default-action': {
                            'type': 'string',
                            'enum': [
                                'assign',
                                'block'
                            ]
                        },
                        'netmask': {
                            'type': 'string'
                        },
                        'next-server': {
                            'type': 'string'
                        },
                        'ntp-server1': {
                            'type': 'string'
                        },
                        'ntp-server2': {
                            'type': 'string'
                        },
                        'ntp-server3': {
                            'type': 'string'
                        },
                        'ntp-service': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'specify',
                                'local'
                            ]
                        },
                        'options': {
                            'type': 'array',
                            'items': {
                                'code': {
                                    'type': 'integer'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'hex',
                                        'string',
                                        'ip',
                                        'fqdn'
                                    ]
                                },
                                'value': {
                                    'type': 'string'
                                }
                            }
                        },
                        'reserved-address': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'assign',
                                        'block',
                                        'reserved'
                                    ]
                                },
                                'description': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'mac': {
                                    'type': 'string'
                                }
                            }
                        },
                        'server-type': {
                            'type': 'string',
                            'enum': [
                                'regular',
                                'ipsec'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tftp-server': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'timezone': {
                            'type': 'string',
                            'enum': [
                                '00',
                                '01',
                                '02',
                                '03',
                                '04',
                                '05',
                                '06',
                                '07',
                                '08',
                                '09',
                                '10',
                                '11',
                                '12',
                                '13',
                                '14',
                                '15',
                                '16',
                                '17',
                                '18',
                                '19',
                                '20',
                                '21',
                                '22',
                                '23',
                                '24',
                                '25',
                                '26',
                                '27',
                                '28',
                                '29',
                                '30',
                                '31',
                                '32',
                                '33',
                                '34',
                                '35',
                                '36',
                                '37',
                                '38',
                                '39',
                                '40',
                                '41',
                                '42',
                                '43',
                                '44',
                                '45',
                                '46',
                                '47',
                                '48',
                                '49',
                                '50',
                                '51',
                                '52',
                                '53',
                                '54',
                                '55',
                                '56',
                                '57',
                                '58',
                                '59',
                                '60',
                                '61',
                                '62',
                                '63',
                                '64',
                                '65',
                                '66',
                                '67',
                                '68',
                                '69',
                                '70',
                                '71',
                                '72',
                                '73',
                                '74',
                                '75',
                                '76',
                                '77',
                                '78',
                                '79',
                                '80',
                                '81',
                                '82',
                                '83',
                                '84',
                                '85',
                                '86',
                                '87'
                            ]
                        },
                        'timezone-option': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'default',
                                'specify'
                            ]
                        },
                        'vci-match': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'vci-string': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'wifi-ac1': {
                            'type': 'string'
                        },
                        'wifi-ac2': {
                            'type': 'string'
                        },
                        'wifi-ac3': {
                            'type': 'string'
                        },
                        'wins-server1': {
                            'type': 'string'
                        },
                        'wins-server2': {
                            'type': 'string'
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'auto-configuration',
                                'conflicted-ip-timeout',
                                'ddns-auth',
                                'ddns-key',
                                'ddns-keyname',
                                'ddns-server-ip',
                                'ddns-ttl',
                                'ddns-update',
                                'ddns-update-override',
                                'ddns-zone',
                                'default-gateway',
                                'dns-server1',
                                'dns-server2',
                                'dns-server3',
                                'dns-service',
                                'domain',
                                'filename',
                                'forticlient-on-net-status',
                                'id',
                                'interface',
                                'ip-mode',
                                'ipsec-lease-hold',
                                'lease-time',
                                'mac-acl-default-action',
                                'netmask',
                                'next-server',
                                'ntp-server1',
                                'ntp-server2',
                                'ntp-server3',
                                'ntp-service',
                                'server-type',
                                'status',
                                'tftp-server',
                                'timezone',
                                'timezone-option',
                                'vci-match',
                                'vci-string',
                                'wifi-ac1',
                                'wifi-ac2',
                                'wifi-ac3',
                                'wins-server1',
                                'wins-server2'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
                                ]
                            }
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'add': 'object0',
            'get': 'object1',
            'set': 'object0',
            'update': 'object0'
        }
    }

    module_arg_spec = {
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'add',
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    method = module.params['method']
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation is False:
            tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
