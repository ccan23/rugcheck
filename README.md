# RugCheck
![RugCheck](docs/header.jpeg)

This is an **unofficial** but simple and super easy-to-use Python wrapper for [rugcheck.xyz](https://rugcheck.xyz).

If you’ve been around DEXs, you know the scams, rug pulls, and sudden liquidity losses. This wrapper lets you automate token risk checks, potentially saving your wallet before it’s too late.

RugCheck doesn’t promise you Lambos or moonshots, but it can help you avoid disasters. Use it as one part of your research arsenal.

Stay safe and happy trading!

## ⚠️ Disclaimer
I'm just the messenger here. This project **only gives you what RugCheck reports** so what they report is what you get. If they mess up or miss a rug, **I'm not responsible!** So please **DYOR** and stay cautious :) 

## 📚 Helpful Links
- **RugCheck API Documentation**: [Swagger Docs](https://api.rugcheck.xyz/swagger/index.html)
- **Post About API**: [x.com/Rugcheckxyz](https://x.com/Rugcheckxyz/status/1875266458642780429)


## 📥 Installation
Get started by installing via pip:

```bash
pip install rugcheck
```

## 🚀 How to Use It
Check any token with ease:

```python
from rugcheck import rugcheck

token = '6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN'
rc = rugcheck(token)
```

## 🔍 Get a Summary
You can use `rc.summary` to get the token's summary as a Python dictionary or just print the `rugcheck` object for an instant, human-readable overview:
```text
>>> print(rc)
Name: OFFICIAL TRUMP (TRUMP)
Rugged: No
Result: Danger
Risk Score: 18717
Mint Address: 6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN
Total Market Liquidity: $454,326,308.40

Risks:
  - Top 10 holders high ownership (Level: danger, Score: 9298)
    Description: The top 10 users hold more than 70% token supply
  - Single holder ownership (Level: danger, Score: 8000)
    Description: One user holds a large amount of the token supply
    Value: 80.00%
  - High ownership (Level: danger, Score: 1419)
    Description: The top users hold more than 80% token supply

Links:
  No links provided.

Detected At: 2025-01-17T14:27:21.13275916Z
```

## 🔑 What’s Inside?
You get all the token details found on the RugCheck website and more. Access them using JavaScript-style dot notation or Python’s classic `get()` method:

```python
rc.creator                rc.get(                   rc.lockers                rc.result                 rc.to_dict()              rc.tokenType              rc.totalMarketLiquidity   
rc.detectedAt             rc.graphInsiderReport     rc.markets                rc.risks                  rc.to_json()              rc.token_address          rc.transferFee            
rc.events                 rc.graphInsidersDetected  rc.mint                   rc.rugged                 rc.token                  rc.token_extensions       rc.verification           
rc.fileMeta               rc.knownAccounts          rc.mintAuthority          rc.score                  rc.tokenMeta              rc.topHolders             
rc.freezeAuthority        rc.lockerOwners           rc.print_summary(         rc.summary                rc.tokenProgram           rc.totalLPProviders 
```

## 📦 Want to See Everything?
Export the entire token data easily:

* As a python dictionary: `rc.to_dict()`
* As a JSON string: `rc.to_json()`

You can check `samples/response.json` for the full response to see what data you can expect.

## 📬 Contact
dev.ccanb@protonmail.com