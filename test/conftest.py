from webtools import settings
from webtools.tools import join

import os

settings.dir_path = join(os.path.dirname(os.path.realpath(__file__)), "data")
settings.html_path = join(os.path.dirname(os.path.realpath(__file__)), "_html")
settings.template_path = join(os.path.dirname(os.path.realpath(__file__)), "data")
settings.url = "http://example.com"
settings.repo = "DefElement/website-build-tools"
