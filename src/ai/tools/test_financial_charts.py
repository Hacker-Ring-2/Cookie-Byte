"""
Test script for financial chart generation utilities.
This script tests the integration of financial chart types with the graph generation tool.
"""

import json
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.ai.tools.financial_chart_utils import (
    generate_stock_price_chart,
    generate_candlestick_data,
    generate_correlation_heatmap,
    format_chart_for_response,
    detect_chart_type_from_query
)

from src.ai.tools.graph_gen_tool import graph_generation_tool

def test_stock_price_chart():
    """Test generating a stock price line chart"""
    print("\n=== Testing Stock Price Chart ===")
    
    # Sample data
    ticker = "AAPL"
    dates = ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01"]
    prices = [150.82, 155.73, 160.95, 165.21, 170.35]
    
    # Generate chart
    chart_data = generate_stock_price_chart(ticker, dates, prices)
    
    # Format for response
    response = format_chart_for_response(chart_data)
    
    print(f"Chart data: {json.dumps(chart_data, indent=2)}")
    print(f"Formatted response: {response}")
    
    return chart_data

def test_candlestick_chart():
    """Test generating a candlestick chart"""
    print("\n=== Testing Candlestick Chart ===")
    
    # Sample data
    dates = ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01"]
    open_prices = [150.0, 155.0, 158.0, 163.0, 168.0]
    high_prices = [152.0, 158.0, 162.0, 167.0, 172.0]
    low_prices = [148.0, 153.0, 156.0, 161.0, 166.0]
    close_prices = [151.0, 157.0, 160.0, 165.0, 170.0]
    volumes = [1000000, 1200000, 980000, 1100000, 1300000]
    
    # Generate chart
    chart_data = generate_candlestick_data(
        dates, open_prices, high_prices, low_prices, close_prices, volumes, "AAPL"
    )
    
    print(f"Chart data: {json.dumps(chart_data, indent=2)}")
    
    return chart_data

def test_correlation_heatmap():
    """Test generating a correlation heatmap"""
    print("\n=== Testing Correlation Heatmap ===")
    
    # Sample data
    labels = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
    correlation_matrix = [
        [1.0, 0.7, 0.6, 0.5, 0.4],
        [0.7, 1.0, 0.8, 0.6, 0.5],
        [0.6, 0.8, 1.0, 0.7, 0.6],
        [0.5, 0.6, 0.7, 1.0, 0.8],
        [0.4, 0.5, 0.6, 0.8, 1.0]
    ]
    
    # Generate chart
    chart_data = generate_correlation_heatmap(labels, correlation_matrix, "Stock Correlation Matrix")
    
    print(f"Chart data: {json.dumps(chart_data, indent=2)}")
    
    return chart_data

def test_chart_type_detection():
    """Test chart type detection from queries"""
    print("\n=== Testing Chart Type Detection ===")
    
    queries = [
        "Show me a candlestick chart for Apple stock",
        "Create a correlation heatmap for tech stocks",
        "Display the trend of MSFT stock price over time",
        "What's the distribution of my portfolio allocation?",
        "Compare quarterly revenue for top tech companies"
    ]
    
    for query in queries:
        detected_types = detect_chart_type_from_query(query)
        print(f"Query: '{query}' -> Detected types: {detected_types}")

def test_graph_gen_tool_integration():
    """Test integration with graph_gen_tool"""
    print("\n=== Testing Graph Generation Tool Integration ===")
    
    # Sample markdown table for stock data
    stock_table = """
    | Date | Open | High | Low | Close | Volume |
    |------|------|------|-----|-------|--------|
    | 2023-01-01 | 150.0 | 152.0 | 148.0 | 151.0 | 1000000 |
    | 2023-02-01 | 155.0 | 158.0 | 153.0 | 157.0 | 1200000 |
    | 2023-03-01 | 158.0 | 162.0 | 156.0 | 160.0 | 980000 |
    | 2023-04-01 | 163.0 | 167.0 | 161.0 | 165.0 | 1100000 |
    | 2023-05-01 | 168.0 | 172.0 | 166.0 | 170.0 | 1300000 |
    """
    
    # Test with candlestick chart type
    result = graph_generation_tool._run(
        table=stock_table,
        query="Show me a candlestick chart for this stock data",
        chart_type="candlestick"
    )
    
    print(f"Graph generation tool result: {result}")
    
    return result

if __name__ == "__main__":
    # Run all tests
    test_stock_price_chart()
    test_candlestick_chart()
    test_correlation_heatmap()
    test_chart_type_detection()
    
    # Test integration with graph_gen_tool
    test_graph_gen_tool_integration()
    
    print("\nAll tests completed!")