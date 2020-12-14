env = 'dev'
if env == 'dev':
    from djangoProject.settings.settings_dev import *
else:
    from djangoProject.settings.settings_prod import *