"""
Preference Detection Utility

This module analyzes user input from personalization textarea to detect
whether they prefer visual content (charts, graphs, visuals) or text-based
content (detailed explanations, text).
"""

import re
from typing import Dict, Optional


def detect_response_preference(text: str) -> Dict[str, str]:
    """
    Analyze user input text to detect preference for visual, text, or mixed responses.
    
    Args:
        text (str): User input from personalization textarea
        
    Returns:
        Dict[str, str]: Dictionary with 'preference' key containing 'visual', 'text', or 'mixed'
        
    Examples:
        >>> detect_response_preference("I prefer big charts and graphs")
        {'preference': 'visual'}
        
        >>> detect_response_preference("Give me detailed text explanations")
        {'preference': 'text'}
        
        >>> detect_response_preference("I like both charts and detailed explanations")
        {'preference': 'mixed'}
    """
    if not text or not isinstance(text, str):
        return {'preference': None}
    
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Define keywords for visual preferences
    visual_keywords = [
        'chart', 'charts', 'graph', 'graphs', 'visual', 'visuals',
        'diagram', 'diagrams', 'plot', 'plots', 'visualization',
        'visualizations', 'graphic', 'graphics', 'image', 'images',
        'figure', 'figures', 'infographic', 'infographics',
        'dashboard', 'dashboards', 'map', 'maps', 'timeline',
        'timelines', 'flowchart', 'flowcharts', 'pie chart',
        'bar chart', 'line chart', 'scatter plot', 'heatmap',
        'treemap', 'candlestick', 'histogram', 'big charts',
        'large graphs', 'prominent visuals'
    ]
    
    # Define keywords for text preferences
    text_keywords = [
        'text', 'explanation', 'explanations', 'detail', 'details',
        'detailed', 'description', 'descriptions', 'narrative',
        'narratives', 'summary', 'summaries', 'analysis',
        'analyses', 'report', 'reports', 'breakdown',
        'breakdowns', 'insight', 'insights', 'commentary',
        'commentaries', 'discussion', 'discussions',
        'elaborate', 'elaboration', 'comprehensive',
        'thorough', 'in-depth', 'written', 'textual',
        'verbal', 'prose', 'paragraph', 'paragraphs',
        'bullet point', 'bullet points', 'list', 'lists'
    ]
    
    # Define keywords for mixed/balanced preferences
    mixed_keywords = [
        'both', 'balanced', 'combination', 'mix', 'mixed',
        'balance', 'together', 'and', 'plus', 'along with',
        'as well as', 'combined', 'integrate', 'blend'
    ]
    
    # Count matches for each preference type
    visual_score = 0
    text_score = 0
    mixed_score = 0
    
    # Check for visual keywords
    for keyword in visual_keywords:
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(keyword) + r'\b'
        matches = len(re.findall(pattern, text_lower))
        visual_score += matches
    
    # Check for text keywords
    for keyword in text_keywords:
        pattern = r'\b' + re.escape(keyword) + r'\b'
        matches = len(re.findall(pattern, text_lower))
        text_score += matches
    
    # Check for mixed keywords
    for keyword in mixed_keywords:
        pattern = r'\b' + re.escape(keyword) + r'\b'
        matches = len(re.findall(pattern, text_lower))
        mixed_score += matches
    
    # Check for preference-indicating phrases
    visual_phrases = [
        r'\b(prefer|like|want|need|show me|give me|display).{0,20}(big|large|prominent).{0,10}(chart|graph|visual)',
        r'\b(big|large|prominent).{0,10}(chart|graph|visual)',
        r'\b(prefer|like|want|need|show me|give me|display).{0,20}(chart|graph|visual)',
        r'\b(chart|graph|visual).{0,20}(prefer|like|want|need|better)',
        r'\bvisual\w*\s+(person|learner|type)',
        r'\bsee.{0,10}(chart|graph|visual)',
        r'\bshow.{0,10}(chart|graph|visual)',
        r'\b(more|less).{0,10}(chart|graph|visual)',
        r'\bvisualize\b',
        r'\bdashboard\b'
    ]
    
    text_phrases = [
        r'\b(prefer|like|want|need|give me|show me).{0,20}(detailed|comprehensive|thorough).{0,10}(text|explanation|detail)',
        r'\b(detailed|comprehensive|thorough).{0,10}(text|explanation|detail)',
        r'\b(prefer|like|want|need|give me|show me).{0,20}(text|explanation|detail)',
        r'\b(text|explanation|detail).{0,20}(prefer|like|want|need|better)',
        r'\btext\w*\s+(person|learner|type)',
        r'\bread.{0,10}(text|explanation|detail)',
        r'\bexplain.{0,10}(detail|thorough)',
        r'\b(more|less).{0,20}(text|explanation|detail)',
        r'\bbut.{0,10}(prefer|like).{0,10}(text|explanation|detail)'
    ]
    
    mixed_phrases = [
        r'\b(both|combination|mix|balance).{0,20}(chart|graph|visual).{0,20}(text|explanation|detail)',
        r'\b(both|combination|mix|balance).{0,20}(text|explanation|detail).{0,20}(chart|graph|visual)',
        r'\b(chart|graph|visual).{0,20}(and|plus|with).{0,20}(text|explanation|detail)',
        r'\b(text|explanation|detail).{0,20}(and|plus|with).{0,20}(chart|graph|visual)',
        r'\bbalanced.{0,20}(approach|content|response)',
        r'\bmix.{0,20}of.{0,20}(visual|text)',
        r'\bcombine.{0,20}(visual|text)',
        r'\bintegrate.{0,20}(chart|graph|visual).{0,20}(text|explanation)'
    ]
    
    # Check visual phrases
    for phrase in visual_phrases:
        if re.search(phrase, text_lower):
            visual_score += 2  # Phrases get higher weight
    
    # Check text phrases
    for phrase in text_phrases:
        if re.search(phrase, text_lower):
            text_score += 2  # Phrases get higher weight
    
    # Check mixed phrases
    for phrase in mixed_phrases:
        if re.search(phrase, text_lower):
            mixed_score += 3  # Mixed phrases get highest weight
    
    # Determine preference based on scores
    # If mixed indicators are present and there are both visual and text elements
    if mixed_score > 0 and visual_score > 0 and text_score > 0:
        return {'preference': 'mixed'}
    elif mixed_score > max(visual_score, text_score):
        return {'preference': 'mixed'}
    elif visual_score > text_score and visual_score > mixed_score:
        return {'preference': 'visual'}
    elif text_score > visual_score and text_score > mixed_score:
        return {'preference': 'text'}
    else:
        # If scores are equal or all are zero, return None
        return {'preference': None}


def analyze_preference_strength(text: str) -> Dict[str, any]:
    """
    Analyze preference with confidence score and detected keywords.
    
    Args:
        text (str): User input text
        
    Returns:
        Dict containing preference, confidence score, and detected keywords
    """
    if not text or not isinstance(text, str):
        return {
            'preference': None,
            'confidence': 0.0,
            'visual_keywords': [],
            'text_keywords': [],
            'total_keywords': 0
        }
    
    text_lower = text.lower()
    
    visual_keywords = [
        'chart', 'charts', 'graph', 'graphs', 'visual', 'visuals',
        'diagram', 'diagrams', 'plot', 'plots', 'visualization',
        'graphic', 'graphics', 'dashboard', 'map', 'timeline'
    ]
    
    text_keywords = [
        'text', 'explanation', 'explanations', 'detail', 'details',
        'detailed', 'description', 'analysis', 'report', 'summary',
        'elaborate', 'comprehensive', 'thorough', 'in-depth'
    ]
    
    found_visual = []
    found_text = []
    
    # Find matching keywords
    for keyword in visual_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
            found_visual.append(keyword)
    
    for keyword in text_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
            found_text.append(keyword)
    
    visual_score = len(found_visual)
    text_score = len(found_text)
    total_keywords = visual_score + text_score
    
    # Calculate confidence based on keyword density and total matches
    word_count = len(text.split())
    keyword_density = total_keywords / max(word_count, 1)
    
    if total_keywords == 0:
        preference = None
        confidence = 0.0
    elif visual_score > text_score:
        preference = 'visual'
        confidence = min(0.9, 0.3 + (visual_score * 0.2) + (keyword_density * 0.5))
    elif text_score > visual_score:
        preference = 'text'
        confidence = min(0.9, 0.3 + (text_score * 0.2) + (keyword_density * 0.5))
    else:
        preference = None
        confidence = 0.0
    
    return {
        'preference': preference,
        'confidence': round(confidence, 2),
        'visual_keywords': found_visual,
        'text_keywords': found_text,
        'total_keywords': total_keywords
    }