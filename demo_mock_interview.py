"""
Demo script for Mock Interview Analyzer
Shows how to use the core components
"""

import sys
import os

# Add the mock_interview module to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'mock_interview'))

def demo_analyzer():
    """Demo the interview analyzer"""
    print("🎤 Mock Interview Analyzer Demo")
    print("=" * 40)
    
    try:
        from mock_interview.core.interview_analyzer import InterviewAnalyzer
        
        analyzer = InterviewAnalyzer()
        
        # Demo scenarios
        scenarios = [
            {
                'name': 'Good Technical Response',
                'transcript': 'I have extensive experience with Python programming and machine learning. I worked on several projects involving data analysis and model development using scikit-learn and TensorFlow.',
                'ideal': 'Python, machine learning, data analysis, scikit-learn, TensorFlow, programming, experience'
            },
            {
                'name': 'Poor Response',
                'transcript': 'Um, like, I know some stuff about, you know, programming and things.',
                'ideal': 'Python, machine learning, data analysis, programming'
            },
            {
                'name': 'Behavioral Response',
                'transcript': 'I had a challenging situation where I had to work with a difficult team member. I focused on clear communication and finding common ground.',
                'ideal': 'teamwork, communication, problem-solving, leadership, collaboration'
            }
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n--- Scenario {i}: {scenario['name']} ---")
            print(f"Transcript: {scenario['transcript']}")
            print(f"Ideal Answer: {scenario['ideal']}")
            
            # Analyze the response
            analysis = analyzer.analyze_response(
                transcript=scenario['transcript'],
                ideal_answer=scenario['ideal']
            )
            
            # Display results
            overall = analysis.get('overall_score', {})
            print(f"\n📊 Analysis Results:")
            print(f"Overall Score: {overall.get('score', 0):.1%} (Grade: {overall.get('grade', 'N/A')})")
            
            # Individual metrics
            metrics = ['clarity', 'sentiment', 'keyword_match', 'fluency']
            for metric in metrics:
                if metric in analysis:
                    score = analysis[metric].get('score', 0)
                    details = analysis[metric].get('details', '')
                    print(f"{metric.title()}: {score:.1%} - {details}")
            
            # Generate feedback
            feedback = analyzer.generate_feedback(analysis)
            print(f"\n💡 Feedback:")
            print(feedback)
            
            print("-" * 50)
        
        print("\n✅ Demo completed successfully!")
        
    except Exception as e:
        print(f"❌ Demo error: {e}")

def demo_audio_processor():
    """Demo the audio processor"""
    print("\n🎙️ Audio Processor Demo")
    print("=" * 30)
    
    try:
        from mock_interview.core.audio_processor import AudioProcessor
        
        processor = AudioProcessor()
        
        # Test with dummy audio data (this will fail gracefully if dependencies missing)
        dummy_audio = b"dummy_audio_data"
        
        print("Testing speech-to-text conversion...")
        result = processor.speech_to_text(dummy_audio)
        print(f"Result: {result}")
        
        print("Testing audio feature analysis...")
        features = processor.analyze_audio_features(dummy_audio)
        print(f"Features extracted: {len(features)} features")
        
        print("✅ Audio processor demo completed!")
        
    except Exception as e:
        print(f"❌ Audio processor error: {e}")

if __name__ == "__main__":
    print("🚀 Starting Mock Interview Analyzer Demo...")
    
    # Demo the analyzer
    demo_analyzer()
    
    # Demo the audio processor
    demo_audio_processor()
    
    print("\n🎉 Demo completed! Run 'streamlit run ui/mock_interview_ui.py' to use the full interface.")
