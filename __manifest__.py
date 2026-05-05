{
    'name': "To do",
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base','mail'],
    'author': "Ahmed",
    'category': 'Category',
    'description': """
    Description text
    """,
# data files always loaded at installation
    'data': ['security/ir.model.access.csv',
             "views/base_menu.xml",
             "views/to_do_view.xml",
             "views/estimated_time.xml",
             "reports/todo_reports.xml",
             ],
    # data files containing optionally loaded demonstration data
    'application': True,
}