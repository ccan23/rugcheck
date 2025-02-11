#!/usr/bin/env python3

import json
import requests

class RugCheckData:
    """A simple wrapper with dot notation, .get(), and dictionary-like access."""

    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                value = RugCheckData(value)
            elif isinstance(value, list):
                value = [RugCheckData(item) if isinstance(item, dict) else item for item in value]
            setattr(self, key, value)

    def get(self, key, default=None):
        """Mimic dict.get()."""
        return getattr(self, key, default)

    def to_dict(self):
        """Convert back to a standard dictionary."""
        def convert(value):
            if isinstance(value, RugCheckData):
                return value.to_dict()
            elif isinstance(value, list):
                return [convert(item) for item in value]
            return value

        return {key: convert(value) for key, value in self.__dict__.items()}

    def to_json(self):
        """Convert to a JSON string."""
        return json.dumps(self.to_dict(), indent=4)

    def __getitem__(self, key):
        """Enable dictionary-style access using [key]."""
        return getattr(self, key)

    def __repr__(self):
        """Provide clean, readable output."""
        return repr(self.to_dict())

class rugcheck:
    """
    rugcheck: A simple Python wrapper for interacting with the RugCheck API.

    This class provides easy access to token-related risk assessments, including liquidity, holder risks, 
    and other important factors that could indicate a rug pull or scam. It allows users to fetch data,
    print summaries, and convert token information into Python dictionaries or JSON strings.

    Attributes:
        token_address (str): The address of the token to be checked.
        price (dict or None): The token's price details (fetched if `get_price=True`).
        votes (dict or None): The token's voting data (fetched if `get_votes=True`).

    Usage:
        >>> from rugcheck import rugcheck
        
        >>> token = '6p6xgHyF7AeE6TZkSmFsko444wqoP15icUSqi2jfGiPN'
        >>> rc = rugcheck(token)
    """

    def __init__(self, token_address: str, get_price: bool = False, get_votes: bool = False):
        self.token_address = token_address
        self._wrapped_data = RugCheckData(self.__fetch_report())
        
        for key, value in self._wrapped_data.__dict__.items():
            setattr(self, key, value)

        self.price = self.__fetch_price() if get_price else None
        self.votes = RugCheckData(self.__fetch_votes()) if get_votes else None

    def __fetch_data(self, url: str) -> dict:
        """Fetch data from an endpoint."""
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.3; Win64; x64; en-US) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/49.0.1324.155 Safari/602',}
        response = requests.get(url=url, headers=headers)
        if response and response.status_code == 200:
            return response.json()
        return {}
    
    def __fetch_report(self):
        return self.__fetch_data(f'https://api.rugcheck.xyz/v1/tokens/{self.token_address}/report')
    
    def __fetch_votes(self):
        return self.__fetch_data(f'https://api.rugcheck.xyz/v1/tokens/{self.token_address}/votes')
    
    def __fetch_price(self):
        return self.__fetch_data(f'https://data.fluxbeam.xyz/tokens/{self.token_address}/price')

    def get(self, key, default=None) -> dict:
        """Mimic dict.get()"""
        return self._wrapped_data.get(key, default)

    def to_dict(self) -> dict:
        """Convert RugCheck object and its attributes to a dictionary."""
        return self._wrapped_data.to_dict()

    def to_json(self) -> str:
        """Convert RugCheck object and its attributes to JSON."""
        return json.dumps(self.to_dict())

    def __repr__(self):
        return f'<RugCheck token={self.token_address}, score={self.score}, result={self.result}>'
    
    def __str__(self):
        return self.print_summary(self.summary)
    
    def __eq__(self, other):
        return self.result == other

    @property
    def result(self) -> str:
        return 'Good' if self.score < 1e3 else 'Warning' if self.score < 5e3 else 'Danger'
    
    @property
    def summary(self) -> dict:
        """Generate a summary."""
        return {
            'name': self.tokenMeta.name,
            'symbol': self.tokenMeta.symbol,
            'rugged': self.rugged,
            'result': self.result,
            'riskScore': self.score,
            'risks': self.risks,
            'mint': self.mint,
            'totalMarketLiquidity': self.totalMarketLiquidity,
            'links': self.verification.links if self.verification else None,
            'detectedAt': self.detectedAt
        }
    
    def print_summary(self, summary: dict) -> str:
        """Format the summary dictionary for terminal output."""
        result = [
            f"Name: {summary.get('name', 'N/A')} ({summary.get('symbol', 'N/A')})",
            f"Rugged: {'Yes' if summary.get('rugged') else 'No'}",
            f"Result: {summary.get('result', 'N/A')}",
            f"Risk Score: {summary.get('riskScore', 'N/A')}",
            f"Mint Address: {summary.get('mint', 'N/A')}",
            f"Total Market Liquidity: ${summary.get('totalMarketLiquidity', 0):,.2f}"
        ]

        # Risks Section
        risks = summary.get('risks', [])
        result.append("\nRisks:")
        if risks:
            for risk in risks:
                result.append(f"  - {risk.get('name', 'Unknown')} (Level: {risk.get('level', 'N/A')}, Score: {risk.get('score', 'N/A')})")
                result.append(f"    Description: {risk.get('description', 'No description available')}")
                if risk.get('value'):
                    result.append(f"    Value: {risk.get('value')}")
        else:
            result.append("  No significant risks detected.")

        result.append("\nLinks:")
        links = summary.get('links', [])
        if links:
            for link in links:
                result.append(f"  - {link.get('provider', 'Unknown').capitalize()}: {link.get('value', 'No link provided')}")
        else:
            result.append("  No links provided.")

        result.append(f"\nDetected At: {summary.get('detectedAt', 'Unknown')}")
        return '\n'.join(result)