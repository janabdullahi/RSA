# -*- coding: utf-8 -*-
{
    'name': "Resident Service Module",

    'summary': "Manage resident profiles, enquiries, requests and community services efficiently",

    'description': """
        Resident Service Module
        ========================
    
        A customised Odoo module designed to support Resident Services Associates and residential property management teams in managing resident information and day-to-day community operations.

        The module provides a centralised platform for maintaining resident records and can be extended to support key resident-service processes, including resident communication, requests, enquiries, property information, and service management.

        The solution is inspired by the Build-to-Rent (BTR) and residential property management sector, where Resident Services Associates act as the primary point of contact for residents and combine customer service, hospitality, administration, and operational responsibilities.

        Key objectives:

        Centralise and manage resident information.
        
        Improve visibility of resident records and details.
        
        Support front-of-house and resident service operations.
        
        Provide a foundation for managing resident enquiries and requests.
        
        Reduce manual administrative work through Odoo automation.
        
        Create a scalable system that can be expanded with additional resident-service functionality.
        
        Improve the overall resident experience and support tenant retention.
    """,

    'author': "Hamed Jan",
    # 'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}

