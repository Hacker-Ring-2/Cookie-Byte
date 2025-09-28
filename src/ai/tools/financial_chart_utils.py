"""
Financial chart utilities for extending graph generation capabilities.
This module provides functions to generate various financial chart types
for use in prompt responses.
"""

import json
from typing import Dict, List, Any, Optional, Union

# Chart type definitions
CHART_TYPES = {
    "line": "lines",
    "bar": "bar",
    "group_bar": "group_bar",
    "pie": "pie",
    "candlestick": "candlestick",
    "heatmap": "heatmap"
}

def generate_stock_price_chart(ticker: str, 
                              dates: List[str], 
                              prices: List[float], 
                              title: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a line chart for stock price history.
    
    Args:
        ticker: Stock ticker symbol
        dates: List of date strings
        prices: List of price values
        title: Optional chart title
        
    Returns:
        Chart data structure compatible with PlotlyChart
    """
    if not title:
        title = f"{ticker} Stock Price History"
        
    return {
        "chart_type": "lines",
        "chart_title": title,
        "x_label": "Date",
        "y_label": "Price ($)",
        "data": [
            {
                "legend_label": ticker,
                "x_axis_data": dates,
                "y_axis_data": prices
            }
        ]
    }

def generate_multi_stock_comparison(tickers: List[str], 
                                   dates: List[str], 
                                   prices_by_ticker: Dict[str, List[float]],
                                   title: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a line chart comparing multiple stocks.
    
    Args:
        tickers: List of stock ticker symbols
        dates: List of date strings (shared x-axis)
        prices_by_ticker: Dictionary mapping tickers to their price lists
        title: Optional chart title
        
    Returns:
        Chart data structure compatible with PlotlyChart
    """
    if not title:
        title = "Stock Price Comparison"
        
    data = []
    for ticker in tickers:
        if ticker in prices_by_ticker:
            data.append({
                "legend_label": ticker,
                "x_axis_data": dates,
                "y_axis_data": prices_by_ticker[ticker]
            })
    
    return {
        "chart_type": "lines",
        "chart_title": title,
        "x_label": "Date",
        "y_label": "Price ($)",
        "data": data
    }

def generate_candlestick_data(dates: List[str],
                             open_prices: List[float],
                             high_prices: List[float],
                             low_prices: List[float],
                             close_prices: List[float],
                             volumes: Optional[List[float]] = None,
                             ticker: Optional[str] = None,
                             title: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate data for a candlestick chart.
    
    Args:
        dates: List of date strings
        open_prices: List of opening prices
        high_prices: List of high prices
        low_prices: List of low prices
        close_prices: List of closing prices
        volumes: Optional list of trading volumes
        ticker: Optional stock ticker symbol
        title: Optional chart title
        
    Returns:
        Candlestick chart data structure
    """
    if not title and ticker:
        title = f"{ticker} Price Movement"
    elif not title:
        title = "Stock Price Movement"
        
    return {
        "dates": dates,
        "open": open_prices,
        "high": high_prices,
        "low": low_prices,
        "close": close_prices,
        "volume": volumes if volumes else [],
        "title": title
    }

def generate_correlation_heatmap(labels: List[str],
                                correlation_matrix: List[List[float]],
                                title: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate data for a correlation heatmap.
    
    Args:
        labels: List of labels for the correlation matrix
        correlation_matrix: 2D list of correlation values
        title: Optional chart title
        
    Returns:
        Correlation heatmap data structure
    """
    if not title:
        title = "Correlation Matrix"
        
    return {
        "labels": labels,
        "correlationMatrix": correlation_matrix,
        "title": title
    }

def generate_financial_metrics_chart(companies: List[str],
                                    metric: str,
                                    values: List[float],
                                    unit: str = "$",
                                    title: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a bar chart for financial metrics comparison.
    
    Args:
        companies: List of company names
        metric: The financial metric being compared
        values: List of metric values
        unit: Unit of measurement
        title: Optional chart title
        
    Returns:
        Chart data structure compatible with PlotlyChart
    """
    if not title:
        title = f"{metric} Comparison"
        
    return {
        "chart_type": "bar",
        "chart_title": title,
        "x_label": "Company",
        "y_label": f"{metric} ({unit})",
        "data": [
            {
                "legend_label": metric,
                "x_axis_data": companies,
                "y_axis_data": values
            }
        ]
    }

def generate_pie_chart(labels: List[str],
                      values: List[float],
                      title: Optional[str] = None,
                      metric: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a pie chart for data distribution.
    
    Args:
        labels: List of segment labels
        values: List of segment values
        title: Optional chart title
        metric: Optional metric name
        
    Returns:
        Chart data structure compatible with PlotlyChart
    """
    if not title and metric:
        title = f"{metric} Distribution"
    elif not title:
        title = "Distribution"
        
    return {
        "chart_type": "pie",
        "chart_title": title,
        "x_label": "Category",
        "y_label": "Value",
        "data": [
            {
                "legend_label": metric if metric else "Distribution",
                "x_axis_data": labels,
                "y_axis_data": values
            }
        ]
    }

def format_chart_for_response(chart_data: Dict[str, Any]) -> str:
    """
    Format chart data for inclusion in a response.
    
    Args:
        chart_data: Chart data structure
        
    Returns:
        Formatted JSON string for graph block
    """
    # Wrap in chart_collection format expected by frontend
    wrapper = {
        "chart_collection": [chart_data]
    }
    
    return json.dumps(wrapper, ensure_ascii=False)

def detect_chart_type_from_query(query: str) -> List[str]:
    """
    Detect potential chart types from a user query.
    
    Args:
        query: User query string
        
    Returns:
        List of detected chart types
    """
    query = query.lower()
    detected_types = []
    
    # Map keywords to chart types
    keyword_mapping = {
        "candlestick": ["candlestick", "candle", "ohlc", "open high low close"],
        "line": ["line chart", "trend", "over time", "historical", "history"],
        "bar": ["bar chart", "bar graph", "comparison", "compare"],
        "pie": ["pie chart", "distribution", "allocation", "breakdown", "percentage"],
        "heatmap": ["heatmap", "correlation", "matrix", "relationship"],
        "group_bar": ["grouped bar", "group bar", "side by side", "multiple metrics"]
    }
    
    for chart_type, keywords in keyword_mapping.items():
        if any(keyword in query for keyword in keywords):
            detected_types.append(chart_type)
    
    return detected_types

def generate_chart_from_table(table_data: Dict[str, Any], query: str) -> Dict[str, Any]:
    """
    Generate appropriate chart based on table data and query.
    
    Args:
        table_data: Parsed table data
        query: User query string
        
    Returns:
        Chart data structure
    """
    try:
        # Implementation would parse table data and generate appropriate chart
        detected_types = detect_chart_type_from_query(query)
        
        # Default to bar chart if no specific type detected
        chart_type = detected_types[0] if detected_types else "bar"
        
        # Generate chart based on detected type
        # This is a simplified implementation for error handling
        
        return {
            "chart_type": CHART_TYPES.get(chart_type, "bar"),
            "chart_title": "Financial Data",
            "x_label": "Category",
            "y_label": "Value",
            "data": [
                {
                    "legend_label": "Sample Data",
                    "x_axis_data": ["A", "B", "C", "D", "E"],
                    "y_axis_data": [10, 20, 30, 40, 50]
                }
            ]
        }
    except Exception as e:
        import logging
        logging.error(f"Error in generate_chart_from_table: {str(e)}")
        # Return a simple fallback chart
        return {
            "chart_type": "bar",
            "chart_title": "Data Visualization",
            "x_label": "Category",
            "y_label": "Value",
            "data": [
                {
                    "legend_label": "Sample Data",
                    "x_axis_data": ["A", "B", "C"],
                    "y_axis_data": [10, 20, 30]
                }
            ]
        }