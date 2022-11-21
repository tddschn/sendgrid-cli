#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-11-21
Purpose: sendgrid CLI
"""

import argparse
import sys
from . import __version__


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='sendgrid CLI',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='Email body is read from stdin, supply your API key with SENDGRID_API_KEY environment variable',
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'%(prog)s {__version__}',
    )

    parser.add_argument(
        '-t', '--to-emails', help='To emails', metavar='str', type=str, nargs='+'
    )

    parser.add_argument(
        '-f',
        '--from-email',
        help='From email EMAIL',
        metavar='str',
        type=str,
    )

    parser.add_argument(
        '-n', '--from-name', help='From name NAME', metavar='str', type=str
    )

    parser.add_argument(
        '-s',
        '--subject',
        help='Subject',
        metavar='str',
        type=str,
    )

    parser.add_argument(
        '-H', '--html', help='send as html instead of plain text', action='store_true'
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    stdin_content = sys.stdin.read()
    import os

    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    if not sendgrid_api_key:
        print('SENDGRID_API_KEY environment variable is not set')
        sys.exit(1)
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    content_kwarg = {
        'html_content' if args.html else 'plain_text_content': stdin_content
    }

    message = Mail(
        from_email=(args.from_email, args.from_name),
        to_emails=args.to_emails,
        subject=args.subject,
        **content_kwarg,
    )

    sg = SendGridAPIClient(sendgrid_api_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == '__main__':
    main()
