## -*- coding: utf-8 -*-

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


software_names = [SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value] 

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)



BOT_NAME = 'covid'

SPIDER_MODULES = ['covid.spiders']
NEWSPIDER_MODULE = 'covid.spiders'


USER_AGENT = user_agent_rotator.get_random_user_agent()

ROBOTSTXT_OBEY = False


FEED_EXPORT_FIELDS = []
