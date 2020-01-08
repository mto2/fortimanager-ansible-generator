#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
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
module: fmgr_pm_config_obj_vpnmgr_node
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/vpnmgr/node
    - /pm/config/global/obj/vpnmgr/node
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
        description: 'VPN node for VPN Manager. Must specify vpntable and scope member.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    add-route:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    assign-ip:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    assign-ip-from:
                        type: str
                        choices:
                            - 'range'
                            - 'usrgrp'
                            - 'dhcp'
                            - 'name'
                    authpasswd:
                        -
                            type: str
                    authusr:
                        type: str
                    authusrgrp:
                        type: str
                    auto-configuration:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    automatic_routing:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    banner:
                        type: str
                    default-gateway:
                        type: str
                    dhcp-server:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dns-mode:
                        type: str
                        choices:
                            - 'auto'
                            - 'manual'
                    dns-service:
                        type: str
                        choices:
                            - 'default'
                            - 'specify'
                            - 'local'
                    domain:
                        type: str
                    extgw:
                        type: str
                    extgw_hubip:
                        type: str
                    extgw_p2_per_net:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    extgwip:
                        type: str
                    hub_iface:
                        type: str
                    id:
                        type: int
                    iface:
                        type: str
                    ip-range:
                        -
                            end-ip:
                                type: str
                            id:
                                type: int
                            start-ip:
                                type: str
                    ipsec-lease-hold:
                        type: int
                    ipv4-dns-server1:
                        type: str
                    ipv4-dns-server2:
                        type: str
                    ipv4-dns-server3:
                        type: str
                    ipv4-end-ip:
                        type: str
                    ipv4-exclude-range:
                        -
                            end-ip:
                                type: str
                            id:
                                type: int
                            start-ip:
                                type: str
                    ipv4-netmask:
                        type: str
                    ipv4-split-include:
                        type: str
                    ipv4-start-ip:
                        type: str
                    ipv4-wins-server1:
                        type: str
                    ipv4-wins-server2:
                        type: str
                    local-gw:
                        type: str
                    localid:
                        type: str
                    mode-cfg:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    mode-cfg-ip-version:
                        type: str
                        choices:
                            - '4'
                            - '6'
                    net-device:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    peer:
                        type: str
                    peergrp:
                        type: str
                    peerid:
                        type: str
                    peertype:
                        type: str
                        choices:
                            - 'any'
                            - 'one'
                            - 'dialup'
                            - 'peer'
                            - 'peergrp'
                    protected_subnet:
                        -
                            addr:
                                type: str
                            seq:
                                type: int
                    public-ip:
                        type: str
                    role:
                        type: str
                        choices:
                            - 'hub'
                            - 'spoke'
                    route-overlap:
                        type: str
                        choices:
                            - 'use-old'
                            - 'use-new'
                            - 'allow'
                    spoke-zone:
                        type: str
                    summary_addr:
                        -
                            addr:
                                type: str
                            priority:
                                type: int
                            seq:
                                type: int
                    tunnel-search:
                        type: str
                        choices:
                            - 'selectors'
                            - 'nexthop'
                    unity-support:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    usrgrp:
                        type: str
                    vpn-interface-priority:
                        type: int
                    vpn-zone:
                        type: str
                    vpntable:
                        type: str
                    xauthtype:
                        type: str
                        choices:
                            - 'disable'
                            - 'client'
                            - 'pap'
                            - 'chap'
                            - 'auto'
    schema_object1:
        methods: [get]
        description: 'VPN node for VPN Manager. Must specify vpntable and scope member.'
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
                            - 'add-route'
                            - 'assign-ip'
                            - 'assign-ip-from'
                            - 'authpasswd'
                            - 'authusr'
                            - 'authusrgrp'
                            - 'auto-configuration'
                            - 'automatic_routing'
                            - 'banner'
                            - 'default-gateway'
                            - 'dhcp-server'
                            - 'dns-mode'
                            - 'dns-service'
                            - 'domain'
                            - 'extgw'
                            - 'extgw_hubip'
                            - 'extgw_p2_per_net'
                            - 'extgwip'
                            - 'hub_iface'
                            - 'id'
                            - 'iface'
                            - 'ipsec-lease-hold'
                            - 'ipv4-dns-server1'
                            - 'ipv4-dns-server2'
                            - 'ipv4-dns-server3'
                            - 'ipv4-end-ip'
                            - 'ipv4-netmask'
                            - 'ipv4-split-include'
                            - 'ipv4-start-ip'
                            - 'ipv4-wins-server1'
                            - 'ipv4-wins-server2'
                            - 'local-gw'
                            - 'localid'
                            - 'mode-cfg'
                            - 'mode-cfg-ip-version'
                            - 'net-device'
                            - 'peer'
                            - 'peergrp'
                            - 'peerid'
                            - 'peertype'
                            - 'public-ip'
                            - 'role'
                            - 'route-overlap'
                            - 'spoke-zone'
                            - 'tunnel-search'
                            - 'unity-support'
                            - 'usrgrp'
                            - 'vpn-interface-priority'
                            - 'vpn-zone'
                            - 'vpntable'
                            - 'xauthtype'
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/VPNMGR/NODE
      fmgr_pm_config_obj_vpnmgr_node:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     add-route: <value in [disable, enable]>
                     assign-ip: <value in [disable, enable]>
                     assign-ip-from: <value in [range, usrgrp, dhcp, ...]>
                     authpasswd:
                       - <value of string>
                     authusr: <value of string>
                     authusrgrp: <value of string>
                     auto-configuration: <value in [disable, enable]>
                     automatic_routing: <value in [disable, enable]>
                     banner: <value of string>
                     default-gateway: <value of string>
                     dhcp-server: <value in [disable, enable]>
                     dns-mode: <value in [auto, manual]>
                     dns-service: <value in [default, specify, local]>
                     domain: <value of string>
                     extgw: <value of string>
                     extgw_hubip: <value of string>
                     extgw_p2_per_net: <value in [disable, enable]>
                     extgwip: <value of string>
                     hub_iface: <value of string>
                     id: <value of integer>
                     iface: <value of string>
                     ip-range:
                       -
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     ipsec-lease-hold: <value of integer>
                     ipv4-dns-server1: <value of string>
                     ipv4-dns-server2: <value of string>
                     ipv4-dns-server3: <value of string>
                     ipv4-end-ip: <value of string>
                     ipv4-exclude-range:
                       -
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     ipv4-netmask: <value of string>
                     ipv4-split-include: <value of string>
                     ipv4-start-ip: <value of string>
                     ipv4-wins-server1: <value of string>
                     ipv4-wins-server2: <value of string>
                     local-gw: <value of string>
                     localid: <value of string>
                     mode-cfg: <value in [disable, enable]>
                     mode-cfg-ip-version: <value in [4, 6]>
                     net-device: <value in [disable, enable]>
                     peer: <value of string>
                     peergrp: <value of string>
                     peerid: <value of string>
                     peertype: <value in [any, one, dialup, ...]>
                     protected_subnet:
                       -
                           addr: <value of string>
                           seq: <value of integer>
                     public-ip: <value of string>
                     role: <value in [hub, spoke]>
                     route-overlap: <value in [use-old, use-new, allow]>
                     spoke-zone: <value of string>
                     summary_addr:
                       -
                           addr: <value of string>
                           priority: <value of integer>
                           seq: <value of integer>
                     tunnel-search: <value in [selectors, nexthop]>
                     unity-support: <value in [disable, enable]>
                     usrgrp: <value of string>
                     vpn-interface-priority: <value of integer>
                     vpn-zone: <value of string>
                     vpntable: <value of string>
                     xauthtype: <value in [disable, client, pap, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/VPNMGR/NODE
      fmgr_pm_config_obj_vpnmgr_node:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [add-route, assign-ip, assign-ip-from, ...]>
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
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/vpnmgr/node'
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
               add-route:
                  type: str
               assign-ip:
                  type: str
               assign-ip-from:
                  type: str
               authpasswd:
                  type: array
                  suboptions:
                     type: str
               authusr:
                  type: str
               authusrgrp:
                  type: str
               auto-configuration:
                  type: str
               automatic_routing:
                  type: str
               banner:
                  type: str
               default-gateway:
                  type: str
               dhcp-server:
                  type: str
               dns-mode:
                  type: str
               dns-service:
                  type: str
               domain:
                  type: str
               extgw:
                  type: str
               extgw_hubip:
                  type: str
               extgw_p2_per_net:
                  type: str
               extgwip:
                  type: str
               hub_iface:
                  type: str
               id:
                  type: int
               iface:
                  type: str
               ip-range:
                  type: array
                  suboptions:
                     end-ip:
                        type: str
                     id:
                        type: int
                     start-ip:
                        type: str
               ipsec-lease-hold:
                  type: int
               ipv4-dns-server1:
                  type: str
               ipv4-dns-server2:
                  type: str
               ipv4-dns-server3:
                  type: str
               ipv4-end-ip:
                  type: str
               ipv4-exclude-range:
                  type: array
                  suboptions:
                     end-ip:
                        type: str
                     id:
                        type: int
                     start-ip:
                        type: str
               ipv4-netmask:
                  type: str
               ipv4-split-include:
                  type: str
               ipv4-start-ip:
                  type: str
               ipv4-wins-server1:
                  type: str
               ipv4-wins-server2:
                  type: str
               local-gw:
                  type: str
               localid:
                  type: str
               mode-cfg:
                  type: str
               mode-cfg-ip-version:
                  type: str
               net-device:
                  type: str
               peer:
                  type: str
               peergrp:
                  type: str
               peerid:
                  type: str
               peertype:
                  type: str
               protected_subnet:
                  type: array
                  suboptions:
                     addr:
                        type: str
                     seq:
                        type: int
               public-ip:
                  type: str
               role:
                  type: str
               route-overlap:
                  type: str
               spoke-zone:
                  type: str
               summary_addr:
                  type: array
                  suboptions:
                     addr:
                        type: str
                     priority:
                        type: int
                     seq:
                        type: int
               tunnel-search:
                  type: str
               unity-support:
                  type: str
               usrgrp:
                  type: str
               vpn-interface-priority:
                  type: int
               vpn-zone:
                  type: str
               vpntable:
                  type: str
               xauthtype:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/vpnmgr/node'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/vpnmgr/node',
        '/pm/config/global/obj/vpnmgr/node'
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
                        'add-route': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'assign-ip': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'assign-ip-from': {
                            'type': 'string',
                            'enum': [
                                'range',
                                'usrgrp',
                                'dhcp',
                                'name'
                            ]
                        },
                        'authpasswd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'authusr': {
                            'type': 'string'
                        },
                        'authusrgrp': {
                            'type': 'string'
                        },
                        'auto-configuration': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'automatic_routing': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'banner': {
                            'type': 'string'
                        },
                        'default-gateway': {
                            'type': 'string'
                        },
                        'dhcp-server': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dns-mode': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'manual'
                            ]
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
                        'extgw': {
                            'type': 'string'
                        },
                        'extgw_hubip': {
                            'type': 'string'
                        },
                        'extgw_p2_per_net': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'extgwip': {
                            'type': 'string'
                        },
                        'hub_iface': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'iface': {
                            'type': 'string'
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
                        'ipv4-dns-server1': {
                            'type': 'string'
                        },
                        'ipv4-dns-server2': {
                            'type': 'string'
                        },
                        'ipv4-dns-server3': {
                            'type': 'string'
                        },
                        'ipv4-end-ip': {
                            'type': 'string'
                        },
                        'ipv4-exclude-range': {
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
                        'ipv4-netmask': {
                            'type': 'string'
                        },
                        'ipv4-split-include': {
                            'type': 'string'
                        },
                        'ipv4-start-ip': {
                            'type': 'string'
                        },
                        'ipv4-wins-server1': {
                            'type': 'string'
                        },
                        'ipv4-wins-server2': {
                            'type': 'string'
                        },
                        'local-gw': {
                            'type': 'string'
                        },
                        'localid': {
                            'type': 'string'
                        },
                        'mode-cfg': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mode-cfg-ip-version': {
                            'type': 'string',
                            'enum': [
                                '4',
                                '6'
                            ]
                        },
                        'net-device': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'peer': {
                            'type': 'string'
                        },
                        'peergrp': {
                            'type': 'string'
                        },
                        'peerid': {
                            'type': 'string'
                        },
                        'peertype': {
                            'type': 'string',
                            'enum': [
                                'any',
                                'one',
                                'dialup',
                                'peer',
                                'peergrp'
                            ]
                        },
                        'protected_subnet': {
                            'type': 'array',
                            'items': {
                                'addr': {
                                    'type': 'string'
                                },
                                'seq': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'public-ip': {
                            'type': 'string'
                        },
                        'role': {
                            'type': 'string',
                            'enum': [
                                'hub',
                                'spoke'
                            ]
                        },
                        'route-overlap': {
                            'type': 'string',
                            'enum': [
                                'use-old',
                                'use-new',
                                'allow'
                            ]
                        },
                        'spoke-zone': {
                            'type': 'string'
                        },
                        'summary_addr': {
                            'type': 'array',
                            'items': {
                                'addr': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'integer'
                                },
                                'seq': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'tunnel-search': {
                            'type': 'string',
                            'enum': [
                                'selectors',
                                'nexthop'
                            ]
                        },
                        'unity-support': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'usrgrp': {
                            'type': 'string'
                        },
                        'vpn-interface-priority': {
                            'type': 'integer'
                        },
                        'vpn-zone': {
                            'type': 'string'
                        },
                        'vpntable': {
                            'type': 'string'
                        },
                        'xauthtype': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'client',
                                'pap',
                                'chap',
                                'auto'
                            ]
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
                                'add-route',
                                'assign-ip',
                                'assign-ip-from',
                                'authpasswd',
                                'authusr',
                                'authusrgrp',
                                'auto-configuration',
                                'automatic_routing',
                                'banner',
                                'default-gateway',
                                'dhcp-server',
                                'dns-mode',
                                'dns-service',
                                'domain',
                                'extgw',
                                'extgw_hubip',
                                'extgw_p2_per_net',
                                'extgwip',
                                'hub_iface',
                                'id',
                                'iface',
                                'ipsec-lease-hold',
                                'ipv4-dns-server1',
                                'ipv4-dns-server2',
                                'ipv4-dns-server3',
                                'ipv4-end-ip',
                                'ipv4-netmask',
                                'ipv4-split-include',
                                'ipv4-start-ip',
                                'ipv4-wins-server1',
                                'ipv4-wins-server2',
                                'local-gw',
                                'localid',
                                'mode-cfg',
                                'mode-cfg-ip-version',
                                'net-device',
                                'peer',
                                'peergrp',
                                'peerid',
                                'peertype',
                                'public-ip',
                                'role',
                                'route-overlap',
                                'spoke-zone',
                                'tunnel-search',
                                'unity-support',
                                'usrgrp',
                                'vpn-interface-priority',
                                'vpn-zone',
                                'vpntable',
                                'xauthtype'
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

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
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

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()
