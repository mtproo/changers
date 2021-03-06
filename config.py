PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000000"
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True,
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "man-bargashtam.proxy.orginal.hame.dostam.daran.fadat.co.uno.io"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "c9f96504e1e6ffe934f134baf7ca5255"

