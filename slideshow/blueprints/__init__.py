from .core.views import bp as core_bp
from .user.views import bp as user_bp
from .display.views import bp as display_bp

all_blueprints = [core_bp, user_bp, display_bp]
