"""Product mapping from options to futures.

This is derived from the CME database.
"""
__copyright__ = "Copyright (C) 2021  Martin Blais"
__license__ = "GNU GPLv2"

# Mapping of (option-product, future-product).
PRODUCTS = \
{'12C': 'QC2',
 '12K': 'KNS',
 '12S': 'QS2',
 '12W': 'QW2',
 '1AD': '6A',
 '1BP': '6B',
 '1CD': '6C',
 '1E': 'RP',
 '1EU': '6E',
 '1H': 'RY',
 '1I': 'RF',
 '1JY': '6J',
 '1M': '6M',
 '1N': '6Z',
 '1N5': 'N1B',
 '1R': '6L',
 '1SF': '6S',
 '1Z': '6N',
 '2AD': '6A',
 '2BP': '6B',
 '2CD': '6C',
 '2E': 'RP',
 '2EU': '6E',
 '2H': 'RY',
 '2I': 'RF',
 '2JY': '6J',
 '2M': '6M',
 '2N': '6Z',
 '2R': '6L',
 '2SF': '6S',
 '2Z': '6N',
 '3AD': '6A',
 '3BP': '6B',
 '3CD': '6C',
 '3E': 'RP',
 '3EU': '6E',
 '3H': 'RY',
 '3I': 'RF',
 '3JY': '6J',
 '3M': '6M',
 '3N': '6Z',
 '3R': '6L',
 '3SF': '6S',
 '3Z': '6N',
 '4AD': '6A',
 '4BP': '6B',
 '4CD': '6C',
 '4E': 'RP',
 '4EU': '6E',
 '4H': 'RY',
 '4I': 'RF',
 '4JY': '6J',
 '4M': '6M',
 '4N': '6Z',
 '4R': '6L',
 '4SF': '6S',
 '4Z': '6N',
 '5AD': '6A',
 '5BP': '6B',
 '5CD': '6C',
 '5EU': '6E',
 '5JY': '6J',
 '5M': '6M',
 '5SF': '6S',
 '6M': '6M',
 '6N': '6N',
 '6OA': '28A',
 '6OO': 'OO6',
 '6R': '6R',
 '6R1': '6R',
 '6R2': '6R',
 '6R3': '6R',
 '6R4': '6R',
 '6Y': '8SS',
 '7B': 'A6A',
 '7C': '5A',
 '7HO': 'B7H',
 '7M': '4A',
 '7Z': '3A',
 '9AV': 'D3L',
 '9B': 'A6B',
 '9C': '2A',
 '9D': '5B',
 '9L': '4B',
 '9Y': '3B',
 'A30': 'AUJ',
 'A3U': 'GZ',
 'A3W': 'AHL',
 'A3Y': 'ARE',
 'A4D': 'U8R',
 'A4H': 'B0',
 'A4I': 'A7Q',
 'A4J': 'AC0',
 'A4K': 'AD0',
 'A6E': 'A8T',
 'A6F': '8S',
 'A6I': 'H8U',
 'A6J': 'U8P',
 'A8H': 'SE',
 'A9T': 'K3L',
 'A9U': 'T3L',
 'AA': 'BD',
 'AAH': 'DCB',
 'AAO': 'CSX',
 'AB': 'BF',
 'ABV': 'ABY',
 'AC': 'BJ',
 'AC5': 'UA',
 'ADU': '6A',
 'AE7': 'HH',
 'AF7': 'AGX',
 'AFG': 'MFB',
 'AFZ': 'AAK',
 'AG2': 'CG9',
 'AG5': 'HH8',
 'AG7': 'HH6',
 'AIC': 'DSA',
 'AJI': 'BAS',
 'AJN': 'AB3',
 'ALO': 'AUP',
 'AM': 'BM',
 'AM2': 'SGB',
 'AN2': 'AKS',
 'AOT': 'AZ9',
 'APE': 'AR8',
 'AQ6': 'UV',
 'ARF': 'RB',
 'ASG': 'AL6',
 'ATX': 'MPX',
 'AWM': 'CV',
 'AWZ': 'CX',
 'AZ': 'BQ',
 'AZB': 'ZJY',
 'AZC': 'ZK',
 'AZM': 'AZL',
 'B7A': 'CA2',
 'BA': 'CY',
 'BCE': 'BCX',
 'BCO': 'BOO',
 'BE': 'BZ',
 'BLK': 'BLK',
 'BPC': 'BPS',
 'BQP': 'BQS',
 'BR': '6L',
 'BSO': 'BCF',
 'BTC': 'BTC',
 'BW1': 'BZ',
 'BW2': 'BZ',
 'BW3': 'BZ',
 'BW4': 'BZ',
 'BW5': 'BZ',
 'BWO': 'BWF',
 'BZO': 'BZ',
 'C01': 'CL',
 'C02': 'CL',
 'C07': 'CL',
 'C08': 'CL',
 'C09': 'CL',
 'C10': 'CL',
 'C13': 'CL',
 'C14': 'CL',
 'C15': 'CL',
 'C16': 'CL',
 'C17': 'CL',
 'C18': 'CL',
 'C19': 'CL',
 'C20': 'CL',
 'C21': 'CL',
 'C22': 'CL',
 'C23': 'CL',
 'C24': 'CL',
 'C25': 'CL',
 'C26': 'CL',
 'C27': 'CL',
 'C30': 'CL',
 'C31': 'CL',
 'CAP': 'HGS',
 'CAU': '6C',
 'CB': 'CB',
 'CCO': 'CC5',
 'CE1': '1CE',
 'CE2': '2CE',
 'CE3': '3CE',
 'CE6': '6CE',
 'CHU': '6S',
 'CHY': 'HCY',
 'CK3': 'C3S',
 'CKO': 'CZK',
 'CKZ': 'KZS',
 'CLR': 'CLD',
 'CPR': 'A8K',
 'CSA': 'E9X',
 'CSC': 'CSC',
 'CVR': 'CU',
 'CWZ': 'ZWC',
 'CZ6': 'QC6',
 'CZ7': 'QC7',
 'CZ8': 'QC8',
 'CZ9': 'QCC',
 'CZC': 'QC3',
 'CZL': 'QO2',
 'CZM': 'QM2',
 'CZS': 'SQ2',
 'CZW': 'QW3',
 'DAH': 'DCD',
 'DAP': 'AA5',
 'DBP': 'AUB',
 'DC': 'DC',
 'DNM': 'CAY',
 'DRD': 'ODO',
 'DTM': 'CQ',
 'DY': 'DY',
 'E01': 'GE',
 'E02': 'GE',
 'E03': 'GE',
 'E04': 'GE',
 'E05': 'GE',
 'E1A': 'ES',
 'E1C': 'ES',
 'E21': 'GE',
 'E22': 'GE',
 'E23': 'GE',
 'E24': 'GE',
 'E25': 'GE',
 'E2A': 'ES',
 'E2C': 'ES',
 'E31': 'GE',
 'E32': 'GE',
 'E33': 'GE',
 'E34': 'GE',
 'E35': 'GE',
 'E3A': 'ES',
 'E3C': 'ES',
 'E4A': 'ES',
 'E4C': 'ES',
 'E5A': 'ES',
 'E5C': 'ES',
 'E5O': 'AE5',
 'ECZ': 'ECK',
 'EFB': 'AUH',
 'EHU': 'EHF',
 'EMD': 'EMD',
 'EPL': 'EPZ',
 'ES': 'ES',
 'EUU': '6E',
 'EV': 'SP',
 'EV1': 'SP',
 'EV2': 'SP',
 'EV3': 'SP',
 'EV4': 'SP',
 'EW': 'ES',
 'EW1': 'ES',
 'EW2': 'ES',
 'EW3': 'ES',
 'EW4': 'ES',
 'EX': 'MES',
 'EX1': 'MES',
 'EX2': 'MES',
 'EX3': 'MES',
 'EX4': 'MES',
 'EYC': 'ES',
 'EYM': 'YM',
 'F2C': 'F2M',
 'F2Q': 'F2B',
 'F4C': 'F4M',
 'F4Q': 'F4B',
 'F8': 'BG',
 'FAY': 'GHY',
 'FB': 'GK',
 'FC': 'GMY',
 'FFO': 'AFF',
 'FLO': 'FLP',
 'FM': 'AGF',
 'G10': 'G44',
 'G3B': 'BH9',
 'G4X': 'G8X',
 'G6B': 'H7Y',
 'GBU': '6B',
 'GCE': 'T7K',
 'GDK': 'GDK',
 'GE': 'GE',
 'GE0': 'GE',
 'GE2': 'GE',
 'GE3': 'GE',
 'GE4': 'GE',
 'GE5': 'GE',
 'GF': 'GF',
 'GNF': 'GNF',
 'GUL': 'ALY',
 'GVR': 'AGE',
 'GXA': 'GUS',
 'GXB': 'GWS',
 'GXC': 'GYS',
 'GXM': 'GVS',
 'GXZ': 'GLS',
 'H1E': 'HG',
 'H1X': 'H1X',
 'H2E': 'HG',
 'H3E': 'HG',
 'H3X': 'H3X',
 'H4E': 'HG',
 'H4X': 'H4X',
 'H5E': 'HG',
 'H5X': 'H5X',
 'H7X': 'H7X',
 'HE': 'HE',
 'HFO': 'HUF',
 'HIO': 'HIL',
 'HRO': 'HRC',
 'HTO': 'HTT',
 'HXE': 'HG',
 'IAY': 'DGY',
 'IB': 'ADJ',
 'ICD': 'CL',
 'IE': 'ADE',
 'ILS': 'ILS',
 'IM': 'DMA',
 'INE': 'AU6',
 'IS2': 'ILS',
 'IS3': 'ILS',
 'IS4': 'ILS',
 'IS5': 'ILS',
 'IZ': 'MDZ',
 'JA5': 'JA',
 'JAC': 'AJ2',
 'JDA': 'AZ9',
 'JFO': 'JKM',
 'JHA': 'ISA',
 'JKO': 'JKM',
 'JOA': 'AL1',
 'JPU': '6J',
 'KC6': 'K6S',
 'KCR': 'CKS',
 'KCW': 'QKC',
 'KDB': 'NG',
 'KR1': 'KRW',
 'KR2': 'KRW',
 'KR3': 'KRW',
 'KR4': 'KRW',
 'KRW': 'KRW',
 'KWE': 'KE',
 'KZC': 'KC7',
 'L0A': 'Q02',
 'L0B': 'Q04',
 'L0C': 'Q06',
 'LB': 'HO',
 'LBS': 'LBS',
 'LCE': 'CL',
 'LE': 'LE',
 'LM1': 'CL',
 'LM2': 'CL',
 'LM3': 'CL',
 'LM4': 'CL',
 'LM5': 'CL',
 'LN1': 'NG',
 'LN2': 'NG',
 'LN3': 'NG',
 'LN4': 'NG',
 'LN5': 'NG',
 'LNE': 'NG',
 'LO': 'CL',
 'LO1': 'CL',
 'LO2': 'CL',
 'LO3': 'CL',
 'LO4': 'CL',
 'LO5': 'CL',
 'LRO': 'LLR',
 'MA1': '6A',
 'MA2': '6A',
 'MA3': '6A',
 'MA4': '6A',
 'MA5': '6A',
 'MB1': '6B',
 'MB2': '6B',
 'MB3': '6B',
 'MB4': '6B',
 'MB5': '6B',
 'MC3': 'QM3',
 'MC4': 'QM4',
 'MC5': 'QM5',
 'MC6': 'QM6',
 'MCW': 'MCX',
 'MD1': '6C',
 'MD2': '6C',
 'MD3': '6C',
 'MD4': '6C',
 'MD5': '6C',
 'ME3': 'EMD',
 'MES': 'MES',
 'MFO': 'MFF',
 'MFY': 'RLS',
 'MJ1': '6J',
 'MJ2': '6J',
 'MJ3': '6J',
 'MJ4': '6J',
 'MJ5': '6J',
 'MKW': 'WMK',
 'MNQ': 'MNQ',
 'MO1': '6E',
 'MO2': '6E',
 'MO3': '6E',
 'MO4': '6E',
 'MO5': '6E',
 'MQ1': 'MNQ',
 'MQ2': 'MNQ',
 'MQ3': 'MNQ',
 'MQ4': 'MNQ',
 'MQE': 'MNQ',
 'MTC': 'CLP',
 'MTO': 'MTF',
 'NB9': 'N9L',
 'NC3': 'QO3',
 'NC4': 'QO4',
 'NC5': 'QO5',
 'NEG': 'NSS',
 'NKW': 'NIY',
 'NKY': 'NIY',
 'NQ': 'NQ',
 'NVP': 'AEZ',
 'NWE': 'UN',
 'OB': 'RB',
 'OC6': 'QO6',
 'OCD': 'ZC',
 'ODB': 'BB',
 'OE1': 'KE',
 'OE2': 'KE',
 'OE3': 'KE',
 'OE4': 'KE',
 'OE5': 'KE',
 'OEA': '7EM',
 'OEH': 'EH',
 'OG': 'GC',
 'OG1': 'GC',
 'OG2': 'GC',
 'OG3': 'GC',
 'OG4': 'GC',
 'OG5': 'GC',
 'OH': 'HO',
 'OKE': 'KE',
 'OLD': 'ZL',
 'OMD': 'ZM',
 'ON': 'NG',
 'ON1': 'NG',
 'ON2': 'NG',
 'ON3': 'NG',
 'ON4': 'NG',
 'OQE': 'OQD',
 'OSD': 'ZS',
 'OSX': 'BZ',
 'OTN': 'TN',
 'OUA': 'AB3',
 'OUB': 'UB',
 'OWD': 'ZW',
 'OYA': 'AH3',
 'OYM': 'YM',
 'OZB': 'ZB',
 'OZC': 'ZC',
 'OZF': 'ZF',
 'OZL': 'ZL',
 'OZM': 'ZM',
 'OZN': 'ZN',
 'OZO': 'ZO',
 'OZQ': 'ZQ',
 'OZR': 'ZR',
 'OZS': 'ZS',
 'OZT': 'ZT',
 'OZW': 'ZW',
 'PAO': 'PA',
 'PDA': 'SDD',
 'PLZ': 'PLN',
 'PMA': 'AL1',
 'PO': 'PL',
 'POO': 'CPO',
 'POX': 'CPV',
 'PRK': 'PRK',
 'PRT': 'SRT',
 'Q1A': 'NQ',
 'Q1C': 'NQ',
 'Q2A': 'NQ',
 'Q2C': 'NQ',
 'Q3A': 'NQ',
 'Q3C': 'NQ',
 'Q4A': 'NQ',
 'Q4C': 'NQ',
 'Q5A': 'NQ',
 'Q5C': 'NQ',
 'QN1': 'NQ',
 'QN2': 'NQ',
 'QN3': 'NQ',
 'QN4': 'NQ',
 'QNE': 'NQ',
 'R1E': 'RTY',
 'R2E': 'RTY',
 'R3E': 'RTY',
 'R4E': 'RTY',
 'RA': 'RLX',
 'RB1': 'RMB',
 'RB2': 'RMB',
 'RB3': 'RMB',
 'RB4': 'RMB',
 'RBC': 'RBB',
 'RE1': 'RME',
 'RE2': 'RME',
 'RE3': 'RME',
 'RE4': 'RME',
 'RF': 'RF',
 'RGE': 'EXR',
 'RGX': 'RGI',
 'RMB': 'RMB',
 'RME': 'RME',
 'RO': '6Z',
 'RP': 'RP',
 'RTM': 'RTY',
 'RTO': 'RTY',
 'RXY': 'ZXY',
 'RY': 'RY',
 'S0': 'SR3',
 'S01': 'SR3',
 'S03': 'SR3',
 'S04': 'SR3',
 'S1A': 'SP',
 'S1C': 'SP',
 'S2': 'SR3',
 'S21': 'SR3',
 'S23': 'SR3',
 'S24': 'SR3',
 'S2A': 'SP',
 'S2C': 'SP',
 'S3': 'SR3',
 'S31': 'SR3',
 'S33': 'SR3',
 'S34': 'SR3',
 'S3A': 'SP',
 'S3C': 'SP',
 'S4': 'SR3',
 'S4A': 'SP',
 'S4C': 'SP',
 'S5': 'SR3',
 'S5A': 'SP',
 'S5C': 'SP',
 'SC7': 'S7C',
 'SCO': 'SF3',
 'SMC': 'SMC',
 'SO': 'SI',
 'SO1': 'SI',
 'SO2': 'SI',
 'SO3': 'SI',
 'SO4': 'SI',
 'SO5': 'SI',
 'SP': 'SP',
 'SPO': 'SPX',
 'SR1': 'SR1',
 'SR3': 'SR3',
 'SSO': 'SSW',
 'SWO': 'LSW',
 'SZ0': 'QS0',
 'SZ1': 'QS1',
 'SZ3': 'QS3',
 'SZ4': 'QC4',
 'SZ5': 'SQ5',
 'SZ8': 'QS8',
 'SZ9': 'QS9',
 'SZH': 'QX5',
 'SZK': 'QS5',
 'TCI': 'TH',
 'TCW': 'TM',
 'TDT': 'TL',
 'TE2': 'GE',
 'TE3': 'GE',
 'TE4': 'GE',
 'TFO': 'TTF',
 'TN1': 'TN',
 'TN2': 'TN',
 'TN3': 'TN',
 'TN4': 'TN',
 'TN5': 'TN',
 'TS2': 'SR3',
 'TS3': 'SR3',
 'TS4': 'SR3',
 'TTL': 'TTF',
 'TTO': 'TTF',
 'U01': 'NG',
 'U02': 'NG',
 'U07': 'NG',
 'U08': 'NG',
 'U09': 'NG',
 'U10': 'NG',
 'U13': 'NG',
 'U14': 'NG',
 'U15': 'NG',
 'U16': 'NG',
 'U17': 'NG',
 'U18': 'NG',
 'U19': 'NG',
 'U20': 'NG',
 'U21': 'NG',
 'U22': 'NG',
 'U23': 'NG',
 'U24': 'NG',
 'U25': 'NG',
 'U27': 'NG',
 'U30': 'NG',
 'U31': 'NG',
 'UB1': 'UB',
 'UB2': 'UB',
 'UB3': 'UB',
 'UB4': 'UB',
 'UB5': 'UB',
 'UFO': 'UKG',
 'UKO': 'UKG',
 'UWO': 'UWF',
 'V6A': '6A',
 'V6B': '6B',
 'V6C': '6C',
 'V6E': '6E',
 'V6J': '6J',
 'VA1': '6A',
 'VA2': '6A',
 'VA3': '6A',
 'VA4': '6A',
 'VA5': '6A',
 'VAA': '6A',
 'VAB': '6A',
 'VAC': '6A',
 'VAD': '6A',
 'VAE': '6A',
 'VBA': '6B',
 'VBB': '6B',
 'VBC': '6B',
 'VBD': '6B',
 'VBE': '6B',
 'VC1': '6C',
 'VC2': '6C',
 'VC3': '6C',
 'VC4': '6C',
 'VC5': '6C',
 'VCA': '6C',
 'VCB': '6C',
 'VCC': '6C',
 'VCD': '6C',
 'VCE': '6C',
 'VE1': '6E',
 'VE2': '6E',
 'VE3': '6E',
 'VE4': '6E',
 'VE5': '6E',
 'VG1': '6B',
 'VG2': '6B',
 'VG3': '6B',
 'VG4': '6B',
 'VG5': '6B',
 'VJ1': '6J',
 'VJ2': '6J',
 'VJ3': '6J',
 'VJ4': '6J',
 'VJ5': '6J',
 'VJA': '6J',
 'VJB': '6J',
 'VJC': '6J',
 'VJD': '6J',
 'VJE': '6J',
 'VSA': '6S',
 'VSB': '6S',
 'VSC': '6S',
 'VSD': '6S',
 'VSE': '6S',
 'VTA': '6E',
 'VTB': '6E',
 'VTC': '6E',
 'VTD': '6E',
 'VTE': '6E',
 'VXA': '6A',
 'VXB': '6B',
 'VXC': '6C',
 'VXJ': '6J',
 'VXS': '6S',
 'VXT': '6E',
 'WA1': '6A',
 'WA2': '6A',
 'WA3': '6A',
 'WA4': '6A',
 'WA5': '6A',
 'WAO': 'WNC',
 'WAY': 'CAY',
 'WB': 'CQ',
 'WB1': 'ZB',
 'WB2': 'ZB',
 'WB3': 'ZB',
 'WB4': 'ZB',
 'WB5': 'ZB',
 'WC': 'CT',
 'WC3': 'Z3W',
 'WC6': 'QW6',
 'WCI': 'WCW',
 'WCM': 'WQ6',
 'WCO': 'WCE',
 'WD1': '6C',
 'WD2': '6C',
 'WD3': '6C',
 'WD4': '6C',
 'WD5': '6C',
 'WE1': '6E',
 'WE2': '6E',
 'WE3': '6E',
 'WE4': '6E',
 'WE5': '6E',
 'WF1': 'ZF',
 'WF2': 'ZF',
 'WF3': 'ZF',
 'WF4': 'ZF',
 'WF5': 'ZF',
 'WG1': '6B',
 'WG2': '6B',
 'WG3': '6B',
 'WG4': '6B',
 'WG5': '6B',
 'WJ1': '6J',
 'WJ2': '6J',
 'WJ3': '6J',
 'WJ4': '6J',
 'WJ5': '6J',
 'WJO': 'AWJ',
 'WNO': 'WNT',
 'WT1': 'ZT',
 'WT2': 'ZT',
 'WT3': 'ZT',
 'WT4': 'ZT',
 'WT5': 'ZT',
 'WTO': 'WTT',
 'WU1': 'UB',
 'WU2': 'UB',
 'WU3': 'UB',
 'WU4': 'UB',
 'WU5': 'UB',
 'WX1': 'TN',
 'WX2': 'TN',
 'WX3': 'TN',
 'WX4': 'TN',
 'WX5': 'TN',
 'WY1': 'ZN',
 'WY2': 'ZN',
 'WY3': 'ZN',
 'WY4': 'ZN',
 'WY5': 'ZN',
 'XAO': 'AXA',
 'YM1': 'YM',
 'YM2': 'YM',
 'YM3': 'YM',
 'YM4': 'YM',
 'YPC': 'SP',
 'YVO': 'AYV',
 'YXO': 'AYX',
 'Z07': 'T07',
 'Z08': 'T08',
 'Z09': 'T09',
 'Z10': 'T10',
 'Z13': 'T13',
 'Z16': 'T16',
 'Z17': 'T17',
 'Z18': 'T18',
 'Z19': 'T19',
 'Z1O': 'AZ1',
 'Z20': 'T20',
 'Z23': 'T23',
 'ZAY': 'ZIY',
 'ZB1': 'ZB',
 'ZB2': 'ZB',
 'ZB3': 'ZB',
 'ZB4': 'ZB',
 'ZB5': 'ZB',
 'ZC1': 'ZC',
 'ZC2': 'ZC',
 'ZC3': 'ZC',
 'ZC4': 'ZC',
 'ZC5': 'ZC',
 'ZCW': 'QCW',
 'ZF1': 'ZF',
 'ZF2': 'ZF',
 'ZF3': 'ZF',
 'ZF4': 'ZF',
 'ZF5': 'ZF',
 'ZL1': 'ZL',
 'ZL2': 'ZL',
 'ZL3': 'ZL',
 'ZL4': 'ZL',
 'ZL5': 'ZL',
 'ZM1': 'ZM',
 'ZM2': 'ZM',
 'ZM3': 'ZM',
 'ZM4': 'ZM',
 'ZM5': 'ZM',
 'ZN1': 'ZN',
 'ZN2': 'ZN',
 'ZN3': 'ZN',
 'ZN4': 'ZN',
 'ZN5': 'ZN',
 'ZQ1': 'ZQ',
 'ZQ6': 'ZQ',
 'ZS1': 'ZS',
 'ZS2': 'ZS',
 'ZS3': 'ZS',
 'ZS4': 'ZS',
 'ZS5': 'ZS',
 'ZT1': 'ZT',
 'ZT2': 'ZT',
 'ZT3': 'ZT',
 'ZT4': 'ZT',
 'ZT5': 'ZT',
 'ZW1': 'ZW',
 'ZW2': 'ZW',
 'ZW3': 'ZW',
 'ZW4': 'ZW',
 'ZW5': 'ZW'}
