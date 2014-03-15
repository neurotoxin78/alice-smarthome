#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib2 import urlparse

def asciify_url(url, force_quote=False):
    r"""Attempts to make a unicode url usuable with ``urllib/urllib2``.

    More specifically, it attempts to convert the unicode object ``url``,
    which is meant to represent a IRI, to an unicode object that,
    containing only ASCII characters, is a valid URI. This involves:

        * IDNA/Puny-encoding the domain name.
        * UTF8-quoting the path and querystring parts.

    See also RFC 3987.
    """
    assert type(url) == unicode

    parts = urlparse.urlsplit(url)
    if not parts.scheme or not parts.netloc:
        # apparently not an url
        return url

    # idna-encode domain
    hostname = parts.hostname.encode('idna')

    # UTF8-quote the other parts. We check each part individually if
    # if needs to be quoted - that should catch some additional user
    # errors, say for example an umlaut in the username even though
    # the path *is* already quoted.
    def quote(s, safe):
        s = s or ''
        # Triggers on non-ascii characters - another option would be:
        #     urllib.quote(s.replace('%', '')) != s.replace('%', '')
        # which would trigger on all %-characters, e.g. "&".
        if s.encode('ascii', 'replace') != s or force_quote:
            return urllib.quote(s.encode('utf8'), safe=safe)
        return s
    username = quote(parts.username, '')
    password = quote(parts.password, safe='')
    path = quote(parts.path, safe='/')
    query = quote(parts.query, safe='&=')

    # put everything back together
    netloc = hostname
    if username or password:
        netloc = '@' + netloc
        if password:
            netloc = ':' + password + netloc
        netloc = username + netloc
    if parts.port:
        netloc += ':' + str(parts.port)
    return urlparse.urlunsplit([
        parts.scheme, netloc, path, query, parts.fragment])
