/**
 * Frontend utility for detecting user response preferences
 * This is a simplified version for immediate feedback before API call
 */

export interface PreferenceResult {
  preference: 'visual' | 'text' | 'mixed' | null;
  confidence?: number;
}

export function detectResponsePreference(text: string): PreferenceResult {
  if (!text || typeof text !== 'string') {
    return { preference: null };
  }

  const textLower = text.toLowerCase();

  // Visual keywords
  const visualKeywords = [
    'chart', 'charts', 'graph', 'graphs', 'visual', 'visuals',
    'diagram', 'diagrams', 'plot', 'plots', 'visualization',
    'graphic', 'graphics', 'dashboard', 'map', 'timeline',
    'pie chart', 'bar chart', 'line chart', 'big charts',
    'large graphs', 'prominent visuals'
  ];

  // Text keywords
  const textKeywords = [
    'text', 'explanation', 'explanations', 'detail', 'details',
    'detailed', 'description', 'analysis', 'report', 'summary',
    'elaborate', 'comprehensive', 'thorough', 'in-depth', 'written'
  ];

  // Mixed keywords
  const mixedKeywords = [
    'both', 'balanced', 'combination', 'mix', 'mixed',
    'balance', 'together', 'and', 'plus', 'along with',
    'as well as', 'combined', 'integrate', 'blend'
  ];

  let visualScore = 0;
  let textScore = 0;
  let mixedScore = 0;

  // Count keyword matches
  visualKeywords.forEach(keyword => {
    const regex = new RegExp(`\\b${keyword}\\b`, 'gi');
    const matches = textLower.match(regex);
    if (matches) visualScore += matches.length;
  });

  textKeywords.forEach(keyword => {
    const regex = new RegExp(`\\b${keyword}\\b`, 'gi');
    const matches = textLower.match(regex);
    if (matches) textScore += matches.length;
  });

  mixedKeywords.forEach(keyword => {
    const regex = new RegExp(`\\b${keyword}\\b`, 'gi');
    const matches = textLower.match(regex);
    if (matches) mixedScore += matches.length;
  });

  // Check for preference phrases
  const visualPhrases = [
    /\b(prefer|like|want|need|show me|give me).{0,20}(big|large|prominent).{0,10}(chart|graph|visual)/i,
    /\b(big|large|prominent).{0,10}(chart|graph|visual)/i,
    /\b(prefer|like|want|need|show me|give me).{0,20}(chart|graph|visual)/i,
    /\bvisual\w*\s+(person|learner|type)/i,
    /\bvisualize\b/i
  ];

  const textPhrases = [
    /\b(prefer|like|want|need|give me|show me).{0,20}(detailed|comprehensive|thorough).{0,10}(text|explanation|detail)/i,
    /\b(detailed|comprehensive|thorough).{0,10}(text|explanation|detail)/i,
    /\b(prefer|like|want|need|give me|show me).{0,20}(text|explanation|detail)/i,
    /\btext\w*\s+(person|learner|type)/i,
    /\bexplain.{0,10}(detail|thorough)/i
  ];

  const mixedPhrases = [
    /\b(both|combination|mix|balance).{0,20}(chart|graph|visual).{0,20}(text|explanation|detail)/i,
    /\b(both|combination|mix|balance).{0,20}(text|explanation|detail).{0,20}(chart|graph|visual)/i,
    /\b(chart|graph|visual).{0,20}(and|plus|with).{0,20}(text|explanation|detail)/i,
    /\b(text|explanation|detail).{0,20}(and|plus|with).{0,20}(chart|graph|visual)/i,
    /\bbalanced.{0,20}(approach|content|response)/i,
    /\bmix.{0,20}of.{0,20}(visual|text)/i
  ];

  visualPhrases.forEach(phrase => {
    if (phrase.test(textLower)) visualScore += 2;
  });

  textPhrases.forEach(phrase => {
    if (phrase.test(textLower)) textScore += 2;
  });

  mixedPhrases.forEach(phrase => {
    if (phrase.test(textLower)) mixedScore += 3;
  });

  // Determine preference
  // If mixed indicators are present and there are both visual and text elements
  if (mixedScore > 0 && visualScore > 0 && textScore > 0) {
    return { preference: 'mixed', confidence: Math.min(0.9, 0.4 + mixedScore * 0.2) };
  } else if (mixedScore > Math.max(visualScore, textScore)) {
    return { preference: 'mixed', confidence: Math.min(0.9, 0.3 + mixedScore * 0.2) };
  } else if (visualScore > textScore && visualScore > mixedScore) {
    return { preference: 'visual', confidence: Math.min(0.9, 0.3 + visualScore * 0.15) };
  } else if (textScore > visualScore && textScore > mixedScore) {
    return { preference: 'text', confidence: Math.min(0.9, 0.3 + textScore * 0.15) };
  } else {
    return { preference: null, confidence: 0 };
  }
}

export function getPreferenceDisplayText(preference: 'visual' | 'text' | 'mixed' | null): string {
  switch (preference) {
    case 'visual':
      return 'Visual content (big charts, graphs, brief summary text)';
    case 'text':
      return 'Text-based content (detailed explanations, small supporting charts)';
    case 'mixed':
      return 'Balanced content (equal mix of charts, graphs and text)';
    default:
      return 'No specific preference detected';
  }
}

export function getPreferenceColor(preference: 'visual' | 'text' | 'mixed' | null): string {
  switch (preference) {
    case 'visual':
      return 'bg-blue-500';
    case 'text':
      return 'bg-green-500';
    case 'mixed':
      return 'bg-purple-500';
    default:
      return 'bg-gray-400';
  }
}