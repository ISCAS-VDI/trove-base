# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class AccountsView(object):

    def __init__(self, accounts_summary):
        self.accounts_summary = accounts_summary

    def data(self):
        return {'accounts': self.accounts_summary.accounts}


class AccountView(object):

    def __init__(self, account):
        self.account = account

    def data(self):
        return {
            'account': {
                'id': self.account.id,
                'instance_ids': self.account.instance_ids,
            }
        }
