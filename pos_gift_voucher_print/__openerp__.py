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
    'name': 'Print Gift voucher',
    'version':'1.0',
    'category' : 'Point Of Sale',
    'description': """

    """,
    'author':'VMCloud Solution',
    'website': 'http://vmcloudsolution.pe',
    'depends': ['pos_gift_voucher', 'posbox_proxy_backend'],
    'data': ['security/ir.model.access.csv',
             'pos_gift_voucher_print.xml',
             ],
    'qweb':[
        'static/src/xml/print.xml',
    ],
    'auto_install': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

