#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
    This file will contain all the exceptions that will be raised by cli
    client.
    Ideally, CLI should only raise and catch these exceptions.
"""

# Do NOT modify or remove this copyright and confidentiality notice

# Copyright 2015 Seagate Technology LLC or one of its affiliates.
#
# The code contained herein is CONFIDENTIAL to Seagate Technology LLC.
# Portions may also be trade secret. Any use, duplication, derivation,
# distribution or disclosure of this code, for any reason, not expressly
# authorized in writing by Seagate Technology LLC is prohibited.
# All rights are expressly reserved by Seagate Technology LLC.

# Import system Modules

# Import Local Modules


class BaseError(Exception):
    """
        Parent class for the cli error classes
    """
    err = "Internal Error"
    desc = "Could not execute the command"

    def __init__(self, err=None, desc=None):
        super(BaseError, self).__init__()
        self.err = err or self.err
        self.desc = desc or self.desc


class CommandTerminated(BaseError):
    """
        This error will be raised when some command is terminated during
        the processing
    """
    err = "Command Terminated"
    desc = "Command is cancelled"

    def __init__(self, err=None, desc=None):
        super(CommandTerminated, self).__init__(err, desc)


class InvalidResponse(BaseError):
    """
        This error will be raised when an invalid response
        message is received for any of the cli commands.
    """
    err = "Invalid response"
    desc = "Invalid response message received " \
           "or the response message could not be parsed correctly"

    def __init__(self, err=None, desc=None):
        super(InvalidResponse, self).__init__(err, desc)


class InternalError(BaseError):
    """
    This error is raised by CLI for all unknown internal errors
    """

    err = "Internal Error"
    desc = 'An Internal error has occurred, unable to complete command.'

    def __init__(self, err=None, desc=None):
        super(InternalError, self).__init__(err, desc)
