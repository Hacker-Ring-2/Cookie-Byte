"""
Test cases for preference detection functionality
"""

from preference_detector import detect_response_preference, analyze_preference_strength


def test_preference_detection():
    """Test various user inputs for preference detection"""
    
    test_cases = [
        # Visual preferences
        ("I prefer charts and graphs", "visual"),
        ("Show me visual representations", "visual"),
        ("I like to see data in charts", "visual"),
        ("Give me graphs and visualizations", "visual"),
        ("I'm a visual learner, show me diagrams", "visual"),
        ("Display information using charts and plots", "visual"),
        ("I want to see pie charts and bar graphs", "visual"),
        ("Visualize the data for me", "visual"),
        
        # Text preferences  
        ("Give me detailed text explanations", "text"),
        ("I prefer written descriptions", "text"),
        ("Provide comprehensive analysis in text", "text"),
        ("I like detailed explanations", "text"),
        ("Give me thorough written reports", "text"),
        ("I prefer reading detailed summaries", "text"),
        ("Explain everything in detail with text", "text"),
        ("I want in-depth textual analysis", "text"),
        
        # Mixed or unclear
        ("I like both charts and detailed explanations", None),
        ("Hello, I'm John from New York", None),
        ("I work in finance and need market updates", None),
        ("", None),
        (None, None),
        
        # Edge cases
        ("Charts are okay but I prefer detailed text", "text"),
        ("I usually like text but show me some graphs too", "text"),
        ("Visual charts help but give me explanations", None),  # Equal weight
    ]
    
    print("Testing preference detection...")
    print("=" * 50)
    
    for i, (text, expected) in enumerate(test_cases, 1):
        result = detect_response_preference(text)
        actual = result['preference']
        
        status = "✅ PASS" if actual == expected else "❌ FAIL"
        print(f"Test {i:2d}: {status}")
        print(f"  Input: '{text}'")
        print(f"  Expected: {expected}")
        print(f"  Actual: {actual}")
        print()


def test_preference_analysis():
    """Test detailed preference analysis"""
    
    test_texts = [
        "I prefer charts and graphs for financial data",
        "Give me detailed text explanations with comprehensive analysis",
        "I'm a visual person who likes dashboards and plots",
        "Hello, I work in finance"
    ]
    
    print("Testing detailed preference analysis...")
    print("=" * 50)
    
    for i, text in enumerate(test_texts, 1):
        result = analyze_preference_strength(text)
        
        print(f"Analysis {i}:")
        print(f"  Input: '{text}'")
        print(f"  Preference: {result['preference']}")
        print(f"  Confidence: {result['confidence']}")
        print(f"  Visual keywords: {result['visual_keywords']}")
        print(f"  Text keywords: {result['text_keywords']}")
        print(f"  Total keywords: {result['total_keywords']}")
        print()


if __name__ == "__main__":
    test_preference_detection()
    test_preference_analysis()