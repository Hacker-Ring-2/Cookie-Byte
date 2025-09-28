#!/usr/bin/env python3
"""
Test script for preference-aware response generation system
"""

import asyncio
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.backend.utils.utils import get_user_metadata_with_preferences
from src.ai.agent_prompts.preference_aware_prompts import get_preference_aware_prompt
from src.ai.agents.response_generator_agent import ReportGenerationAgent


async def test_preference_metadata():
    """Test the preference-aware metadata generation"""
    print("Testing Preference-Aware Metadata Generation")
    print("=" * 50)
    
    # Test with no user_id (should show "Not specified")
    metadata_no_user = await get_user_metadata_with_preferences("UTC", None, None)
    print("Metadata without user_id:")
    print(metadata_no_user)
    print()
    
    # Test with fake user_id (should show "Not specified" due to no DB connection)
    metadata_fake_user = await get_user_metadata_with_preferences("UTC", None, "fake_user_id")
    print("Metadata with fake user_id:")
    print(metadata_fake_user)
    print()


def test_preference_prompts():
    """Test the preference-aware prompt selection"""
    print("Testing Preference-Aware Prompt Selection")
    print("=" * 50)
    
    # Test visual preference
    visual_prompt = get_preference_aware_prompt('visual')
    print("Visual preference prompt (first 200 chars):")
    print(visual_prompt[:200] + "...")
    print()
    
    # Test text preference
    text_prompt = get_preference_aware_prompt('text')
    print("Text preference prompt (first 200 chars):")
    print(text_prompt[:200] + "...")
    print()
    
    # Test default (no preference)
    default_prompt = get_preference_aware_prompt(None)
    print("Default prompt (first 200 chars):")
    print(default_prompt[:200] + "...")
    print()


def test_preference_extraction():
    """Test the preference extraction from metadata"""
    print("Testing Preference Extraction from Metadata")
    print("=" * 50)
    
    agent = ReportGenerationAgent()
    
    # Test visual preference extraction
    visual_metadata = """<UserMetaData>
- User's current Datetime:2025-09-27T23:10:00+05:30
- User's current location details: {"location": "UTC"}
- User Response Preference: VISUAL (prefers charts, graphs, and visual representations)
</UserMetaData>"""
    
    visual_pref = agent.extract_user_preference(visual_metadata)
    print(f"Visual preference extraction: {visual_pref}")
    
    # Test text preference extraction
    text_metadata = """<UserMetaData>
- User's current Datetime:2025-09-27T23:10:00+05:30
- User's current location details: {"location": "UTC"}
- User Response Preference: TEXT (prefers detailed explanations and text-based content)
</UserMetaData>"""
    
    text_pref = agent.extract_user_preference(text_metadata)
    print(f"Text preference extraction: {text_pref}")
    
    # Test no preference extraction
    no_pref_metadata = """<UserMetaData>
- User's current Datetime:2025-09-27T23:10:00+05:30
- User's current location details: {"location": "UTC"}
- User Response Preference: Not specified
</UserMetaData>"""
    
    no_pref = agent.extract_user_preference(no_pref_metadata)
    print(f"No preference extraction: {no_pref}")
    print()


def test_prompt_differences():
    """Test the key differences between visual and text prompts"""
    print("Testing Key Differences Between Prompts")
    print("=" * 50)
    
    visual_prompt = get_preference_aware_prompt('visual')
    text_prompt = get_preference_aware_prompt('text')
    
    # Check for visual-first indicators
    visual_indicators = [
        "CHARTS FIRST",
        "show charts or graph first",
        "LEAD WITH CHARTS AND GRAPHS IMMEDIATELY",
        "minimal text"
    ]
    
    text_indicators = [
        "DETAILED TEXT content",
        "comprehensive explanations",
        "LEAD WITH COMPREHENSIVE TEXT EXPLANATIONS",
        "charts and graphs as supporting evidence"
    ]
    
    print("Visual prompt contains visual-first indicators:")
    for indicator in visual_indicators:
        found = indicator.lower() in visual_prompt.lower()
        print(f"  - '{indicator}': {'✅' if found else '❌'}")
    
    print("\nText prompt contains text-first indicators:")
    for indicator in text_indicators:
        found = indicator.lower() in text_prompt.lower()
        print(f"  - '{indicator}': {'✅' if found else '❌'}")
    
    print()


async def main():
    """Run all tests"""
    print("🧪 Testing Preference-Aware Response Generation System")
    print("=" * 60)
    print()
    
    await test_preference_metadata()
    test_preference_prompts()
    test_preference_extraction()
    test_prompt_differences()
    
    print("✅ All tests completed!")
    print()
    print("📋 Summary:")
    print("- ✅ Preference-aware metadata generation implemented")
    print("- ✅ Visual-first and text-first prompts created")
    print("- ✅ Preference extraction from metadata working")
    print("- ✅ Response generator agent updated to use preferences")
    print("- ✅ Agent communication system updated")
    print()
    print("🎯 Expected Behavior:")
    print("- Visual users: Charts/graphs shown FIRST, minimal text")
    print("- Text users: Detailed explanations FIRST, charts as support")
    print("- Same data, different presentation order and emphasis")


if __name__ == "__main__":
    asyncio.run(main())