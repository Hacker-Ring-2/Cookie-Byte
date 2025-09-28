"""
Test script to verify the preference detection API endpoint
"""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from backend.utils.preference_detector import detect_response_preference, analyze_preference_strength


async def test_api_functionality():
    """Test the preference detection functions that will be used by the API"""
    
    print("Testing Preference Detection API Functions")
    print("=" * 50)
    
    test_cases = [
        "I prefer charts and graphs",
        "Give me detailed text explanations", 
        "I'm a visual learner who likes dashboards",
        "Show me comprehensive written analysis",
        "Hello, I work in finance",
        "I like both visual and text content"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: '{text}'")
        
        # Test basic detection
        basic_result = detect_response_preference(text)
        print(f"  Basic Detection: {basic_result}")
        
        # Test detailed analysis
        detailed_result = analyze_preference_strength(text)
        print(f"  Detailed Analysis:")
        print(f"    Preference: {detailed_result['preference']}")
        print(f"    Confidence: {detailed_result['confidence']}")
        print(f"    Visual Keywords: {detailed_result['visual_keywords']}")
        print(f"    Text Keywords: {detailed_result['text_keywords']}")


if __name__ == "__main__":
    asyncio.run(test_api_functionality())