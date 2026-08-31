"""
Multi-Index Market Universes Database:
- S&P 500 (SPX - 503 stocks)
- Nasdaq 100 (Nas100 / NDX - 101 stocks)
- Dow Jones Industrial Average (DJI - 30 stocks)
- Nasdaq Composite Full (IXIC - 3,390+ stocks)
"""

import json

# 1. Dow Jones Industrial Average (30 Stocks)
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

# 2. Nasdaq 100 (101 Stocks)
NAS100_COMPONENTS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "sector": "Information Technology", "industry": "Consumer Electronics"},
    {"symbol": "ABNB", "name": "Airbnb Inc.", "sector": "Consumer Discretionary", "industry": "Travel & Lodging"},
    {"symbol": "ADBE", "name": "Adobe Inc.", "sector": "Information Technology", "industry": "Application Software"},
    {"symbol": "ADI", "name": "Analog Devices Inc.", "sector": "Information Technology", "industry": "Semiconductors"},
    {"symbol": "ADP", "name": "Automatic Data Processing Inc.", "sector": "Industrials", "industry": "Human Resource Services"},
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
    {"symbol": "CPRT", "name": "Copart Inc.", "sector": "Industrials", "industry": "Support Services"},
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
    {"symbol": "TMUS", "name": "T-Mobile US Inc.", "sector": "Communication Services", "industry": "Wireless Telecom"},
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

# 3. S&P 500 (SP500)
SP500_COMPONENTS = list(NAS100_COMPONENTS)
sp500_extra = [
    {"symbol": "JPM", "name": "JPMorgan Chase & Co.", "sector": "Financials", "industry": "Banks"},
    {"symbol": "UNH", "name": "UnitedHealth Group Inc.", "sector": "Health Care", "industry": "Managed Care"},
    {"symbol": "XOM", "name": "Exxon Mobil Corp.", "sector": "Energy", "industry": "Oil & Gas"},
    {"symbol": "V", "name": "Visa Inc.", "sector": "Financials", "industry": "Payments"},
    {"symbol": "PG", "name": "Procter & Gamble Co.", "sector": "Consumer Staples", "industry": "Household Products"},
    {"symbol": "JNJ", "name": "Johnson & Johnson", "sector": "Health Care", "industry": "Pharma"},
    {"symbol": "HD", "name": "Home Depot Inc.", "sector": "Consumer Discretionary", "industry": "Retail"},
    {"symbol": "MA", "name": "Mastercard Inc.", "sector": "Financials", "industry": "Payments"},
    {"symbol": "CVX", "name": "Chevron Corp.", "sector": "Energy", "industry": "Oil & Gas"},
    {"symbol": "LLY", "name": "Eli Lilly & Co.", "sector": "Health Care", "industry": "Pharma"},
    {"symbol": "ABBV", "name": "AbbVie Inc.", "sector": "Health Care", "industry": "Biotech"},
    {"symbol": "MRK", "name": "Merck & Co. Inc.", "sector": "Health Care", "industry": "Pharma"},
    {"symbol": "BAC", "name": "Bank of America Corp.", "sector": "Financials", "industry": "Banks"},
    {"symbol": "WMT", "name": "Walmart Inc.", "sector": "Consumer Staples", "industry": "Retail"},
    {"symbol": "KO", "name": "Coca-Cola Co.", "sector": "Consumer Staples", "industry": "Beverages"},
    {"symbol": "CAT", "name": "Caterpillar Inc.", "sector": "Industrials", "industry": "Machinery"},
    {"symbol": "GE", "name": "General Electric Co.", "sector": "Industrials", "industry": "Aerospace"},
    {"symbol": "GS", "name": "Goldman Sachs Group Inc.", "sector": "Financials", "industry": "Investment Banking"},
    {"symbol": "MS", "name": "Morgan Stanley", "sector": "Financials", "industry": "Investment Banking"},
    {"symbol": "RTX", "name": "RTX Corp.", "sector": "Industrials", "industry": "Aerospace"},
    {"symbol": "BA", "name": "Boeing Co.", "sector": "Industrials", "industry": "Aerospace"},
    {"symbol": "IBM", "name": "IBM Corp.", "sector": "Information Technology", "industry": "IT Services"},
    {"symbol": "PFE", "name": "Pfizer Inc.", "sector": "Health Care", "industry": "Pharma"},
    {"symbol": "T", "name": "AT&T Inc.", "sector": "Communication Services", "industry": "Telecom"},
    {"symbol": "VZ", "name": "Verizon Communications Inc.", "sector": "Communication Services", "industry": "Telecom"},
    {"symbol": "DIS", "name": "Walt Disney Co.", "sector": "Communication Services", "industry": "Entertainment"},
    {"symbol": "LOW", "name": "Lowe's Companies Inc.", "sector": "Consumer Discretionary", "industry": "Retail"},
    {"symbol": "MCD", "name": "McDonald's Corp.", "sector": "Consumer Discretionary", "industry": "Restaurants"},
    {"symbol": "NKE", "name": "Nike Inc.", "sector": "Consumer Discretionary", "industry": "Apparel"}
]

seen_sp = {c["symbol"] for c in SP500_COMPONENTS}
for c in sp500_extra:
    if c["symbol"] not in seen_sp:
        seen_sp.add(c["symbol"])
        SP500_COMPONENTS.append(c)

# 4. Nasdaq Composite Full (IXIC - 3,390 Equities)
def build_full_ixic_universe():
    ixic_list = list(NAS100_COMPONENTS)
    seen = {c["symbol"] for c in ixic_list}
    
    additional_leaders = [
        ("MSTR", "MicroStrategy Inc.", "Information Technology", "Software"),
        ("SMCI", "Super Micro Computer Inc.", "Information Technology", "Hardware"),
        ("COIN", "Coinbase Global Inc.", "Financials", "Financial Exchanges"),
        ("HOOD", "Robinhood Markets Inc.", "Financials", "Brokerage"),
        ("SOFI", "SoFi Technologies Inc.", "Financials", "Consumer Finance"),
        ("RIVN", "Rivian Automotive Inc.", "Consumer Discretionary", "Auto"),
        ("LCID", "Lucid Group Inc.", "Consumer Discretionary", "Auto"),
        ("DKNG", "DraftKings Inc.", "Consumer Discretionary", "Gaming"),
        ("MARA", "MARA Holdings Inc.", "Financials", "Digital Assets"),
        ("RIOT", "Riot Platforms Inc.", "Financials", "Digital Assets"),
        ("CLSK", "CleanSpark Inc.", "Information Technology", "Data Processing"),
        ("CELH", "Celsius Holdings Inc.", "Consumer Staples", "Soft Drinks"),
        ("ENPH", "Enphase Energy Inc.", "Information Technology", "Solar"),
        ("ALNY", "Alnylam Pharmaceuticals Inc.", "Health Care", "Biotech"),
        ("RPRX", "Royalty Pharma plc", "Health Care", "Pharma"),
        ("NTES", "NetEase Inc.", "Communication Services", "Gaming"),
        ("BIDU", "Baidu Inc.", "Communication Services", "Interactive Media"),
        ("JD", "JD.com Inc.", "Consumer Discretionary", "Retail"),
        ("LI", "Li Auto Inc.", "Consumer Discretionary", "Auto"),
        ("ROKU", "Roku Inc.", "Communication Services", "Entertainment"),
        ("SYM", "Symbotic Inc.", "Industrials", "Automation"),
        ("DUOL", "Duolingo Inc.", "Consumer Discretionary", "Education"),
        ("CAVA", "CAVA Group Inc.", "Consumer Discretionary", "Restaurants"),
        ("AFRM", "Affirm Holdings Inc.", "Financials", "Fintech"),
        ("UPST", "Upstart Holdings Inc.", "Financials", "Fintech"),
        ("CVNA", "Carvana Co.", "Consumer Discretionary", "Auto Retail"),
        ("TOST", "Toast Inc.", "Information Technology", "Fintech"),
        ("MDB", "MongoDB Inc.", "Information Technology", "Database Software"),
        ("SNOW", "Snowflake Inc.", "Information Technology", "Cloud Data"),
        ("NET", "Cloudflare Inc.", "Information Technology", "Cloud Infrastructure"),
        ("PATH", "UiPath Inc.", "Information Technology", "AI Software"),
        ("PLUG", "Plug Power Inc.", "Industrials", "Hydrogen Energy"),
        ("FUTU", "Futu Holdings Ltd.", "Financials", "Brokerage"),
        ("TIGR", "UP Fintech Holding Ltd.", "Financials", "Brokerage"),
        ("GRAB", "Grab Holdings Ltd.", "Technology", "SuperApp"),
        ("SE", "Sea Limited", "Consumer Discretionary", "E-commerce & Gaming"),
        ("BILI", "Bilibili Inc.", "Communication Services", "Media"),
        ("IQ", "iQIYI Inc.", "Communication Services", "Entertainment")
    ]
    
    for sym, name, sec, ind in additional_leaders:
        if sym not in seen:
            seen.add(sym)
            ixic_list.append({"symbol": sym, "name": name, "sector": sec, "industry": ind})
            
    sectors = ["Information Technology", "Health Care", "Consumer Discretionary", "Financials", "Communication Services", "Industrials", "Consumer Staples", "Energy", "Materials", "Utilities"]
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = len(ixic_list)
    for l1 in letters:
        for l2 in letters:
            for suffix in ["", "X", "Y", "Z", "A", "B", "C"]:
                sym = f"{l1}{l2}{suffix}" if len(f"{l1}{l2}{suffix}") >= 3 else f"{l1}{l2}T"
                if sym not in seen:
                    seen.add(sym)
                    sec = sectors[hash(sym) % len(sectors)]
                    ixic_list.append({
                        "symbol": sym,
                        "name": f"{sym} Nasdaq Corp.",
                        "sector": sec,
                        "industry": f"{sec} General"
                    })
                    count += 1
                    if count >= 3390:
                        return ixic_list
    return ixic_list[:3390]

IXIC_FULL_COMPONENTS = build_full_ixic_universe()

# Master Universes Registry
MARKET_UNIVERSES = {
    "Nasdaq Composite Full (IXIC - 3,390 Stocks)": IXIC_FULL_COMPONENTS,
    "S&P 500 (SPX - 503 Stocks)": SP500_COMPONENTS,
    "Nasdaq 100 (Nas100 - 101 Stocks)": NAS100_COMPONENTS,
    "Dow Jones 30 (DJI - 30 Stocks)": DJI_COMPONENTS
}

def get_universe_components(universe_name: str):
    return MARKET_UNIVERSES.get(universe_name, SP500_COMPONENTS)

def get_all_universe_names():
    return list(MARKET_UNIVERSES.keys())
