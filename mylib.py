"""Utility module for performing simple actions with logging."""

import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

def do_something():
    """Log an info message indicating that an action is performed."""
    logger.info('Doing something')
