#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def _key_auth_str(username, key):
    """Returns an ApiKey Auth string."""
    return 'ApiKey ' + '%s:%s' % (username, key)


class TastyPieAuth(requests.auth.AuthBase):
    """A small wrapper class to provide Client with ApiKey style auth."""
    def __init__(self, username, key):
        self.username = username
        self.key = key

    def __call__(self, r):
        r.headers['Authorization'] = _key_auth_str(self.username, self.key)
        return r
