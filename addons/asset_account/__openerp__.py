﻿# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 CodUP (<http://codup.com>).
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
    'name': 'Assets & Finance',
    'version': '1.0',
    'summary': 'Integrate Asset and Accounting',
    'description': """
Integrate financial and maintenance asset management.
===========================

This module allows use the same Assets for maintenance and accounting purposes.
Integration take in account assumption that maintenable asset is physical asset
and must have depreciation. Also vice versa, if asset have depreciation then
it must be maintenable. So, when you create asset for accounting, it automaticaly
available for maintenance. And when you create asset for maintenance, it automaticaly
available for finance.
Keep one entity in one place for escape mistakes!
    """,
    'author': 'CodUP',
    'website': 'http://codup.com',
    'category': 'Enterprise Asset Management',
    'sequence': 0,
    'depends': ['asset','account_asset'],
    'data': ['asset_view.xml'],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: