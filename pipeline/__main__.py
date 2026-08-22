"""Allow `python -m pipeline <html>` to work as documented in main.py."""
from .main import main

raise SystemExit(main())