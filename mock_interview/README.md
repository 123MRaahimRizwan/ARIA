# 🎤 Mock Interview Analyzer

A comprehensive AI-powered interview analysis system that evaluates speech clarity, confidence, sentiment, and keyword matching to help candidates improve their interview performance.

## 🌟 Features

### Core Analysis Capabilities
- **Clarity Analysis**: Evaluates speech clarity, filler word usage, and sentence structure
- **Confidence Assessment**: Analyzes audio features like volume, pitch variation, and speech rate
- **Sentiment Analysis**: Determines emotional tone (positive/neutral/negative) using multiple NLP techniques
- **Keyword Matching**: Advanced semantic matching with ideal answers and technical term recognition
- **Fluency Evaluation**: Assesses coherence, repetition, and speech flow

### User Interface
- **Interactive UI**: Streamlit-based interface with real-time analysis
- **Audio Recording**: Browser-based audio capture and file upload support
- **Visual Analytics**: Progress bars, metrics, and color-coded scoring
- **Session Management**: Track multiple questions and responses
- **Export Options**: Generate detailed reports and JSON exports

## 🚀 Quick Start

### Installation

The module works with optional dependencies for enhanced functionality:

```bash
# Core dependencies (required)
pip install streamlit numpy

# Enhanced audio processing (optional)
pip install speech_recognition librosa soundfile

# Enhanced NLP (optional)
pip install textblob nltk
```

### Basic Usage

```python
from mock_interview.core.interview_analyzer import InterviewAnalyzer
from mock_interview.core.audio_processor import AudioProcessor

# Initialize components
analyzer = InterviewAnalyzer()
audio_processor = AudioProcessor()

# Analyze a response
analysis = analyzer.analyze_response(
    transcript="I have experience with Python programming and machine learning.",
    ideal_answer="Python, machine learning, programming, experience"
)

print(f"Overall Score: {analysis['overall_score']['score']:.1%}")
```

### Using the UI

```python
# Run the Streamlit interface
streamlit run ui/mock_interview_ui.py
```

## 📊 Analysis Metrics

### Clarity Score
- **Filler Word Detection**: Identifies and penalizes excessive use of "um", "uh", "like"
- **Sentence Structure**: Analyzes average sentence length and complexity
- **Word Complexity**: Evaluates appropriate use of technical terminology
- **Repetition Analysis**: Detects and penalizes excessive word repetition

### Confidence Score
- **Volume Analysis**: Measures speaking volume and consistency
- **Pitch Variation**: Analyzes voice pitch changes (indicates confidence)
- **Speech Rate**: Evaluates words per minute (optimal ~150 WPM)
- **Pause Detection**: Identifies and penalizes excessive pauses

### Sentiment Analysis
- **Multi-Model Approach**: Uses TextBlob and VADER sentiment analysis
- **Fallback System**: Keyword-based sentiment when NLP libraries unavailable
- **Emotional Tone**: Categorizes responses as positive, neutral, or negative

### Keyword Matching
- **Direct Matching**: Exact keyword overlap with ideal answers
- **Semantic Matching**: Synonym and related term recognition
- **Technical Bonus**: Extra points for appropriate technical terminology
- **Weighted Scoring**: Combines direct and semantic matching

### Fluency Score
- **Coherence**: Evaluates logical flow and organization
- **Completeness**: Assesses sentence completion and structure
- **Repetition**: Penalizes excessive word or phrase repetition
- **Flow**: Analyzes natural speech patterns

## 🎯 Question Categories

### Technical Questions
- Data structures and algorithms
- System design and architecture
- Programming languages and frameworks
- Database and networking concepts

### Behavioral Questions
- Team collaboration and conflict resolution
- Learning and adaptation scenarios
- Problem-solving and decision-making
- Leadership and communication

### General Questions
- Self-introduction and background
- Career goals and motivation
- Strengths and areas for improvement
- Company and role interest

## 🔧 Configuration

### Interview Settings
```python
# Configure analysis parameters
analyzer = InterviewAnalyzer()

# Customize scoring weights
weights = {
    'clarity': 0.25,
    'confidence': 0.25,
    'sentiment': 0.15,
    'keyword_match': 0.20,
    'fluency': 0.15
}
```

## 📈 Reporting

### Session Summary
- Average performance across all questions
- Performance trends (improving/declining/stable)
- Best and worst performing areas
- Overall recommendations

### Individual Analysis
- Detailed scoring for each metric
- Specific feedback and improvement suggestions
- Keyword matching results
- Audio quality assessment

### Export Options
- **Text Report**: Comprehensive analysis in text format
- **JSON Export**: Machine-readable session data
- **Session Management**: Save and resume interview sessions

## 🛠️ Advanced Features

### Audio Processing
- **Speech-to-Text**: Google Speech Recognition integration
- **Audio Analysis**: Volume, pitch, and quality metrics
- **File Support**: WAV, MP3, OGG, WebM, M4A formats
- **Real-time Processing**: Live audio analysis capabilities

### Dependency Management
- **Graceful Fallbacks**: Works without optional dependencies
- **Progressive Enhancement**: Better analysis with more libraries
- **Error Handling**: Robust error handling and user feedback

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_mock_interview.py
```

Run the demo:

```bash
python demo_mock_interview.py
```

### Test Coverage
- Module imports and dependencies
- Analysis algorithms
- Audio processing
- Dependency fallbacks
- Comprehensive scenarios

## 📝 Example Usage

### Complete Interview Session

```python
from mock_interview.core.interview_analyzer import InterviewAnalyzer

# Initialize
analyzer = InterviewAnalyzer()

# Sample questions and responses
questions = [
    "Tell me about yourself.",
    "What are your greatest strengths?",
    "Describe a challenging project you worked on."
]

responses = [
    "I am a software engineer with 5 years of experience in Python development.",
    "My greatest strengths include problem-solving skills and attention to detail.",
    "I worked on a machine learning project that involved processing large datasets."
]

ideal_answers = [
    "software engineer, experience, Python, development",
    "problem-solving, attention to detail, strengths",
    "machine learning, project, datasets, challenging"
]

# Analyze each response
for question, response, ideal in zip(questions, responses, ideal_answers):
    analysis = analyzer.analyze_response(
        transcript=response,
        ideal_answer=ideal
    )
    
    score = analysis['overall_score']['score']
    print(f"Score: {score:.1%}")
    
    # Generate feedback
    feedback = analyzer.generate_feedback(analysis)
    print(f"Feedback: {feedback}")
```

## 🤝 Contributing

### Adding New Questions
```python
# Add to question bank
new_question = {
    "question": "What is your approach to code review?",
    "category": "technical",
    "difficulty": "Medium",
    "ideal_keywords": ["code review", "quality", "collaboration", "standards"]
}
```

### Custom Analysis Metrics
```python
# Extend analyzer with custom metrics
class CustomAnalyzer(InterviewAnalyzer):
    def _analyze_custom_metric(self, text: str) -> Dict:
        # Your custom analysis logic
        return {'score': 0.8, 'details': 'Custom analysis'}
```

## 📚 API Reference

### InterviewAnalyzer
- `analyze_response(transcript, ideal_answer, audio_features)`: Main analysis method
- `generate_feedback(analysis)`: Generate human-readable feedback
- `_analyze_clarity(text)`: Clarity analysis
- `_analyze_sentiment(text)`: Sentiment analysis
- `_analyze_keyword_match(transcript, ideal_answer)`: Keyword matching
- `_analyze_fluency(text)`: Fluency analysis

### AudioProcessor
- `speech_to_text(audio_data)`: Convert audio to text
- `analyze_audio_features(audio_data)`: Analyze audio characteristics
- `save_audio_file(audio_data, filename)`: Save audio to file

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Install missing dependencies or use fallback mode
2. **Audio Processing**: Ensure audio format compatibility
3. **Speech Recognition**: Check internet connection for Google Speech API
4. **Memory Issues**: Process audio in smaller chunks for large files

### Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Enable detailed logging
analyzer = InterviewAnalyzer()
```

## 📄 License

This module is part of the ARIA (Agentic Resume Intelligence Analyzer) project.

## 🙏 Acknowledgments

- Streamlit for the UI framework
- Google Speech Recognition for speech-to-text
- NLTK and TextBlob for NLP capabilities
- Librosa for audio processing
- The open-source community for various dependencies
