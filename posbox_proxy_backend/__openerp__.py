# -*- coding: utf-8 -*-

##############################################################################
#
#    This module copyright :
#        (c) 2015 VMCloud Solution (http://vmcloudsolution.pe)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Posbox proxy backend',
    'version':'1.0',
    'category' : 'Hardware Drivers',
    'description': """
        For printered from the backend
    """,
    'author':'VMCloud Solution',
    'website': 'http://vmcloudsolution.pe',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'posbox_proxy_device.xml',
             'posbox_proxy_device_data.xml'],
    'auto_install': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

