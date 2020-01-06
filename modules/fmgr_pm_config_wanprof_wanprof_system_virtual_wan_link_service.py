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
module: fmgr_pm_config_wanprof_wanprof_system_virtual_wan_link_service
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service
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
            wanprof:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    addr-mode:
                        type: str
                        description: 'Address mode (IPv4 or IPv6).'
                        choices:
                            - ipv4
                            - ipv6
                    bandwidth-weight:
                        type: int
                        description: 'Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.'
                    default:
                        type: str
                        description: 'Enable/disable use of SD-WAN as default service.'
                        choices:
                            - disable
                            - enable
                    dscp-forward:
                        type: str
                        description: 'Enable/disable forward traffic DSCP tag.'
                        choices:
                            - disable
                            - enable
                    dscp-forward-tag:
                        type: str
                        description: 'Forward traffic DSCP tag.'
                    dscp-reverse:
                        type: str
                        description: 'Enable/disable reverse traffic DSCP tag.'
                        choices:
                            - disable
                            - enable
                    dscp-reverse-tag:
                        type: str
                        description: 'Reverse traffic DSCP tag.'
                    dst:
                        type: str
                        description: 'Destination address name.'
                    dst-negate:
                        type: str
                        description: 'Enable/disable negation of destination address match.'
                        choices:
                            - disable
                            - enable
                    dst6:
                        type: str
                        description: 'Destination address6 name.'
                    end-port:
                        type: int
                        description: 'End destination port number.'
                    gateway:
                        type: str
                        description: 'Enable/disable SD-WAN service gateway.'
                        choices:
                            - disable
                            - enable
                    groups:
                        type: str
                        description: 'User groups.'
                    health-check:
                        type: str
                        description: 'Health check.'
                    hold-down-time:
                        type: int
                        description: 'Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).'
                    id:
                        type: int
                        description: 'Priority rule ID (1 - 4000).'
                    internet-service:
                        type: str
                        description: 'Enable/disable use of Internet service for application-based load balancing.'
                        choices:
                            - disable
                            - enable
                    internet-service-ctrl:
                        -
                            type: int
                    internet-service-ctrl-group:
                        type: str
                        description: 'Control-based Internet Service group list.'
                    internet-service-custom:
                        type: str
                        description: 'Custom Internet service name list.'
                    internet-service-custom-group:
                        type: str
                        description: 'Custom Internet Service group list.'
                    internet-service-group:
                        type: str
                        description: 'Internet Service group list.'
                    internet-service-id:
                        type: str
                        description: 'Internet service ID list.'
                    jitter-weight:
                        type: int
                        description: 'Coefficient of jitter in the formula of custom-profile-1.'
                    latency-weight:
                        type: int
                        description: 'Coefficient of latency in the formula of custom-profile-1.'
                    link-cost-factor:
                        type: str
                        description: 'Link cost factor.'
                        choices:
                            - latency
                            - jitter
                            - packet-loss
                            - inbandwidth
                            - outbandwidth
                            - bibandwidth
                            - custom-profile-1
                    link-cost-threshold:
                        type: int
                        description: 'Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).'
                    member:
                        type: str
                        description: 'Member sequence number.'
                    mode:
                        type: str
                        description: 'Control how the priority rule sets the priority of interfaces in the SD-WAN.'
                        choices:
                            - auto
                            - manual
                            - priority
                            - sla
                            - load-balance
                    name:
                        type: str
                        description: 'Priority rule name.'
                    packet-loss-weight:
                        type: int
                        description: 'Coefficient of packet-loss in the formula of custom-profile-1.'
                    priority-members:
                        type: str
                        description: 'Member sequence number list.'
                    protocol:
                        type: int
                        description: 'Protocol number.'
                    quality-link:
                        type: int
                        description: 'Quality grade.'
                    route-tag:
                        type: int
                        description: 'IPv4 route map route-tag.'
                    sla:
                        -
                            health-check:
                                type: str
                                description: 'Virtual WAN Link health-check.'
                            id:
                                type: int
                                description: 'SLA ID.'
                    src:
                        type: str
                        description: 'Source address name.'
                    src-negate:
                        type: str
                        description: 'Enable/disable negation of source address match.'
                        choices:
                            - disable
                            - enable
                    src6:
                        type: str
                        description: 'Source address6 name.'
                    start-port:
                        type: int
                        description: 'Start destination port number.'
                    status:
                        type: str
                        description: 'Enable/disable SD-WAN service.'
                        choices:
                            - disable
                            - enable
                    tos:
                        type: str
                        description: 'Type of service bit pattern.'
                    tos-mask:
                        type: str
                        description: 'Type of service evaluated bits.'
                    users:
                        type: str
                        description: 'User name.'
    schema_object1:
        methods: [get]
        description: 'Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.'
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
                            - addr-mode
                            - bandwidth-weight
                            - default
                            - dscp-forward
                            - dscp-forward-tag
                            - dscp-reverse
                            - dscp-reverse-tag
                            - dst
                            - dst-negate
                            - dst6
                            - end-port
                            - gateway
                            - groups
                            - health-check
                            - hold-down-time
                            - id
                            - internet-service
                            - internet-service-ctrl
                            - internet-service-ctrl-group
                            - internet-service-custom
                            - internet-service-custom-group
                            - internet-service-group
                            - internet-service-id
                            - jitter-weight
                            - latency-weight
                            - link-cost-factor
                            - link-cost-threshold
                            - member
                            - mode
                            - name
                            - packet-loss-weight
                            - priority-members
                            - protocol
                            - quality-link
                            - route-tag
                            - src
                            - src-negate
                            - src6
                            - start-port
                            - status
                            - tos
                            - tos-mask
                            - users
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
                    - count
                    - object member
                    - datasrc
                    - get reserved
                    - syntax
            range:
                -
                    type: int
            sortings:
                -
                    \{attr_name\}:
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
    - name: send request to /pm/config/wanprof/{wanprof}/system/virtual-wan-link/service
      fmgr_pm_config_wanprof_wanprof_system_virtual_wan_link_service:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            - 
               data: 
                - 
                     addr-mode: <value in [ipv4, ipv6]>
                     bandwidth-weight: <value of integer>
                     default: <value in [disable, enable]>
                     dscp-forward: <value in [disable, enable]>
                     dscp-forward-tag: <value of string>
                     dscp-reverse: <value in [disable, enable]>
                     dscp-reverse-tag: <value of string>
                     dst: <value of string>
                     dst-negate: <value in [disable, enable]>
                     dst6: <value of string>
                     end-port: <value of integer>
                     gateway: <value in [disable, enable]>
                     groups: <value of string>
                     health-check: <value of string>
                     hold-down-time: <value of integer>
                     id: <value of integer>
                     internet-service: <value in [disable, enable]>
                     internet-service-ctrl: 
                      - <value of integer>
                     internet-service-ctrl-group: <value of string>
                     internet-service-custom: <value of string>
                     internet-service-custom-group: <value of string>
                     internet-service-group: <value of string>
                     internet-service-id: <value of string>
                     jitter-weight: <value of integer>
                     latency-weight: <value of integer>
                     link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
                     link-cost-threshold: <value of integer>
                     member: <value of string>
                     mode: <value in [auto, manual, priority, ...]>
                     name: <value of string>
                     packet-loss-weight: <value of integer>
                     priority-members: <value of string>
                     protocol: <value of integer>
                     quality-link: <value of integer>
                     route-tag: <value of integer>
                     sla: 
                      - 
                           health-check: <value of string>
                           id: <value of integer>
                     src: <value of string>
                     src-negate: <value in [disable, enable]>
                     src6: <value of string>
                     start-port: <value of integer>
                     status: <value in [disable, enable]>
                     tos: <value of string>
                     tos-mask: <value of string>
                     users: <value of string>
    - name: send request to /pm/config/wanprof/{wanprof}/system/virtual-wan-link/service
      fmgr_pm_config_wanprof_wanprof_system_virtual_wan_link_service:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [addr-mode, bandwidth-weight, default, ...]>
               filter: 
                - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range: 
                - <value of integer>
               sortings: 
                - 
                     \{attr_name\}: <value in [1, -1]>

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
                  description: 'Priority rule ID (1 - 4000).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service
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
               addr-mode:
                  type: str
                  description: 'Address mode (IPv4 or IPv6).'
               bandwidth-weight:
                  type: int
                  description: 'Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.'
               default:
                  type: str
                  description: 'Enable/disable use of SD-WAN as default service.'
               dscp-forward:
                  type: str
                  description: 'Enable/disable forward traffic DSCP tag.'
               dscp-forward-tag:
                  type: str
                  description: 'Forward traffic DSCP tag.'
               dscp-reverse:
                  type: str
                  description: 'Enable/disable reverse traffic DSCP tag.'
               dscp-reverse-tag:
                  type: str
                  description: 'Reverse traffic DSCP tag.'
               dst:
                  type: str
                  description: 'Destination address name.'
               dst-negate:
                  type: str
                  description: 'Enable/disable negation of destination address match.'
               dst6:
                  type: str
                  description: 'Destination address6 name.'
               end-port:
                  type: int
                  description: 'End destination port number.'
               gateway:
                  type: str
                  description: 'Enable/disable SD-WAN service gateway.'
               groups:
                  type: str
                  description: 'User groups.'
               health-check:
                  type: str
                  description: 'Health check.'
               hold-down-time:
                  type: int
                  description: 'Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).'
               id:
                  type: int
                  description: 'Priority rule ID (1 - 4000).'
               internet-service:
                  type: str
                  description: 'Enable/disable use of Internet service for application-based load balancing.'
               internet-service-ctrl:
                  type: array
                  suboptions:
                     type: int
               internet-service-ctrl-group:
                  type: str
                  description: 'Control-based Internet Service group list.'
               internet-service-custom:
                  type: str
                  description: 'Custom Internet service name list.'
               internet-service-custom-group:
                  type: str
                  description: 'Custom Internet Service group list.'
               internet-service-group:
                  type: str
                  description: 'Internet Service group list.'
               internet-service-id:
                  type: str
                  description: 'Internet service ID list.'
               jitter-weight:
                  type: int
                  description: 'Coefficient of jitter in the formula of custom-profile-1.'
               latency-weight:
                  type: int
                  description: 'Coefficient of latency in the formula of custom-profile-1.'
               link-cost-factor:
                  type: str
                  description: 'Link cost factor.'
               link-cost-threshold:
                  type: int
                  description: 'Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).'
               member:
                  type: str
                  description: 'Member sequence number.'
               mode:
                  type: str
                  description: 'Control how the priority rule sets the priority of interfaces in the SD-WAN.'
               name:
                  type: str
                  description: 'Priority rule name.'
               packet-loss-weight:
                  type: int
                  description: 'Coefficient of packet-loss in the formula of custom-profile-1.'
               priority-members:
                  type: str
                  description: 'Member sequence number list.'
               protocol:
                  type: int
                  description: 'Protocol number.'
               quality-link:
                  type: int
                  description: 'Quality grade.'
               route-tag:
                  type: int
                  description: 'IPv4 route map route-tag.'
               sla:
                  type: array
                  suboptions:
                     health-check:
                        type: str
                        description: 'Virtual WAN Link health-check.'
                     id:
                        type: int
                        description: 'SLA ID.'
               src:
                  type: str
                  description: 'Source address name.'
               src-negate:
                  type: str
                  description: 'Enable/disable negation of source address match.'
               src6:
                  type: str
                  description: 'Source address6 name.'
               start-port:
                  type: int
                  description: 'Start destination port number.'
               status:
                  type: str
                  description: 'Enable/disable SD-WAN service.'
               tos:
                  type: str
                  description: 'Type of service bit pattern.'
               tos-mask:
                  type: str
                  description: 'Type of service evaluated bits.'
               users:
                  type: str
                  description: 'User name.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service

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
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'wanprof',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'addr-mode': {
                            'type': 'string',
                            'enum': [
                                'ipv4',
                                'ipv6'
                            ]
                        },
                        'bandwidth-weight': {
                            'type': 'integer'
                        },
                        'default': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-forward-tag': {
                            'type': 'string'
                        },
                        'dscp-reverse': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-reverse-tag': {
                            'type': 'string'
                        },
                        'dst': {
                            'type': 'string'
                        },
                        'dst-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dst6': {
                            'type': 'string'
                        },
                        'end-port': {
                            'type': 'integer'
                        },
                        'gateway': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'health-check': {
                            'type': 'string'
                        },
                        'hold-down-time': {
                            'type': 'integer'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'internet-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'internet-service-ctrl': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'internet-service-ctrl-group': {
                            'type': 'string'
                        },
                        'internet-service-custom': {
                            'type': 'string'
                        },
                        'internet-service-custom-group': {
                            'type': 'string'
                        },
                        'internet-service-group': {
                            'type': 'string'
                        },
                        'internet-service-id': {
                            'type': 'string'
                        },
                        'jitter-weight': {
                            'type': 'integer'
                        },
                        'latency-weight': {
                            'type': 'integer'
                        },
                        'link-cost-factor': {
                            'type': 'string',
                            'enum': [
                                'latency',
                                'jitter',
                                'packet-loss',
                                'inbandwidth',
                                'outbandwidth',
                                'bibandwidth',
                                'custom-profile-1'
                            ]
                        },
                        'link-cost-threshold': {
                            'type': 'integer'
                        },
                        'member': {
                            'type': 'string'
                        },
                        'mode': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'manual',
                                'priority',
                                'sla',
                                'load-balance'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'packet-loss-weight': {
                            'type': 'integer'
                        },
                        'priority-members': {
                            'type': 'string'
                        },
                        'protocol': {
                            'type': 'integer'
                        },
                        'quality-link': {
                            'type': 'integer'
                        },
                        'route-tag': {
                            'type': 'integer'
                        },
                        'sla': {
                            'type': 'array',
                            'items': {
                                'health-check': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'src': {
                            'type': 'string'
                        },
                        'src-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'src6': {
                            'type': 'string'
                        },
                        'start-port': {
                            'type': 'integer'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tos': {
                            'type': 'string'
                        },
                        'tos-mask': {
                            'type': 'string'
                        },
                        'users': {
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
                                'addr-mode',
                                'bandwidth-weight',
                                'default',
                                'dscp-forward',
                                'dscp-forward-tag',
                                'dscp-reverse',
                                'dscp-reverse-tag',
                                'dst',
                                'dst-negate',
                                'dst6',
                                'end-port',
                                'gateway',
                                'groups',
                                'health-check',
                                'hold-down-time',
                                'id',
                                'internet-service',
                                'internet-service-ctrl',
                                'internet-service-ctrl-group',
                                'internet-service-custom',
                                'internet-service-custom-group',
                                'internet-service-group',
                                'internet-service-id',
                                'jitter-weight',
                                'latency-weight',
                                'link-cost-factor',
                                'link-cost-threshold',
                                'member',
                                'mode',
                                'name',
                                'packet-loss-weight',
                                'priority-members',
                                'protocol',
                                'quality-link',
                                'route-tag',
                                'src',
                                'src-negate',
                                'src6',
                                'start-port',
                                'status',
                                'tos',
                                'tos-mask',
                                'users'
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
    module = AnsibleModule(argument_spec = module_arg_spec,
                           supports_check_mode = False)
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
        fmgr.govern_response(module = module, results = response,
                             msg = 'Operation Finished',
                             ansible_facts = fmgr.construct_ansible_facts(
                                response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])

if __name__ == '__main__':
    main()