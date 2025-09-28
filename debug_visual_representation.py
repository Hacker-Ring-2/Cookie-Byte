#!/usr/bin/env python3
"""
Debug script to test visual representation issue
"""

import asyncio
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_preference_prompts():
    """Test if preference prompts are working"""
    print("🔍 Testing Preference Prompts")
    print("=" * 50)
    
    try:
        from src.ai.agent_prompts.preference_aware_prompts import get_preference_aware_prompt
        
        # Test visual preference prompt
        visual_prompt = get_preference_aware_prompt('visual')
        print("✅ Visual preference prompt loaded")
        
        # Check for key visual directives
        visual_checks = [
            ("CHARTS FIRST", "CHARTS FIRST" in visual_prompt),
            ("LEAD WITH CHARTS", "LEAD WITH CHARTS AND GRAPHS IMMEDIATELY" in visual_prompt),
            ("minimal text", "minimal text" in visual_prompt.lower()),
            ("Generate ALL relevant charts", "Generate ALL relevant charts immediately at the start" in visual_prompt)
        ]
        
        print("Visual prompt directives:")
        for check, result in visual_checks:
            print(f"  - {check}: {'✅' if result else '❌'}")
        
        print()
        
        # Test text preference prompt
        text_prompt = get_preference_aware_prompt('text')
        print("✅ Text preference prompt loaded")
        
        # Check for key text directives
        text_checks = [
            ("DETAILED TEXT", "DETAILED TEXT content" in text_prompt),
            ("comprehensive explanations", "comprehensive explanations" in text_prompt.lower()),
            ("LEAD WITH COMPREHENSIVE", "LEAD WITH COMPREHENSIVE TEXT EXPLANATIONS" in text_prompt)
        ]
        
        print("Text prompt directives:")
        for check, result in text_checks:
            print(f"  - {check}: {'✅' if result else '❌'}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error testing prompts: {e}")
        return False


def test_preference_extraction():
    """Test preference extraction logic"""
    print("🔍 Testing Preference Extraction")
    print("=" * 50)
    
    try:
        from src.ai.agents.response_generator_agent import ReportGenerationAgent
        
        agent = ReportGenerationAgent()
        
        # Test visual preference
        visual_metadata = """<UserMetaData>
- User's current Datetime:2025-09-27T23:20:00+05:30
- User's current location details: {"location": "UTC"}
- User Response Preference: VISUAL (prefers charts, graphs, and visual representations)
</UserMetaData>"""
        
        visual_pref = agent.extract_user_preference(visual_metadata)
        print(f"Visual preference extraction: {visual_pref} {'✅' if visual_pref == 'visual' else '❌'}")
        
        # Test text preference
        text_metadata = """<UserMetaData>
- User's current Datetime:2025-09-27T23:20:00+05:30
- User's current location details: {"location": "UTC"}
- User Response Preference: TEXT (prefers detailed explanations and text-based content)
</UserMetaData>"""
        
        text_pref = agent.extract_user_preference(text_metadata)
        print(f"Text preference extraction: {text_pref} {'✅' if text_pref == 'text' else '❌'}")
        
        # Test no preference
        no_pref_metadata = """<UserMetaData>
- User's current Datetime:2025-09-27T23:20:00+05:30
- User's current location details: {"location": "UTC"}
- User Response Preference: Not specified
</UserMetaData>"""
        
        no_pref = agent.extract_user_preference(no_pref_metadata)
        print(f"No preference extraction: {no_pref} {'✅' if no_pref is None else '❌'}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error testing extraction: {e}")
        return False


async def test_metadata_generation():
    """Test metadata generation with preferences"""
    print("🔍 Testing Metadata Generation")
    print("=" * 50)
    
    try:
        from src.backend.utils.utils import get_user_metadata_with_preferences
        
        # Test without user_id
        metadata_no_user = await get_user_metadata_with_preferences("UTC", None, None)
        print("Metadata without user_id:")
        print(metadata_no_user)
        print()
        
        # Test with fake user_id (will show "Not specified" due to no DB)
        metadata_fake_user = await get_user_metadata_with_preferences("UTC", None, "fake_user_123")
        print("Metadata with fake user_id:")
        print(metadata_fake_user)
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing metadata: {e}")
        return False


def test_graph_generation_tool():
    """Test if graph generation tool is available"""
    print("🔍 Testing Graph Generation Tool")
    print("=" * 50)
    
    try:
        from src.ai.tools.graph_gen_tool import graph_tool_list
        
        print(f"Graph tools available: {len(graph_tool_list)}")
        for i, tool in enumerate(graph_tool_list):
            print(f"  {i+1}. {tool.name if hasattr(tool, 'name') else str(tool)}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error testing graph tools: {e}")
        return False


def check_preference_detection_system():
    """Check if preference detection system is working"""
    print("🔍 Testing Preference Detection System")
    print("=" * 50)
    
    try:
        from src.backend.utils.preference_detector import detect_response_preference
        
        # Test visual preference detection
        visual_text = "I prefer charts and graphs for financial data"
        visual_result = detect_response_preference(visual_text)
        print(f"Visual detection: '{visual_text}' → {visual_result}")
        
        # Test text preference detection
        text_text = "Give me detailed text explanations"
        text_result = detect_response_preference(text_text)
        print(f"Text detection: '{text_text}' → {text_result}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error testing preference detection: {e}")
        return False


async def main():
    """Run all debug tests"""
    print("🐛 Debugging Visual Representation Issue")
    print("=" * 60)
    print()
    
    success = True
    
    # Test all components
    success &= test_preference_prompts()
    success &= test_preference_extraction()
    success &= await test_metadata_generation()
    success &= test_graph_generation_tool()
    success &= check_preference_detection_system()
    
    print("🔍 Diagnosis Summary")
    print("=" * 50)
    
    if success:
        print("✅ All components are working correctly")
        print()
        print("🤔 Possible reasons for no visual representation:")
        print("1. Users haven't set their preferences in the personalization page")
        print("2. Database doesn't contain user preference data")
        print("3. User queries don't contain numerical data for chart generation")
        print("4. Graph generation tool might not be triggering")
        print()
        print("💡 Debugging steps:")
        print("1. Check if users have set preferences: Go to personalization page")
        print("2. Test with a query that has numerical data")
        print("3. Check browser console for any errors")
        print("4. Verify database contains preference data")
    else:
        print("❌ Some components have issues - check the errors above")
    
    print()
    print("🧪 Test Query Suggestions:")
    print("- 'Show me Apple's financial performance' (should trigger charts)")
    print("- 'Analyze Tesla's revenue trends' (should generate graphs)")
    print("- 'Compare Microsoft and Google financials' (should create comparison charts)")


if __name__ == "__main__":
    asyncio.run(main())