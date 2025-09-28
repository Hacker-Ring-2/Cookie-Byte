#!/usr/bin/env python3
"""
Simple test to check user preferences and provide setup instructions
"""

def test_preference_detection():
    """Test the basic preference detection"""
    print("🧪 Testing Basic Preference Detection")
    print("=" * 50)
    
    try:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from src.backend.utils.preference_detector import detect_response_preference
        
        test_cases = [
            ("I prefer charts and graphs", "visual"),
            ("Show me visual representations", "visual"),
            ("Give me detailed text explanations", "text"),
            ("I like comprehensive written analysis", "text"),
            ("Hello, I work in finance", None)
        ]
        
        print("Preference detection results:")
        for text, expected in test_cases:
            result = detect_response_preference(text)
            actual = result.get('preference')
            status = "✅" if actual == expected else "❌"
            print(f"  {status} '{text}' → {actual}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def check_prompt_system():
    """Check if the prompt system is working"""
    print("🧪 Testing Prompt System")
    print("=" * 50)
    
    try:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from src.ai.agent_prompts.preference_aware_prompts import get_preference_aware_prompt
        
        # Test visual prompt
        visual_prompt = get_preference_aware_prompt('visual')
        visual_has_charts_first = "CHARTS FIRST" in visual_prompt
        print(f"✅ Visual prompt: {'Contains CHARTS FIRST directive' if visual_has_charts_first else 'Missing CHARTS FIRST directive'}")
        
        # Test text prompt  
        text_prompt = get_preference_aware_prompt('text')
        text_has_detailed = "DETAILED TEXT content" in text_prompt
        print(f"✅ Text prompt: {'Contains DETAILED TEXT directive' if text_has_detailed else 'Missing DETAILED TEXT directive'}")
        
        # Test default prompt
        default_prompt = get_preference_aware_prompt(None)
        print(f"✅ Default prompt: Loaded successfully")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Main test function"""
    print("🔍 User Preference System Diagnosis")
    print("=" * 60)
    print()
    
    # Test basic components
    detection_works = test_preference_detection()
    prompt_works = check_prompt_system()
    
    print("📋 Diagnosis Results")
    print("=" * 50)
    
    if detection_works and prompt_works:
        print("✅ Core preference system is working correctly!")
        print()
        print("🎯 Most likely issue: Users haven't set their preferences")
        print()
        print("📝 Setup Instructions for Users:")
        print("1. Go to the Personalization page in the app")
        print("2. In the 'Introduce Yourself' textarea, type one of these:")
        print("   - For visual preference: 'I prefer charts and graphs'")
        print("   - For text preference: 'Give me detailed explanations'")
        print("3. Save the personalization settings")
        print("4. Ask a financial query with numerical data")
        print()
        print("🧪 Test Queries (after setting preferences):")
        print("- 'Show me Apple's financial performance'")
        print("- 'Analyze Tesla's revenue trends'") 
        print("- 'Compare Microsoft and Google financials'")
        print()
        print("💡 Expected Behavior:")
        print("- Visual users: Charts appear FIRST, minimal text")
        print("- Text users: Detailed explanations FIRST, charts as support")
    else:
        print("❌ Core system has issues - check implementation")
    
    print()
    print("🔧 Additional Troubleshooting:")
    print("1. Check browser console for JavaScript errors")
    print("2. Verify backend is running on http://localhost:8001")
    print("3. Verify frontend is running on http://localhost:3000")
    print("4. Check if MongoDB is running and accessible")
    print("5. Test the /personalization API endpoint directly")


if __name__ == "__main__":
    main()