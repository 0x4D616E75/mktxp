# coding=utf8
## Copyright (c) 2020 Arseniy Kuznetsov
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.


from mktxp.datasource.base_ds import BaseDSProcessor

class CapsmanCapsMetricsDataSource:
    ''' Caps Metrics data provider
    '''             
    @staticmethod
    def metric_records(router_entry, *, metric_labels = None):
        if metric_labels is None:
            metric_labels = []                
        try:
            remote_caps_records = router_entry.api_connection.router_api().get_resource('/caps-man/remote-cap').get()
            return BaseDSProcessor.trimmed_records(router_entry, router_records = remote_caps_records, metric_labels = metric_labels)
        except Exception as exc:
            print(f'Error getting caps-man remote caps info from router{router_entry.router_name}@{router_entry.config_entry.hostname}: {exc}')
            return None


class CapsmanRegistrationsMetricsDataSource:
    ''' Capsman Registrations Metrics data provider
    '''             
    @staticmethod
    def metric_records(router_entry, *, metric_labels = None,  add_router_id = True):
        if metric_labels is None:
            metric_labels = []                
        try:
            registration_table_records = router_entry.api_connection.router_api().get_resource('/caps-man/registration-table').get()
            return BaseDSProcessor.trimmed_records(router_entry, router_records = registration_table_records, metric_labels = metric_labels, add_router_id = add_router_id)
        except Exception as exc:
            print(f'Error getting caps-man registration table info from router{router_entry.router_name}@{router_entry.config_entry.hostname}: {exc}')
            return None


class CapsmanInterfacesDatasource:
    ''' Data provider for CAPsMaN interfaces
    '''

    @staticmethod
    def metric_records(router_entry, *, metric_labels = None):
        if metric_labels is None:
            metric_labels = []                
        try:
            caps_interfaces = router_entry.api_connection.router_api().get_resource('/caps-man/interface').get()
            return BaseDSProcessor.trimmed_records(router_entry, router_records = caps_interfaces, metric_labels = metric_labels)
        except Exception as exc:
            print(f'Error getting caps-man interfaces info from router{router_entry.router_name}@{router_entry.config_entry.hostname}: {exc}')
            return None
