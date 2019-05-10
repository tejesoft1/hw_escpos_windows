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

from datetime import datetime
from openerp.osv import fields, osv

class posbox_proxy_backend(osv.osv):
    _name = 'posbox.proxy.backend'

    _columns = {
        'name': fields.char('Model name', select=1, help="Model name, for example: sale.order", required=True),
        'user_id': fields.many2one('res.users', 'User', help="If you set a user will have higher priority"),
        'value_ip': fields.char('Value IP', help='The hostname or ip address of the hardware proxy', size=45),
    }

    def get_proxy_url(self, cr, uid, name, context=None):
        proxy_backend_ids = self.search(cr, uid, [('name', '=', name), '|', ('user_id', '=', uid), ('user_id', '=', False)], context=context, order='user_id')
        proxy_url = 'http://localhost:8069'
        for proxy_backend_obj in self.browse(cr, uid, proxy_backend_ids, context=context):
            if proxy_backend_obj.user_id.id == uid:
                proxy_url = proxy_backend_obj.value_ip
                break
            else:
                proxy_url = proxy_backend_obj.value_ip
        return proxy_url

    def set_value_space(self, value, space=7, align='right'):
        if align == 'left':
            val_str = str(value) + ' ' * space
            result = val_str[:space]
        else:
            val_str = ' ' * space + str(value)
            result = val_str[-space:]
        return result

    def get_date_formats(self, cr, uid, context=None):
        lang = self.pool.get('res.users').browse(cr, uid, uid).lang
        res_lang = self.pool.get('res.lang')
        lang_params = {}
        if lang:
            ids = res_lang.search(cr, uid, [("code", "=", lang)])
            if ids:
                lang_params = res_lang.read(cr, uid, ids[0], ["date_format", "time_format"])
        format_date = lang_params.get("date_format", '%m/%d/%Y').encode('utf-8')
        format_time = lang_params.get("time_format", '%H:%M:%S').encode('utf-8')
        return format_date, format_time