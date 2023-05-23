from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

"""
Strategy pattern use case to pull data in a flexible way.
Ensure the environment variables are properly set.
Create an instance of one of the subclasses and use the method pull_data with your custom query.
Returns a dataframe.

Example:
PullDataProduction1().pull_data('enter_your_query_or_function_here')
"""

class PullDataStrategy(ABC):
    """
    Abstract class to provide an interface for different data pulling strategies.
    Subclasses should implement the pull_data method.
    """
    @abstractmethod
    def pull_data(self, query: str):
        pass

class PullDataProduction1(PullDataStrategy):
    def pull_data(self, query: str):
        df_data = pd.read_sql(sql=query, con=os.getenv("PRODUCTION1_URI"))
        return df_data

class PullDataProduction2(PullDataStrategy):
    def pull_data(self, query: str):
        df_data = pd.read_sql(sql=query, con=os.getenv("PRODUCTION2_URI"))
        return df_data

class PullDataReplica1(PullDataStrategy):
    def pull_data(self, query: str):
        df_data = pd.read_sql(sql=query, con=os.getenv("REPLICA1_URI"))
        return df_data

class PullDataReplica2(PullDataStrategy):
    def pull_data(self, query: str):
        df_data = pd.read_sql(sql=query, con=os.getenv("REPLICA2_URI"))
        return df_data

def test_query():
    return f"""
    select * from submissions limit 100
    """

def main():
    # Example usage:
    # PullDataProduction1().pull_data('enter_your_query_or_function_here')
    # PullDataProduction1().pull_data(get_annotations_test())
    return PullDataProduction2().pull_data(test_query())

if __name__ == "__main__":
    test_df = main()
    print(test_df)
