#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Cisco and/or its affiliates.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for nxos_telemetry
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: nxos_telemetry
version_added: 2.9
short_description: 'Telemetry Monitoring Service (TMS) configuration'
description: 'Manages Telemetry Monitoring Service (TMS) configuration'
author: Mike Wiebe (@mikewiebe)
notes:
  - 'Supported on N9k Version 7.0(3)I7(5) and later.'
options:
  config:
    description: The provided configuration
    type: dict
    suboptions:
      certificate:
        type: dict
        description:
          - Certificate SSL/TLS and hostname values.
          - Value must be a dict defining values for keys (key and hostname).
        suboptions:
          key:
            description:
              - Certificate key
            type: str
          hostname:
            description:
              - Certificate hostname
            type: str
      compression:
        type: str
        description:
          - Destination profile compression method.
        choices:
          - gzip
      source_interface:
        type: str
        description:
          - Destination profile source interface.
          - Valid value is a str representing the source interface name.
      vrf:
        type: str
        description:
          - Destination profile vrf.
          - Valid value is a str representing the vrf name.
      destination_groups:
        type: list
        description:
          - List of telemetry destination groups.
        suboptions:
          id:
            type: int
            description:
              - Destination group identifier.
              - Value must be a int representing the destination group identifier.
          destination:
            type: dict
            description:
              - Group destination ipv4, port, protocol and encoding values.
              - Value must be a dict defining values for keys (ip, port, protocol, encoding).
            suboptions:
              ip:
                type: str
                description:
                  - Destination group IP address.
              port:
                type: int
                description:
                  - Destination group port number.
              protocol:
                type: str
                description:
                  - Destination group protocol.
                choices:
                  - HTTP
                  - TCP
                  - UDP
                  - gRPC
              encoding:
                type: str
                description:
                  - Destination group encoding.
                choices:
                  - GPB
                  - JSON
      sensor_groups:
        type: list
        description:
          - List of telemetry sensor groups.
        suboptions:
          id:
            type: int
            description:
              - Sensor group identifier.
              - Value must be a int representing the sensor group identifier.
          data_source:
            type: str
            description:
              - Telemetry data source.
            choices:
              - NX-API
              - DME
              - YANG
          path:
            type: dict
            description:
              - Telemetry sensor path.
              - Value must be a dict defining values for keys (name, depth, filter_condition, query_condition).
              - Mandatory Keys (name)
              - Optional Keys  (depth, filter_condition, query_condition)
            suboptions:
              name:
                type: str
                description:
                  - Sensor group path name.
              depth:
                type: str
                description:
                  - Sensor group depth.
              filter_condition:
                type: str
                description:
                  - Sensor group filter condition.
              query_condition:
                type: str
                description:
                  - Sensor group query condition.
      subscriptions:
        type: list
        description:
          - List of telemetry subscriptions.
        suboptions:
          id:
            type: int
            description:
              - Subscription identifier.
              - Value must be a int representing the subscription identifier.
          destination_group:
            type: int
            description:
              - Associated destination group.
          sensor_group:
            type: dict
            description:
              - Associated sensor group.
              - Value must be a dict defining values for keys (id, sample_interval).
            suboptions:
              id:
                type: int
                description:
                  - Associated sensor group id.
              sample_interval:
                type: int
                description:
                  - Associated sensor group id sample interval.

  state:
    description:
    - Final configuration state
    type: str
    choices:
    - merged
    - replaced
    - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted
# This action will delete all telemetry configuration on the device

- name: Delete Telemetry Configuration
  nxos_telemetry:
    state: deleted


# Using merged
# This action will merge telemetry configuration defined in the playbook with
# telemetry configuration that is already on the device.

- name: Merge Telemetry Configuration
  nxos_telemetry:
    config:
      certificate:
        key: /bootflash/server.key
        hostname: localhost
      compression: gzip
      source_interface: Ethernet1/1
      vrf: management
      destination_groups:
        - id: 2
          destination:
            ip: 192.168.0.2
            port: 50001
            protocol: gPRC
            encoding: GPB
        - id: 55
          destination:
            ip: 192.168.0.55
            port: 60001
            protocol: gPRC
            encoding: GPB
      sensor_groups:
        - id: 1
          data_source: NX-API
          path:
            name: '"show lldp neighbors detail"'
            depth: 0
        - id: 55
          data_source: DME
          path:
            name: 'sys/ch'
            depth: unbounded
            filter_condition: 'ne(eqptFt.operSt,"ok")'
      subscriptions:
        - id: 5
          destination_group: 55
          sensor_group:
            id: 1
            sample_interval: 1000
        - id: 6
          destination_group: 2
          sensor_group:
            id: 55
            sample_interval: 2000
    state: merged


# Using replaced
# This action will replace telemetry configuration on the device with the
# telmetry configuration defined in the playbook.

- name: Override Telemetry Configuration
  nxos_telemetry:
    config:
      certificate:
        key: /bootflash/server.key
        hostname: localhost
      compression: gzip
      source_interface: Ethernet1/1
      vrf: management
      destination_groups:
        - id: 2
          destination:
            ip: 192.168.0.2
            port: 50001
            protocol: gPRC
            encoding: GPB
      subscriptions:
        - id: 5
          destination_group: 55
    state: replaced


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.telemetry.telemetry import (
    TelemetryArgs,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.telemetry.telemetry import (
    Telemetry,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=TelemetryArgs.argument_spec, supports_check_mode=True
    )

    result = Telemetry(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
