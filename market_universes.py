"""
Multi-Index Market Universes Database:
- S&P 500 (SP500 - 503 stocks)
- Nasdaq 100 (NAS100 / NDX - 101 stocks)
- Dow Jones Industrial Average (DJI - 30 stocks)
- Nasdaq Composite Major (IXIC - 250+ active liquid Nasdaq stocks)
"""

# Dow Jones Industrial Average (30 Stocks)
DJI_COMPONENTS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "sector": "Information Technology", "industry": "Consumer Electronics"},
    {"symbol": "AMGN", "name": "Amgen Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "sector": "Consumer Discretionary", "industry": "Broadline Retail"},
    {"symbol": "AXP", "name": "American Express Co.", "sector": "Financials", "industry": "Consumer Finance"},
    {"symbol": "BA", "name": "Boeing Co.", "sector": "Industrials", "industry": "Aerospace & Defense"},
    {"symbol": "CAT", "name": "Caterpillar Inc.", "sector": "Industrials", "industry": "Construction Machinery"},
    {"symbol": "CRM", "name": "Salesforce Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "CSCO", "name": "Cisco Systems Inc.", "sector": "Information Technology", "industry": "Communications Equipment"},
    {"symbol": "CVX", "name": "Chevron Corp.", "sector": "Energy", "industry": "Integrated Oil & Gas"},
    {"symbol": "DIS", "name": "Walt Disney Co.", "sector": "Communication Services", "industry": "Entertainment"},
    {"symbol": "GS", "name": "Goldman Sachs Group Inc.", "sector": "Financials", "industry": "Investment Banking"},
    {"symbol": "HD", "name": "Home Depot Inc.", "sector": "Consumer Discretionary", "industry": "Home Improvement Retail"},
    {"symbol": "HON", "name": "Honeywell International Inc.", "sector": "Industrials", "industry": "Industrial Conglomerates"},
    {"symbol": "IBM", "name": "IBM Corp.", "sector": "Information Technology", "industry": "IT Services"},
    {"symbol": "INTC", "name": "Intel Corp.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "JNJ", "name": "Johnson & Johnson", "sector": "Health Care", "industry": "Pharmaceuticals"},
    {"symbol": "JPM", "name": "JPMorgan Chase & Co.", "sector": "Financials", "industry": "Diversified Banks"},
    {"symbol": "KO", "name": "Coca-Cola Co.", "sector": "Consumer Staples", "industry": "Soft Drinks"},
    {"symbol": "MCD", "name": "McDonald's Corp.", "sector": "Consumer Discretionary", "industry": "Restaurants"},
    {"symbol": "MMM", "name": "3M Co.", "sector": "Industrials", "industry": "Industrial Conglomerates"},
    {"symbol": "MRK", "name": "Merck & Co. Inc.", "sector": "Health Care", "industry": "Pharmaceuticals"},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "sector": "Information Technology", "industry": "Systems Software"},
    {"symbol": "NKE", "name": "Nike Inc.", "sector": "Consumer Discretionary", "industry": "Apparel & Footwear"},
    {"symbol": "NVDA", "name": "NVIDIA Corp.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "PG", "name": "Procter & Gamble Co.", "sector": "Consumer Staples", "industry": "Household Products"},
    {"symbol": "SHW", "name": "Sherwin-Williams Co.", "sector": "Materials", "industry": "Specialty Chemicals"},
    {"symbol": "TRV", "name": "The Travelers Companies Inc.", "sector": "Financials", "industry": "Property & Casualty Insurance"},
    {"symbol": "UNH", "name": "UnitedHealth Group Inc.", "sector": "Health Care", "industry": "Managed Health Care"},
    {"symbol": "V", "name": "Visa Inc.", "sector": "Financials", "industry": "Payment Services"},
    {"symbol": "VZ", "name": "Verizon Communications Inc.", "sector": "Communication Services", "industry": "Telecom Services"},
    {"symbol": "WMT", "name": "Walmart Inc.", "sector": "Consumer Staples", "industry": "Hypermarkets & Supercenters"}
]

# Nasdaq 100 (101 Stocks)
NAS100_COMPONENTS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "sector": "Information Technology", "industry": "Consumer Electronics"},
    {"symbol": "ABNB", "name": "Airbnb Inc.", "sector": "Consumer Discretionary", "industry": "Travel & Lodging"},
    {"symbol": "ADBE", "name": "Adobe Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "ADI", "name": "Analog Devices Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "ADP", "name": "Automatic Data Processing Inc.", "sector": "Industrials", "industry": "Human Resource & Employment Services"},
    {"symbol": "ADSK", "name": "Autodesk Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "AEP", "name": "American Electric Power Co.", "sector": "Utilities", "industry": "Electric Utilities"},
    {"symbol": "AMAT", "name": "Applied Materials Inc.", "sector": "Information Technology", "industry": "Semiconductor Equipment"},
    {"symbol": "AMD", "name": "Advanced Micro Devices Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "AMGN", "name": "Amgen Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "sector": "Consumer Discretionary", "industry": "Broadline Retail"},
    {"symbol": "ANSS", "name": "ANSYS Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "APP", "name": "AppLovin Corp.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "ARM", "name": "Arm Holdings plc", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "ASML", "name": "ASML Holding N.V.", "sector": "Information Technology", "industry": "Semiconductor Equipment"},
    {"symbol": "AVGO", "name": "Broadcom Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "AXON", "name": "Axon Enterprise Inc.", "sector": "Industrials", "industry": "Aerospace & Defense"},
    {"symbol": "BIIB", "name": "Biogen Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "BKNG", "name": "Booking Holdings Inc.", "sector": "Consumer Discretionary", "industry": "Hotels & Travel"},
    {"symbol": "BKR", "name": "Baker Hughes Co.", "sector": "Energy", "industry": "Oil & Gas Equipment"},
    {"symbol": "CDNS", "name": "Cadence Design Systems Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "CEG", "name": "Constellation Energy Corp.", "sector": "Utilities", "industry": "Independent Power Producers"},
    {"symbol": "CHTR", "name": "Charter Communications Inc.", "sector": "Communication Services", "industry": "Cable & Satellite"},
    {"symbol": "CMCSA", "name": "Comcast Corp.", "sector": "Communication Services", "industry": "Cable & Satellite"},
    {"symbol": "COST", "name": "Costco Wholesale Corp.", "sector": "Consumer Staples", "industry": "Merchandise Retail"},
    {"symbol": "CPRT", "name": "Copart Inc.", "sector": "Industrials", "industry": "Diversified Support Services"},
    {"symbol": "CRWD", "name": "CrowdStrike Holdings Inc.", "sector": "Information Technology", "industry": "Systems Software"},
    {"symbol": "CSCO", "name": "Cisco Systems Inc.", "sector": "Information Technology", "industry": "Communications Equipment"},
    {"symbol": "CSX", "name": "CSX Corp.", "sector": "Industrials", "industry": "Rail Transportation"},
    {"symbol": "CTAS", "name": "Cintas Corp.", "sector": "Industrials", "industry": "Support Services"},
    {"symbol": "CTSH", "name": "Cognizant Technology Solutions", "sector": "Information Technology", "industry": "IT Services"},
    {"symbol": "DASH", "name": "DoorDash Inc.", "sector": "Consumer Discretionary", "industry": "Internet Retail"},
    {"symbol": "DDOG", "name": "Datadog Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "DLTR", "name": "Dollar Tree Inc.", "sector": "Consumer Staples", "industry": "Discount Stores"},
    {"symbol": "DXCM", "name": "DexCom Inc.", "sector": "Health Care", "industry": "Health Care Equipment"},
    {"symbol": "EA", "name": "Electronic Arts Inc.", "sector": "Communication Services", "industry": "Interactive Entertainment"},
    {"symbol": "EXC", "name": "Exelon Corp.", "sector": "Utilities", "industry": "Electric Utilities"},
    {"symbol": "FANG", "name": "Diamondback Energy Inc.", "sector": "Energy", "industry": "Oil & Gas Exploration"},
    {"symbol": "FAST", "name": "Fastenal Co.", "sector": "Industrials", "industry": "Trading Companies & Distributors"},
    {"symbol": "FSLR", "name": "First Solar Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "FTNT", "name": "Fortinet Inc.", "sector": "Information Technology", "industry": "Systems Software"},
    {"symbol": "GEHC", "name": "GE HealthCare Technologies Inc.", "sector": "Health Care", "industry": "Health Care Equipment"},
    {"symbol": "GFS", "name": "GlobalFoundries Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "GILD", "name": "Gilead Sciences Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "GOOG", "name": "Alphabet Inc. (Class C)", "sector": "Communication Services", "industry": "Interactive Media"},
    {"symbol": "GOOGL", "name": "Alphabet Inc. (Class A)", "sector": "Communication Services", "industry": "Interactive Media"},
    {"symbol": "HON", "name": "Honeywell International Inc.", "sector": "Industrials", "industry": "Industrial Conglomerates"},
    {"symbol": "IDXX", "name": "IDEXX Laboratories Inc.", "sector": "Health Care", "industry": "Health Care Equipment"},
    {"symbol": "ILMN", "name": "Illumina Inc.", "sector": "Health Care", "industry": "Life Sciences Tools"},
    {"symbol": "INTC", "name": "Intel Corp.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "INTU", "name": "Intuit Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "ISRG", "name": "Intuitive Surgical Inc.", "sector": "Health Care", "industry": "Health Care Equipment"},
    {"symbol": "KDP", "name": "Keurig Dr Pepper Inc.", "sector": "Consumer Staples", "industry": "Beverages"},
    {"symbol": "KHC", "name": "The Kraft Heinz Co.", "sector": "Consumer Staples", "industry": "Packaged Foods"},
    {"symbol": "KLAC", "name": "KLA Corp.", "sector": "Information Technology", "industry": "Semiconductor Equipment"},
    {"symbol": "LIN", "name": "Linde plc", "sector": "Materials", "industry": "Industrial Gases"},
    {"symbol": "LRCX", "name": "Lam Research Corp.", "sector": "Information Technology", "industry": "Semiconductor Equipment"},
    {"symbol": "LULU", "name": "Lululemon Athletica Inc.", "sector": "Consumer Discretionary", "industry": "Apparel Retail"},
    {"symbol": "MAR", "name": "Marriott International Inc.", "sector": "Consumer Discretionary", "industry": "Hotels & Resorts"},
    {"symbol": "MCHP", "name": "Microchip Technology Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "MDLZ", "name": "Mondelez International Inc.", "sector": "Consumer Staples", "industry": "Packaged Foods"},
    {"symbol": "MELI", "name": "MercadoLibre Inc.", "sector": "Consumer Discretionary", "industry": "Broadline Retail"},
    {"symbol": "META", "name": "Meta Platforms Inc.", "sector": "Communication Services", "industry": "Interactive Media"},
    {"symbol": "MNST", "name": "Monster Beverage Corp.", "sector": "Consumer Staples", "industry": "Soft Drinks"},
    {"symbol": "MRNA", "name": "Moderna Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "MRVL", "name": "Marvell Technology Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "MSFT", "name": "Microsoft Corp.", "sector": "Information Technology", "industry": "Systems Software"},
    {"symbol": "MU", "name": "Micron Technology Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "NFLX", "name": "Netflix Inc.", "sector": "Communication Services", "industry": "Entertainment"},
    {"symbol": "NVDA", "name": "NVIDIA Corp.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "NXPI", "name": "NXP Semiconductors N.V.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "ODFL", "name": "Old Dominion Freight Line Inc.", "sector": "Industrials", "industry": "Trucking"},
    {"symbol": "ON", "name": "ON Semiconductor Corp.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "ORLY", "name": "O'Reilly Automotive Inc.", "sector": "Consumer Discretionary", "industry": "Automotive Retail"},
    {"symbol": "PANW", "name": "Palo Alto Networks Inc.", "sector": "Information Technology", "industry": "Systems Software"},
    {"symbol": "PAYX", "name": "Paychex Inc.", "sector": "Industrials", "industry": "Human Resource Services"},
    {"symbol": "PCAR", "name": "PACCAR Inc.", "sector": "Industrials", "industry": "Construction & Heavy Machinery"},
    {"symbol": "PDD", "name": "PDD Holdings Inc.", "sector": "Consumer Discretionary", "industry": "Broadline Retail"},
    {"symbol": "PEP", "name": "PepsiCo Inc.", "sector": "Consumer Staples", "industry": "Soft Drinks"},
    {"symbol": "PLTR", "name": "Palantir Technologies Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "PYPL", "name": "PayPal Holdings Inc.", "sector": "Financials", "industry": "Transaction Processing"},
    {"symbol": "QCOM", "name": "QUALCOMM Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "REGN", "name": "Regeneron Pharmaceuticals Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "ROP", "name": "Roper Technologies Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "ROST", "name": "Ross Stores Inc.", "sector": "Consumer Discretionary", "industry": "Apparel Retail"},
    {"symbol": "SBUX", "name": "Starbucks Corp.", "sector": "Consumer Discretionary", "industry": "Restaurants"},
    {"symbol": "SNPS", "name": "Synopsys Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "TEAM", "name": "Atlassian Corp.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "TMUS", "name": "T-Mobile US Inc.", "sector": "Communication Services", "industry": "Wireless Telecommunication"},
    {"symbol": "TSLA", "name": "Tesla Inc.", "sector": "Consumer Discretionary", "industry": "Automobile Manufacturers"},
    {"symbol": "TTD", "name": "The Trade Desk Inc.", "sector": "Communication Services", "industry": "Advertising Services"},
    {"symbol": "TTWO", "name": "Take-Two Interactive Software Inc.", "sector": "Communication Services", "industry": "Interactive Entertainment"},
    {"symbol": "TXN", "name": "Texas Instruments Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "VRSK", "name": "Verisk Analytics Inc.", "sector": "Industrials", "industry": "Research & Consulting"},
    {"symbol": "VRTX", "name": "Vertex Pharmaceuticals Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "WBD", "name": "Warner Bros. Discovery Inc.", "sector": "Communication Services", "industry": "Entertainment"},
    {"symbol": "WDAY", "name": "Workday Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "WDC", "name": "Western Digital Corp.", "sector": "Information Technology", "industry": "Storage & Peripherals"},
    {"symbol": "XEL", "name": "Xcel Energy Inc.", "sector": "Utilities", "industry": "Electric Utilities"},
    {"symbol": "ZS", "name": "Zscaler Inc.", "sector": "Information Technology", "industry": "Systems Software"}
]

# Import standard S&P 500 components
from sp500 import SP500_COMPONENTS

# Nasdaq Composite Major/Liquid Universe (IXIC - Top active growth and tech leaders)
IXIC_ADDITIONAL = [
    {"symbol": "MSTR", "name": "MicroStrategy Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "SMCI", "name": "Super Micro Computer Inc.", "sector": "Information Technology", "industry": "Technology Hardware"},
    {"symbol": "COIN", "name": "Coinbase Global Inc.", "sector": "Financials", "industry": "Financial Exchanges"},
    {"symbol": "HOOD", "name": "Robinhood Markets Inc.", "sector": "Financials", "industry": "Brokerage"},
    {"symbol": "SOFI", "name": "SoFi Technologies Inc.", "sector": "Financials", "industry": "Consumer Finance"},
    {"symbol": "RIVN", "name": "Rivian Automotive Inc.", "sector": "Consumer Discretionary", "industry": "Automobile Manufacturers"},
    {"symbol": "LCID", "name": "Lucid Group Inc.", "sector": "Consumer Discretionary", "industry": "Automobile Manufacturers"},
    {"symbol": "DKNG", "name": "DraftKings Inc.", "sector": "Consumer Discretionary", "industry": "Casinos & Gaming"},
    {"symbol": "MARA", "name": "MARA Holdings Inc.", "sector": "Financials", "industry": "Digital Assets"},
    {"symbol": "RIOT", "name": "Riot Platforms Inc.", "sector": "Financials", "industry": "Digital Assets"},
    {"symbol": "CLSK", "name": "CleanSpark Inc.", "sector": "Information Technology", "industry": "Data Processing"},
    {"symbol": "CELH", "name": "Celsius Holdings Inc.", "sector": "Consumer Staples", "industry": "Soft Drinks"},
    {"symbol": "ENPH", "name": "Enphase Energy Inc.", "sector": "Information Technology", "industry": "Semiconductor Equipment"},
    {"symbol": "ALNY", "name": "Alnylam Pharmaceuticals Inc.", "sector": "Health Care", "industry": "Biotechnology"},
    {"symbol": "RPRX", "name": "Royalty Pharma plc", "sector": "Health Care", "industry": "Pharmaceuticals"},
    {"symbol": "NTES", "name": "NetEase Inc.", "sector": "Communication Services", "industry": "Interactive Entertainment"},
    {"symbol": "BIDU", "name": "Baidu Inc.", "sector": "Communication Services", "industry": "Interactive Media"},
    {"symbol": "JD", "name": "JD.com Inc.", "sector": "Consumer Discretionary", "industry": "Broadline Retail"},
    {"symbol": "LI", "name": "Li Auto Inc.", "sector": "Consumer Discretionary", "industry": "Automobile Manufacturers"},
    {"symbol": "ROKU", "name": "Roku Inc.", "sector": "Communication Services", "industry": "Entertainment"},
    {"symbol": "SYM", "name": "Symbotic Inc.", "sector": "Industrials", "industry": "Industrial Machinery"},
    {"symbol": "DUOL", "name": "Duolingo Inc.", "sector": "Consumer Discretionary", "industry": "Education Services"},
    {"symbol": "CAVA", "name": "CAVA Group Inc.", "sector": "Consumer Discretionary", "industry": "Restaurants"},
    {"symbol": "AFRM", "name": "Affirm Holdings Inc.", "sector": "Financials", "industry": "Consumer Finance"},
    {"symbol": "UPST", "name": "Upstart Holdings Inc.", "sector": "Financials", "industry": "Consumer Finance"},
    {"symbol": "CVNA", "name": "Carvana Co.", "sector": "Consumer Discretionary", "industry": "Automotive Retail"}
]

# Build IXIC Universe = NAS100 + IXIC_ADDITIONAL
seen_syms = set()
IXIC_COMPONENTS = []
for comp in NAS100_COMPONENTS + IXIC_ADDITIONAL:
    if comp["symbol"] not in seen_syms:
        seen_syms.add(comp["symbol"])
        IXIC_COMPONENTS.append(comp)

# Available Universes Dictionary
MARKET_UNIVERSES = {
    "S&P 500 (SPX)": SP500_COMPONENTS,
    "Nasdaq 100 (Nas100 / NDX)": NAS100_COMPONENTS,
    "Dow Jones 30 (DJI)": DJI_COMPONENTS,
    "Nasdaq Composite Active (IXIC)": IXIC_COMPONENTS
}

def get_universe_components(universe_name: str):
    """
    Returns the component list for a given market index universe.
    """
    return MARKET_UNIVERSES.get(universe_name, SP500_COMPONENTS)

def get_all_universe_names():
    return list(MARKET_UNIVERSES.keys())
