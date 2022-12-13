from .models import Restaurant, MenuItem
from .config import config

session, Base = config()