"""Load information about futures contracts, in particular, the multipliers.
"""
__copyright__ = "Copyright (C) 2021  Martin Blais"
__license__ = "GNU GPLv2"

from decimal import Decimal
from typing import Dict, Tuple


# NOTE(blais): If you need a CME or CBOE product that is not here, please send
# me a patch to add in the multiplier. These just happen to be the ones I've
# needed in the past.


# Standard equity option contract size.
# TODO(blais): Rename to EQUITY_OPTION_CSIZE
OPTION_CONTRACT_SIZE = Decimal(100)


# Multipliers for CME products.
CME_MULTIPLIERS = {name: Decimal(value) for name, value in {
    # Equity indices
    '/ES'     : 50,
    '/MES'    : 5,
    '/NQ'     : 20,
    '/MNQ'    : 2,
    '/RTY'    : 50,
    '/M2K'    : 5,
    '/YM'     : 5,
    '/MYM'    : '0.5',

    # Volatility
    '/VX'     : 1000,
    '/VXM'    : 100,

    # FX
    '/6A'     : 100_000,
    '/M6A'    : 10_000,
    '/6C'     : 100_000,
    '/6B'     : 62_500,
    '/M6B'    : 6250,
    '/6E'     : 125_000,
    '/M6E'    : 12_500,
    '/6J'     : 12_500_000,

    # Energy
    '/CL'     : 1000,
    '/QM'     : 500,
    '/MCL'    : 100,
    '/NG'     : 10_000,
    '/QG'     : 2500,

    # Metals
    '/GC'     : 100,
    '/MGC'    : 10,
    '/SI'     : 5000,
    '/SIL'    : 1000,
    '/HG'     : 25_000,
    '/QC'     : 12_500,
    '/PA'     : 100,
    '/PL'     : 50,

    # Rates
    '/ZQ'     : 4167,
    '/GE'     : 2500,
    '/ZT'     : 2000,
    '/ZF'     : 1000,
    '/ZN'     : 1000,
    '/ZB'     : 1000,

    # Agricultural
    '/ZC'     : 50,
    '/XC'     : 5,
    '/ZS'     : 50,
    '/XK'     : 5,
    '/ZW'     : 50,
    '/XW'     : 5,

    # Livestock
    '/HE'     : 400,
    '/LE'     : 400,

    # Crypto/Digital Assets
    '/BTC'    : 5,
    '/MBT'    : '0.1',
}.items()}

# Multipliers for CBOE products.
CBOE_MULTIPLIERS = {name: Decimal(value) for name, value in {
    # Indices
    'SPX'     : 100,
    'NDX'     : 100,
    'RUT'     : 100,
    'DJI'     : 100,

    # Volatility
    'VIX'     : 100,
    'RVX'     : 1000,
    'VXN'     : 1000,
    'VXD'     : 1000,
}.items()}

# Multipliers for SmallExchange products.
SMALLEXCHANGE_MULTIPLIERS = {name: Decimal(value) for name, value in {
    '/S10Y'   : 100,
    '/S2Y'    : 100,
    '/S30Y'   : 100,
    '/S420'   : 100,
    '/SFX'    : 100,
    '/SM75'   : 100,
    '/SMO'    : 100,
    '/SPRE'   : 100,
    '/STIX'   : 100,
}.items()}


# Merge all the mappings.
MULTIPLIERS = {name: multiplier
               for mulmap in [CME_MULTIPLIERS,
                              CBOE_MULTIPLIERS,
                              SMALLEXCHANGE_MULTIPLIERS]
               for name, multiplier in mulmap.items()}
