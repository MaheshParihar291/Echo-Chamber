#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echo_chamber.settings')

    # If running 'runserver' and no port is specified, use PORT from env
    if 'runserver' in sys.argv:
        port_specified = any(arg.isdigit() or ':' in arg for arg in sys.argv[2:])
        if not port_specified:
            port = os.environ.get('PORT')
            if port:
                sys.argv.append(port)
                
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
