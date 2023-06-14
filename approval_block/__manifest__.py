{
    'name': 'ApprovalBlock',
    'version': '16.0.0.1.0',
    'sequence': 4.0,
    'summary': 'Approval Block',
    'description': """
Approval Block
====================
 Application for  creating Approval Blocks  
    """,
    'category': 'Purchase/Approval_Block',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/block_records_demo.xml',
        'views/approval_block_record_view.xml',
        'views/purchase_order_view.xml',
    ],
    'application': True,
    'installable': True,
    'autoinstall': True,
    'license': 'LGPL-3',
}